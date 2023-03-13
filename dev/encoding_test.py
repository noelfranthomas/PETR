import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os
import pprint


collection = pd.DataFrame(columns=['category', 'full_path', 'condition', 'content'])
categories = next(os.walk('/Users/noelthomas/Documents/GitHub/PETR/data/'))[1]

for category in categories:
    files = os.listdir(f'/Users/noelthomas/Documents/GitHub/PETR/data/{category}')

    for f in files:
        conditions = f.replace("-", " ")
        condition = f.replace(".md", "")
        collection = collection.append(
            {'category': category,
                'full_path': f'/Users/noelthomas/Documents/GitHub/PETR/data/{category}/{f}',
                'condition': condition,
                'content': open(f'/Users/noelthomas/Documents/GitHub/PETR/data/{category}/{f}', "r").read()}, ignore_index=True)
print()
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(collection[collection['category'] == 'copd'].head())

from sentence_transformers import SentenceTransformer
text = df['text']
encoder = SentenceTransformer("paraphrase-mpnet-base-v2")
vectors = encoder.encode(text)

## DEV Experiment