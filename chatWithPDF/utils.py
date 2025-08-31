# ragapi/utils.py
import tempfile
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
# from langchain_perplexity import ChatPerplexity
from langchain_community.document_loaders import PyPDFLoader
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Initialize LLM
llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation"
)
model = ChatHuggingFace(llm=llm)

def summarize_pdf(pdf_file):
    """Takes an uploaded PDF file, extracts text, and summarizes it."""
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        for chunk in pdf_file.chunks():
            tmp_file.write(chunk)
        tmp_path = tmp_file.name

    loader = PyPDFLoader(tmp_path)
    pages = loader.load()
    pdf_text = "\n".join([page.page_content for page in pages])

    if len(pdf_text) > 4000:
        pdf_text = pdf_text[:4000]

    prompt = f"Summarize the following text in a clear, concise way:\n\n{pdf_text}"
    result = model.invoke(prompt)
    return result.content if hasattr(result, "content") else result


def ask_pdf(pdf_file, question):
    """Takes a PDF and a question, answers based on content."""
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        for chunk in pdf_file.chunks():
            tmp_file.write(chunk)
        tmp_path = tmp_file.name

    loader = PyPDFLoader(tmp_path)
    pages = loader.load()
    pdf_text = "\n".join([page.page_content for page in pages])

    text_to_use = pdf_text[:4000] if len(pdf_text) > 4000 else pdf_text
    chat_prompt = f"Answer the following question based ONLY on the provided PDF content.\n\nPDF Content:\n{text_to_use}\n\nQuestion: {question}"
    result = model.invoke(chat_prompt)
    return result.content if hasattr(result, "content") else result


def test_llm(question):
    """Simple test to check if LLM is working."""
    # prompt = "What is the capital of India?"
    result = model.invoke(question)
    return result.content if hasattr(result, "content") else result