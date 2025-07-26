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
