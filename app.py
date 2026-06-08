from fastapi import FastAPI, HTTPException, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import tempfile
import os

from pdf_loader import load_pdf
from doc_split import split_docs
from chain import multi_summary, final_summary
from make_prompt import classprompt

load_dotenv()

app = FastAPI(
    title="Legal Document Summarizer API",
    description="API for AI-powered legal document summarization",
    version="0.1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

llm = ChatOpenAI(model="gpt-5-nano")


@app.get("/")
def health_check():
    return {"status": "ok", "message": "Legal Summarizer API is running"}


@app.post("/summarize")
async def summarize_document(file: UploadFile = File(...)):
    # validate file type
    if not file.filename or not file.filename.endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are supported")

    # save uploaded file to temp location
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
            content = await file.read()
            tmp.write(content)
            tmp_path = tmp.name

        # run summarization pipeline
        docs, chain_type = load_pdf(tmp_path)

        if chain_type == "map_reduce":
            chunks = split_docs(docs)
            map_prompt = classprompt().map_prompt()
            summaries = multi_summary(map_prompt, llm, chunks)
            combine_prompt = classprompt().final_prompt()
            result = final_summary(combine_prompt, llm, summaries)
        else:
            final_prompt = classprompt().final_prompt()
            result = final_summary(final_prompt, llm, docs)

        return {
            "status": "success",
            "filename": file.filename,
            "strategy": chain_type,
            "summary": result
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    finally:
        # cleanup temp file
        if os.path.exists(tmp_path):
            os.remove(tmp_path)