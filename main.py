# --- packages ---
import os, asyncio
import os
from agent_framework.azure import AzureOpenAIResponsesClient
from azure.identity import DefaultAzureCredential
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

    def get_state(self) -> Annotated[str, "output string"]:
        """Gets all lights and their state"""
        return str(self.lights)

    def change_state(self, id: int, is_on: bool) -> Annotated[str, "output string"]:
        """Change light state"""
        for light in self.lights:
            if light["id"] == id:
                light["is_on"] = is_on
                return str(light)
        return "Light not found"


# --- Client ---
client = AzureOpenAIResponsesClient(
    endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"), # env variable AZURE_OPENAI_ENDPOINT
    api_key=os.getenv("AZURE_OPENAI_API_KEY"), # env variable AZURE_OPENAI_API_KEY
    deployment_name=os.getenv("AZURE_OPENAI_CHAT_DEPLOYMENT_NAME") # env variable AZURE_OPENAI_RESPONSES_DEPLOYMENT_NAME
)


# --- Agent ---
plugin = LightsPlugin()
agent = client.create_agent(
    ai_model_id=os.getenv("AZURE_OPENAI_CHAT_DEPLOYMENT_NAME"), # env variable AZURE_OPENAI_RESPONSES_DEPLOYMENT_NAME
    instructions=agent_instructions,
    name=agent_name,
    tools=[plugin.get_state, plugin.change_state]
)

# --- Asynchronous invocation ---
async def run_agent(my_agent, question: str) -> str:
    thread = my_agent.get_new_thread()
    response = await my_agent.run(messages=question, thread=thread)
    return response.text

user_inputs = ["Hello", "Please toggle the porch light", "What's the status of all lights?", "Thank you"]

for question in user_inputs:
    print(f"******\nUser: {question}")
    answer = asyncio.run(run_agent(agent, question))
    print(f"\nAnswer: {answer}\n\n")