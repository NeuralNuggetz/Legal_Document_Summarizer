from langchain_text_splitters import RecursiveCharacterTextSplitter
from pdf_loader import load_pdf


def split_docs(docs):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len,
        is_separator_regex=False,
    )
    chunks = text_splitter.split_documents(docs)
    return chunks