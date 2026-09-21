from chains.prompt import general_prompt
from LLM.model.model import (general_purpose_model)



general_llm = general_purpose_model()

general_chain = general_prompt | general_llm

