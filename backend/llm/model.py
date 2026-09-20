from transformers import pipeline
from langchain_huggingface import HuggingFacePipeline

# General-purpose model
def general_purpose_model():
    general_pipe = pipeline(
        "text-generation",
        model="Qwen/Qwen2.5-1.5B-Instruct",
        device_map="auto",
        max_new_tokens=256,
    )

    general_llm = HuggingFacePipeline(
        pipeline=general_pipe
    )

    return general_llm


# Coding model
def coding_model():
    coding_pipe = pipeline(
        "text-generation",
        model="deepseek-ai/deepseek-coder-1.3b-instruct",
        device_map="auto",
        max_new_tokens=256,
    )

    coding_llm = HuggingFacePipeline(
        pipeline=coding_pipe
    )

    return coding_llm