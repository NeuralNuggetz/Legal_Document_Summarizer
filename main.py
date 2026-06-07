from langchain_openai import ChatOpenAI
from  pdf_loader import load_pdf
from docs_splitter import split_docs
from chain import chain
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from rich import print
load_dotenv()



llm = ChatOpenAI(model = "gpt-5-nano")
pdf_file = "test2.pdf"
docs, chain_type = load_pdf(pdf_file)

if chain_type == "map_reduce":
    chunks = split_docs(docs)
    final_chain = chain(
        llm, chain_type
        )
    result = final_chain.invoke(
        {"input_documents": chunks}
        )
    
else:
    final_chain = chain(
        llm, chain_type
        )
    result = final_chain.invoke(
        {"input_documents": docs}
        )

print("="*50)
print("LEGAL DOCUMENT ANALYSIS")
print("="*50)
print(result['output_text'])