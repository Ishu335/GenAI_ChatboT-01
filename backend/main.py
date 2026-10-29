from pydantic import BaseModel
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from LLM.model import general_purpose_model 
from tools.tools import search
# rag
from RAG.rag import RAGRetriever,EmbeddingManager,VectorStoreManager,load_all_pdfs,split_docs

#intergrate 
from intergrate_llm import generate_output


app = FastAPI()

origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
general_llm = general_purpose_model()

def rag():
    chunks=split_docs(load_all_pdfs())
    print("\n**** Chunks ****\n")

    vector_store = VectorStoreManager()
    print("\n**** VectorStoreManager ****\n")

    embedding_manager=EmbeddingManager()
    print("\n**** EmbeddingManager ****\n")

    texts = [doc.page_content for doc in chunks]
    print("\n**** Texts ****\n")

    emebedding = embedding_manager.generate_embeddings(texts)
    print("\n**** Emebedding Done ****\n")

    vector_store.add_documents(chunks, emebedding)
    print("\n**** Vector_store Done ****\n")

    rag_retriever = RAGRetriever(embedding_manager, vector_store)
    print("\n**** RAGRetriever Done ****\n")

    return rag_retriever

rag_retriever=rag()

class Prompt(BaseModel):
    prompt: str
    model: str = "general"

@app.post("/send/prompt")
async def generate(request: Prompt):

    user_prompt = request.prompt
    print(f"\n**** User Prompt: {user_prompt}****\n")
    


    response = generate_output(user_prompt, rag_retriever, general_llm)
    print(f"\n**** LLM Response: {response}****\n")


    return {
        "response": response,
        "model": request.model
    }

