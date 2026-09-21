from transformers import pipeline
from langchain_huggingface import HuggingFacePipeline

# General-purpose model
def general_purpose_model():
    general_pipe = pipeline(
        "text-generation",
        model="Qwen/Qwen2.5-1.5B-Instruct",
        device_map="cpu",
        max_new_tokens=None,
        max_length=500
    )

    general_llm = HuggingFacePipeline(
        pipeline=general_pipe
    )
    return general_llm

