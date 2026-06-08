from langchain_core.prompts import PromptTemplate

class classprompt:
    def final_prompt(self):
        print("- inside final prompt \n")
        self.template = PromptTemplate(
            template="""
            You are a legal expert. Analyze this document and extract:
            - Overall Impression
            - Key Obligations
            - Rights
            - Termination Clauses
            - Red Flags (significant concerns)
            - Suggestions to finalize and reduce risk
            - Concise Summary
    
            Be direct and factual. Do not offer any follow-up help, 
            next steps, or suggestions like "I can also do X for you".
            End your response after the Concise Summary. Nothing more.
    
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