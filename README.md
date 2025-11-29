# Semantic Kernel sample for comparison with Microsoft Agent Framework

## UV Installation
- On Linux / MAC --> `curl -LsSf https://astral.sh/uv/install.sh | sh`
- On Windows --> `powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"`

## Steps
- Create the project root (like `from-sk-to-maf`)
- CD into the folder created in the previous step (`cd from-sk-to-maf`)
- Create / Activate two environments:
  - `uv venv --python 3.12 .venv-sk`
  - `uv venv --python 3.12 .venv-agent`
- Initialize the project root: `uv init --python 3.12`
  - if you used a folder name after `uv`, that folder would be created
  - this will create `project.toml` file in the roow
- Activate the environment
  - Semantic Kernel:
    - Windows: `.\.venv-sk\Scripts\activate`
    - Linux: `source .venv-sk/bin/activate`
  - Microsoft Agent Framework:
    - Windows: `.\.venv-agent\Scripts\activate`
    - Linux: `source .venv-agent/bin/activate`
- Synchronize to create the file structure: `uv sync --active`
- Add the packages: 
  - Semantic Kernel: `(.venv-sk)` PS > `uv add semantic-kernel python-dotenv --active`
  - Microsoft Agent Framework: `(.venv-agent`) PS > `uv add --pre agent-framework python-dotenv --active`
- Syncrhonize to create the file structure: `uv sync --active`
- To deactivate --> `deactivate`

## What this sample does
It uses the **Microsoft Agent Framework** to create an agent that relies on the Azure OpenAI Responses service:
- First, it creates the client ***AzureOpenAIResponsesClient*** to the Azure OpenAI endpoint -like `https://my-azure-openai-resource.openai.azure.com/`- that is [responses-API enabled](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/responses?view=foundry-classic&tabs=python-key).
- Then, it uses the client to create the agent.
- Bonus demo: it engages *AssistantApi* tools like **Function Tools** and **CodeInterpreter**.

## To switch GitHub repository
- Make sure that all changes in the current repo are committed and pushed to GitHub
- Switch to the other repository:
  - Semantic Kernel: `git checkout main`
  - Microsoft Agent Framework: `git checkout appmod/python-semantic-kernel-to-agent-framework-20251128174805`
- DE-Activate the previous environment: `deactivate`
- Activate the environment
  - Semantic Kernel:
    - Windows: `.\.venv-sk\Scripts\activate`
    - Linux: `source .venv-sk/bin/activate`
  - Microsoft Agent Framework:
    - Windows: `.\.venv-agent\Scripts\activate`
    - Linux: `source .venv-agent/bin/activate`

## Reference docs
- [Azure AI Foundry Agents](https://learn.microsoft.com/en-us/agent-framework/user-guide/agents/agent-types/azure-ai-foundry-agent?pivots=programming-language-python)
- This sample adopts [Azure OpenAI APIs next generation v1](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/api-version-lifecycle?view=foundry-classic&tabs=python#api-evolution)
