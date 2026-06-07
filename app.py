from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from rich import print
from pdf_loader import load_pdf
from doc_split import split_docs
from chain import multi_summary, final_summary
from make_prompt import classprompt
load_dotenv()



llm = ChatOpenAI(model = "gpt-5-nano")
pdf_file = "test2.pdf"
docs, chain_type = load_pdf(pdf_file)

if chain_type == "map_reduce":
    chunks = split_docs(docs)
    map_prompt = classprompt().map_prompt()
    summaries = multi_summary(map_prompt, llm, chunks)
    combine_prompt = classprompt().final_prompt()
    final_summary = final_summary(combine_prompt, llm, summaries)
    print(final_summary)

else:

    final_prompt = classprompt().final_prompt()
    final_summary = final_summary(final_prompt, llm, docs)
    print(final_summary)


