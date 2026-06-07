from langchain_core.prompts import PromptTemplate

class classprompt:
    def stuff_prompt(self):
        print("\n"+" ="*50)
        print("Stuff Prompt Selected")
        print("\n"+" ="*50)
        self.template = PromptTemplate(
            template = """
            You are a legal expert. Analyze this document and extract:
            - Key obligations
            - Rights
            - Termination clauses
            - Red flags

            and summarize
            in a clear, concise manner.

            Document: {text}
        """,
        input_variables=["text"]
        )
        return self.template

    def map_reduce_prompt(self):
        print("\n"+" ="*50)
        print("Map Reduce Prompt Selected \n")
        print(" ="*50)

        self.map_prompt = PromptTemplate(
        template="""
        Summarize the following section of a legal document:

        {text}

        Summary:
        """,
        input_variables=["text"]
        )

        self.combine_prompt = PromptTemplate(
            input_variables=["text"],
            template="""
            You are a legal expert. Based on these summaries, provide a final analysis:
            - Key obligations
            - Rights
            - Termination clauses
            - Red flags

            Summaries: {text}

            Final Analysis:
            """
        )

        return self.map_prompt, self.combine_prompt