# --- packages ---
import os, asyncio
import os
from semantic_kernel.agents import AzureResponsesAgent
from semantic_kernel.functions import kernel_function
from typing import Annotated
from dotenv import load_dotenv

# --- Variables ---
if not load_dotenv("./../config/credentials_my.env"):
    print("Environment variables not loaded, execution stopped")
    exit(1)
agent_instructions="You are a clever agent"
agent_name="my_response_agent"

# --- Plugin ---
class LightsPlugin:
    def __init__(self):
        self.lights = [
            {"id": 0, "name": "Table Lamp", "is_on": False},
            {"id": 1, "name": "Porch light", "is_on": False},
            {"id": 2, "name": "Chandelier", "is_on": False},
        ]

    @kernel_function(name="get_lights", description="Gets all lights and their state")
    def get_state(self) -> Annotated[str, "output string"]:
        return str(self.lights)

    @kernel_function(name="change_state", description="Change light state")
    def change_state(self, id: int, is_on: bool) -> Annotated[str, "output string"]:
        for light in self.lights:
            if light["id"] == id:
                light["is_on"] = is_on
                return str(light)
        return "Light not found"


# --- Client ---
client = AzureResponsesAgent.create_client(
    endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"), # env variable AZURE_OPENAI_ENDPOINT
    api_key=os.getenv("AZURE_OPENAI_API_KEY"), # env variable AZURE_OPENAI_API_KEY
    deployment_name=os.getenv("AZURE_OPENAI_CHAT_DEPLOYMENT_NAME") # env variable AZURE_OPENAI_RESPONSES_DEPLOYMENT_NAME
)


# --- Agent ---
agent = AzureResponsesAgent(
    client=client,
    ai_model_id=os.getenv("AZURE_OPENAI_CHAT_DEPLOYMENT_NAME"), # env variable AZURE_OPENAI_RESPONSES_DEPLOYMENT_NAME
    instructions=agent_instructions,
    name=agent_name,
    plugins=[LightsPlugin()]
)

# --- Asynchronous invocation ---
async def run_agent(my_agent:AzureResponsesAgent, question: str) -> str:
    response = ""
    async for r in my_agent.invoke(messages=question):
        # print(r.content)
        response = r.content

    return response

user_inputs = ["Hello", "Please toggle the porch light", "What's the status of all lights?", "Thank you"]

for question in user_inputs:
    print(f"******\nUser: {question}")
    answer = asyncio.run(run_agent(agent, question))
    print(f"\nAnswer: {answer}\n\n")