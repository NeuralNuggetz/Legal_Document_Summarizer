from langchain_text_splitters import RecursiveCharacterTextSplitter

def split_docs(docs):
    print("- Splitting documents into chunks..."+"\n")
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=2000,
        chunk_overlap=200,
        length_function=len,
        is_separator_regex=False,
    )
    chunks = text_splitter.split_documents(docs)
    return chunks