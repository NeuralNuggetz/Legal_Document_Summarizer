from langchain_community.document_loaders import PyPDFLoader

def load_pdf(file_path):
    print("\n"+" ="*50)
    print("Loading PDF and determining optimal chain type..."+"\n")
    print(" ="*50)

    loader = PyPDFLoader(file_path)
    docs = loader.load()


    total_text = " ".join([doc.page_content for doc in docs])
    print(len(total_text))

    if len(total_text) < 10000:
        chain_type = "stuff"
    else:
        chain_type = "map_reduce"
    return docs, chain_type


