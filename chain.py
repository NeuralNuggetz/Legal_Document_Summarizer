from langchain_core.output_parsers import StrOutputParser

def multi_summary(map_prompt, llm, chunks):

    print("- Summarizing chunks..."+"\n")

    # map_chain is already a Runnable
    map_chain = map_prompt | llm | StrOutputParser()

    # .batch() is a Runnable method
    summaries = map_chain.batch(chunks)

    combined = "\n\n".join(summaries)

    return combined


def final_summary(combine_prompt, llm, summaries):

    print("- Combining summaries..."+"\n")

    # combine_chain is already a Runnable
    combine_chain = combine_prompt | llm | StrOutputParser()

    # invoke() is a Runnable method
    final_summary = combine_chain.invoke({"text": summaries})

    return final_summary