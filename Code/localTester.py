# Import necessary libraries
from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
from langchain_core.messages import HumanMessage, SystemMessage

import getpass
import os

if not os.getenv("HUGGINGFACEHUB_API_TOKEN"):
    os.environ["HUGGINGFACEHUB_API_TOKEN"] = getpass.getpass("Enter your token: ")
# above will be needed for llama models since they have you agree to their license in huggingface


model_id = "microsoft/DialoGPT-small"
# model_id = "meta-llama/Llama-3.1-8B"


# Instantiate the model using HuggingFacePipeline
llm = HuggingFacePipeline.from_model_id(
    model_id=model_id,
    task="text-generation",
    pipeline_kwargs={
        "max_new_tokens": 50,
        "do_sample": True,
        "repetition_penalty": 1.1,
    },
)

# Wrap the LLM with ChatHuggingFace
chat_model = ChatHuggingFace(llm=llm)

# Prepare messages
messages = [
    SystemMessage(content="You are a helpful assistant."),
    HumanMessage(content="Hello, how are you?")
]

# Invoke the model
ai_msg = chat_model.invoke(messages)

# Print the response
print(ai_msg.content)
