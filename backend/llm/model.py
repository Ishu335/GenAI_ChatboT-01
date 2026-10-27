from transformers import pipeline
from langchain_huggingface import HuggingFacePipeline
import torch

# General-purpose model

def general_purpose_model():
    general_pipe = pipeline(
        "text-generation",
        model="google/flan-t5-small",
        device_map="auto",
        max_new_tokens=256,
    )

    general_llm = HuggingFacePipeline(
        pipeline=general_pipe
    )

    return general_llm

