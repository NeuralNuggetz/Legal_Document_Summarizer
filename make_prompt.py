from langchain_core.prompts import PromptTemplate

class classprompt:
    def final_prompt(self):
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

    def map_prompt(self):

        self.prompt = PromptTemplate(
        template="""
        Summarize the following section of a legal document:

        {text}

        Summary:
        """,
        input_variables=["text"]
        )

        return self.prompt