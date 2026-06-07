from langchain_classic.chains.summarize import load_summarize_chain
from prompt import classprompt


def chain(llm,chain_type):
    print("\n"+" ="*50)
    print("Loading LLM with the optimal chain type..."+"\n")
    print(" ="*50)

    if chain_type == "map_reduce":
        finalprompt = classprompt()
        map_prompt, combine_prompt = finalprompt.map_reduce_prompt()
        chain = load_summarize_chain(
            llm,
            chain_type="map_reduce",
            map_prompt=map_prompt,
            combine_prompt=combine_prompt
            )
        return chain

    else:
        finalprompt = classprompt()
        prompt = finalprompt.stuff_prompt()
        chain = load_summarize_chain(llm, chain_type="stuff", prompt=prompt)
        return chain


    