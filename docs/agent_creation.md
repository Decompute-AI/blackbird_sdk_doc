# Creating Custom Agents

The Blackbird SDK provides a powerful and flexible framework for creating custom AI agents. You can create agents with specific personalities, capabilities, and instructions to suit your needs.

## Agent Builder

The `AgentBuilder` class is the main entry point for creating custom agents. It provides a fluent and intuitive API for defining your agent's properties.

### Creating an Agent

To create a new agent, you can use the `create_agent` function:

```python
from blackbird_sdk.creation.builder import create_agent

agent = create_agent("my_agent", "A helpful assistant")
```

### Setting Agent Properties

You can set various properties for your agent using the `AgentBuilder` methods:

*   **`personality(personality)`**: Sets the agent's personality. The available personalities are defined in the `AgentPersonality` enum.
*   **`with_capability(capability)`**: Adds a capability to the agent. The available capabilities are defined in the `AgentCapability` enum.
*   **`with_capabilities(capabilities)`**: Adds multiple capabilities to the agent.
*   **`system_prompt(prompt)`**: Sets the agent's system prompt.
*   **`with_function(function)`**: Adds a custom function to the agent.
*   **`with_functions(functions)`**: Adds multiple custom functions to the agent.
*   **`temperature(temp)`**: Sets the agent's temperature.
*   **`max_tokens(tokens)`**: Sets the agent's maximum number of tokens.
*   **`context_length(length)`**: Sets the agent's context length.
*   **`file_types(types)`**: Sets the file types that the agent can process.
*   **`instruction(instruction_type, instruction)`**: Adds a custom instruction to the agent.
*   **`metadata(key, value)`**: Adds metadata to the agent.

### Building the Agent

Once you have configured your agent, you can build it using the `build` method:

```python
sdk = BlackbirdSDK()
custom_agent = agent.build(sdk)
```

## Agent Templates

The SDK also provides a set of pre-built agent templates that you can use as a starting point for creating your own agents.

### Using a Template

To use a template, you can use the `from_template` method:

```python
from blackbird_sdk.creation.builder import create_agent

agent = create_agent("my_agent", "A financial analyst").from_template("financial_analyst")
```

### Available Templates

You can get a list of all available templates using the `list_templates` function:

```python
from blackbird_sdk.creation.templates import AgentTemplates

templates = AgentTemplates.list_templates()
```

You can also get a description of a specific template using the `get_template_description` function:

```python
from blackbird_sdk.creation.templates import AgentTemplates

description = AgentTemplates.get_template_description("financial_analyst")
```

## Agent Types

The SDK defines several enums and classes that are used to configure custom agents.

### AgentPersonality

The `AgentPersonality` enum defines the available personalities for an agent:

*   `PROFESSIONAL`
*   `FRIENDLY`
*   `ANALYTICAL`
*   `CREATIVE`
*   `TECHNICAL`
*   `SUPPORTIVE`
*   `CONCISE`
*   `DETAILED`

### AgentCapability

The `AgentCapability` enum defines the available capabilities for an agent:

*   `FILE_PROCESSING`
*   `WEB_SEARCH`
*   `CALCULATIONS`
*   `CODE_ANALYSIS`
*   `IMAGE_GENERATION`
*   `EMAIL_INTEGRATION`
*   `CALENDAR_MANAGEMENT`
*   `DATA_ANALYSIS`
*   `DOCUMENT_CREATION`
*   `API_INTEGRATION`

### AgentConfig

The `AgentConfig` class is a dataclass that stores all the configuration options for a custom agent.



## Creating and Publishing Agents on the marketplace

```python
from blackbird_sdk import BlackbirdSDK
from blackbird_sdk.creation.builder import create_agent, AgentPersonality, AgentCapability

# Initialize SDK
sdk = BlackbirdSDK()

# Create a custom agent
agent = create_agent(
    name="financial_advisor",
    description="AI agent specialized in financial analysis and investment advice"
).personality(AgentPersonality.ANALYTICAL).with_capabilities([
    AgentCapability.FILE_PROCESSING,
    AgentCapability.WEB_SEARCH,
    AgentCapability.CALCULATIONS
]).system_prompt(
    "You are a professional financial advisor with expertise in investment analysis."
).temperature(0.3).build(sdk)

# Deploy locally
sdk.deploy_custom_agent(agent)

# Publish to marketplace
result = agent.publish_to_marketplace(
    author="your_username",
    display_name="Financial Advisor Pro",
    category="Finance",
    tags=["finance", "investment", "analysis"],
    version="1.0.0",
    marketplace_url='https://marketplace-blackbird.vercel.app/'
)

print(f"Published! Agent ID: {result['agent']['id']}")
```

### Discovering and Using Marketplace Agents

```python
from blackbird_sdk import BlackbirdSDK

sdk = BlackbirdSDK()

# Browse all available agents
agents = sdk.browse_marketplace(marketplace_url='https://marketplace-blackbird.vercel.app/')
for agent in agents:
    print(f"• {agent.display_name} by {agent.author}")
    print(f"  {agent.description}")

# Search for specific agents
finance_agents = sdk.search_marketplace("finance")
print(f"Found {len(finance_agents)} finance agents")

# Load and use an agent from marketplace
agent = sdk.load_agent_from_marketplace('financial_advisor')
response = sdk.send_message_to_custom_agent(
    'financial_advisor', 
    'What should I consider when building an investment portfolio?'
)
print(response)
```

### Using the Web Interface

1. **Browse Agents**: Visit `https://marketplace-blackbird.vercel.app/` to see all available agents
2. **Search**: Use the search box to find agents by keywords
3. **View Details**: Click on agents to see full descriptions and metadata
4. **Deploy**: Use the "Deploy Agent" button for usage instructions

## 🔧 API Reference

### GET /api/agents
Get all active agents
```json
[
  {
    "id": 1,
    "name": "financial_advisor",
    "display_name": "Financial Advisor Pro",
    "description": "AI agent specialized in financial analysis...",
    "author": "blackbird_team",
    "category": "Finance",
    "download_count": 42,
    "rating": 4.8,
    "is_featured": true
  }
]
```

### GET /api/agents/{name}
Get specific agent by name

### POST /api/agents/{name}/download
Download agent configuration (increments download count)

### POST /api/agents
Publish new agent
```json
{
  "name": "my_agent",
  "display_name": "My Custom Agent",
  "description": "Description of what the agent does",
  "author": "your_username",
  "category": "General",
  "tags": ["tag1", "tag2"],
  "config": {
    "name": "my_agent",
    "description": "...",
    "personality": "professional",
    "system_prompt": "...",
    "capabilities": ["file_processing"],
    "temperature": 0.7
  }
}
```

### GET /api/search?q={query}
Search agents by keywords

### GET /api/categories
Get all available agent categories

## 🏷️ Agent Categories

The marketplace supports organizing agents into categories:

- **Finance**: Financial analysis, investment advice, budgeting
- **Development**: Code review, debugging, development tools
- **Data Science**: Data analysis, statistics, machine learning
- **Marketing**: Content strategy, SEO, social media marketing
- **Legal**: Legal research, document analysis, compliance  
- **Research**: Academic research, literature review, fact-checking
- **Education**: Tutoring, learning assistance, curriculum development
- **General**: Multi-purpose and general assistance agents

