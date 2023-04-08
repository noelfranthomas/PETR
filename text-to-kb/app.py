import streamlit as st
import streamlit.components.v1 as components
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
import utils
from kb import KB
from io import StringIO
import time
import os

st.header("Extracting a Knowledge Base from text")

# Loading the model
st_model_load = st.text('Loading NER model... It may take a while.')

@st.cache_resource()
def load_model():
    print("Loading model...")
    tokenizer = AutoTokenizer.from_pretrained("Babelscape/rebel-large")
    model = AutoModelForSeq2SeqLM.from_pretrained("Babelscape/rebel-large")
    print("Model loaded!")
    return tokenizer, model

tokenizer, model = load_model()
st.success('Model loaded!')
st_model_load.text("")


uploaded_file = st.file_uploader("Upload a file", accept_multiple_files=False)

if uploaded_file is not None:

    uploaded_file_name = str(uploaded_file.name).replace(".md", "")
    network_path = f"networks/{uploaded_file_name}_network.html"
    pickle_path = f"pickles/{uploaded_file_name}_pickle.p"

    if not os.path.exists(pickle_path):
        t = time.time()
        text = StringIO(uploaded_file.getvalue().decode("utf-8")).read()
        kb, num_tokens = utils.from_text_to_kb(text, model, tokenizer, "", verbose=True)
        utils.save_network_html(kb, filename=network_path)
        st.write("Inference time: ", time.time() - t, "seconds")
    else:
        kb = utils.load_kb(pickle_path)
        st.write("No inference executed. Network already exists.")

    st.session_state.kb_chart = network_path
    st.session_state.kb_text, num_entities, num_relations = kb.get_textual_representation()

    st.session_state.error_url = None

    st.write("Inference time: ", time.time() - t, "seconds")
    st.write("Number of tokens: ", num_tokens)
    st.write("Number of entities: ", num_entities)
    st.write("Number of relations: ", num_relations)









    # kb chart session state
    if 'kb_chart' not in st.session_state:
        st.session_state.kb_chart = None
    if 'kb_text' not in st.session_state:
        st.session_state.kb_text = None
    if 'error_url' not in st.session_state:
        st.session_state.error_url = None

    # show graph
    if st.session_state.error_url:
        st.markdown(st.session_state.error_url)
    elif st.session_state.kb_chart:
        with st.container():
            st.subheader("Generated KB")
            st.markdown("*You can interact with the graph and zoom.*")
            html_source_code = open(st.session_state.kb_chart, 'r', encoding='utf-8').read()
            background = "<style>:root {background-color: #273346;}</style>"
            components.html(html_source_code + background, width=700, height=700)
            st.markdown(st.session_state.kb_text)

    