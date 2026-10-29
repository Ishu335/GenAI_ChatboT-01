from transformers import pipeline
from langchain_huggingface import HuggingFacePipeline
import torch

from transformers import AutoModelForCausalLM, AutoTokenizer
# General-purpose model

def general_purpose_model():
    hf_pipe = pipeline(
        "text-generation",
        # model="Qwen/Qwen2.5-0.5B-Instruct",
        model="google/flan-t5-small",
        device_map="auto",
        max_new_tokens=256,
        return_full_text=False,
    )

    llm = HuggingFacePipeline(pipeline=hf_pipe)
    return llm
