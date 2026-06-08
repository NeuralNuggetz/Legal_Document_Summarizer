from langchain_community.document_loaders import PyPDFLoader

def load_pdf(file_path):
    print("-Loading PDF and determining optimal chain type..."+"\n")

    loader = PyPDFLoader(file_path)
    docs = loader.load()

    total_text = " ".join([doc.page_content for doc in docs])
    
    if len(total_text) < 10000:
        chain_type = "stuff"

    else:
        chain_type = "map_reduce"
    return docs, chain_type
    

