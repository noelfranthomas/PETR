import chromadb
import os

chroma_client = chromadb.Client()

collection = chroma_client.create_collection(name="petr_vectorstore")

categories = next(os.walk('/Users/noelthomas/Documents/GitHub/PETR/data/'))[1]

for category in categories:
    print(category)
    files = os.listdir(f'/Users/noelthomas/Documents/GitHub/PETR/data/{category}')

    fullpaths = [f'/Users/noelthomas/Documents/GitHub/PETR/data/{category}/{file}' for file in files]
    conditions = [f.replace("-", " ") for f in files]
    
    collection.add(documents=fullpaths, metadatas=[{'category': category}]*len(files), ids=conditions)

if __name__ == "__main__":
    while True:
        print("Enter symptoms: ")
        query = input()
        results = collection.query(
            query_texts=[query],
            n_results=3
        )
        
        print('Possible conditions:')
        print(results['ids'])
        print('Category:')
        print(results['metadatas'])
        print()