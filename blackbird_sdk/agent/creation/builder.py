"""Advanced Agent Builder for creating custom AI agents."""

from typing import Dict, List, Any, Optional, Callable, Union
from dataclasses import dataclass, field
from enum import Enum
import json
import yaml
from pathlib import Path

from ..utils.errors import ValidationError, AgentInitializationError
from ..utils.logger import get_logger
from ..integrations.function_registry import FunctionRegistry

from typing import TYPE_CHECKING
if TYPE_CHECKING:                         # ← no runtime import
    from ..model.model_types import ModelConfig
    from ..session.memory_types import MemoryConfig
# from .templates import AgentTemplates
class AgentPersonality(Enum):
    """Predefined agent personalities."""
    PROFESSIONAL = "professional"
    FRIENDLY = "friendly"
    ANALYTICAL = "analytical"
    CREATIVE = "creative"
    TECHNICAL = "technical"
    SUPPORTIVE = "supportive"
    CONCISE = "concise"
    DETAILED = "detailed"

class AgentCapability(Enum):
    """Agent capabilities that can be enabled."""
    FILE_PROCESSING = "file_processing"
    WEB_SEARCH = "web_search"
    CALCULATIONS = "calculations"
    CODE_ANALYSIS = "code_analysis"
    IMAGE_GENERATION = "image_generation"
    EMAIL_INTEGRATION = "email_integration"
    CALENDAR_MANAGEMENT = "calendar_management"
    DATA_ANALYSIS = "data_analysis"
    DOCUMENT_CREATION = "document_creation"
    API_INTEGRATION = "api_integration"

@dataclass
class AgentConfig:
    """Configuration for a custom agent."""
    name: str
    description: str
    personality: Union[AgentPersonality, str] = AgentPersonality.PROFESSIONAL
    system_prompt: str = ""
    capabilities: List[AgentCapability] = field(default_factory=list)
    custom_functions: List[Callable] = field(default_factory=list)
    model_config: Optional[Any] = None
    memory_config: Optional[Any] = None
    temperature: float = 0.7
    max_tokens: int = 2000
    context_length: int = 4096
    file_types: List[str] = field(default_factory=list)
    custom_instructions: Dict[str, str] = field(default_factory=dict)
    metadata: Dict[str, Any] = field(default_factory=dict)

class CustomAgent:
    """Represents a custom agent created by the user."""

    def __init__(self, config: AgentConfig, sdk_instance=None):
        self.config = config
        self.sdk = sdk_instance
        self.logger = get_logger(f"agent.{config.name}")
        self.function_registry = FunctionRegistry()
        self.is_initialized = False

        # Register custom functions
        for func in config.custom_functions:
            self.function_registry.register_function(func)

    def process_message(self, message: str, options: Dict[str, Any] = None) -> str:
        """Process a message with the custom agent."""
        if not self.is_initialized:
            raise AgentInitializationError("Agent not initialized")

        # Build the complete prompt
        full_prompt = self._build_prompt(message, options)

        # Process with SDK
        if self.sdk:
            # Pass the agent name and model in options
            if options is None:
                options = {}
            if 'agent' not in options:
                options['agent'] = self.config.name
            return self.sdk.chat_service.send_message(full_prompt, options=options)
        else:
            return f"[{self.config.name}] Processed: {message}"

    def _build_prompt(self, message: str, context: Dict[str, Any] = None) -> str:
        """Build the complete prompt for the agent."""
        prompt_parts = []

        # Add system prompt
        if self.config.system_prompt:
            prompt_parts.append(f"System: {self.config.system_prompt}")

        # Add personality
        personality_prompt = self._get_personality_prompt()
        if personality_prompt:
            prompt_parts.append(personality_prompt)

        # Add custom instructions
        for instruction_type, instruction in self.config.custom_instructions.items():
            prompt_parts.append(f"{instruction_type}: {instruction}")

        # Add context if provided
        if context:
            context_str = json.dumps(context, indent=2)
            prompt_parts.append(f"Context: {context_str}")

        # Add the actual message
        prompt_parts.append(f"User: {message}")

        return "\n\n".join(prompt_parts)

    def _get_personality_prompt(self) -> str:
        """Get personality-specific prompt."""
        personality_prompts = {
            AgentPersonality.PROFESSIONAL: "Respond in a professional, formal manner.",
            AgentPersonality.FRIENDLY: "Respond in a warm, friendly, and approachable manner.",
            AgentPersonality.ANALYTICAL: "Provide detailed, analytical responses with logical reasoning.",
            AgentPersonality.CREATIVE: "Think creatively and provide innovative solutions.",
            AgentPersonality.TECHNICAL: "Focus on technical accuracy and provide detailed explanations.",
            AgentPersonality.SUPPORTIVE: "Be encouraging and provide helpful guidance.",
            AgentPersonality.CONCISE: "Provide brief, direct responses.",
            AgentPersonality.DETAILED: "Provide comprehensive, detailed explanations."
        }

        if isinstance(self.config.personality, AgentPersonality):
            return personality_prompts.get(self.config.personality, "")
        return ""

    def add_function(self, function: Callable) -> None:
        """Add a custom function to the agent."""
        self.function_registry.register_function(function)
        self.config.custom_functions.append(function)

    def enable_capability(self, capability: AgentCapability) -> None:
        """Enable a capability for the agent."""
        if capability not in self.config.capabilities:
            self.config.capabilities.append(capability)

    def set_instruction(self, instruction_type: str, instruction: str) -> None:
        """Set a custom instruction for the agent."""
        self.config.custom_instructions[instruction_type] = instruction

    def save_config(self, file_path: str) -> None:
        """Save agent configuration to file."""
        config_dict = {
            'name': self.config.name,
            'description': self.config.description,
            'personality': self.config.personality.value if isinstance(self.config.personality, AgentPersonality) else self.config.personality,
            'system_prompt': self.config.system_prompt,
            'capabilities': [cap.value for cap in self.config.capabilities],
            'temperature': self.config.temperature,
            'max_tokens': self.config.max_tokens,
            'context_length': self.config.context_length,
            'file_types': self.config.file_types,
            'custom_instructions': self.config.custom_instructions,
            'metadata': self.config.metadata
        }

        with open(file_path, 'w') as f:
            yaml.dump(config_dict, f, default_flow_style=False)

    def publish_to_marketplace(self, author: str, display_name: str = None,
                              category: str = "General", tags: list = None,
                              version: str = "1.0.0", marketplace_url: str = "http://localhost:5001"):
        """
        Publish this agent to the Blackbird Agent Marketplace.

        Args:
            author: Your name/username as the agent author
            display_name: Human-readable name for the agent (defaults to config name)
            category: Category for the agent (e.g., "Finance", "Development", "General")
            tags: List of tags for discoverability (e.g., ["finance", "analysis"])
            version: Version string (e.g., "1.0.0")
            marketplace_url: URL of the marketplace server

        Returns:
            Dictionary with publication result

        Example:
            ```python
            # Create and deploy your agent
            agent = create_agent("my_assistant", "Helpful AI assistant").build(sdk)
            sdk.deploy_custom_agent(agent)

            # Publish to marketplace
            result = agent.publish_to_marketplace(
                author="your_username",
                display_name="My Amazing Assistant",
                category="General",
                tags=["helpful", "assistant", "productivity"]
            )
            print(f"Published! Agent ID: {result['agent']['id']}")
            ```
        """
        try:
            from ..marketplace.publisher import AgentPublisher

            publisher = AgentPublisher(marketplace_url)
            result = publisher.publish_custom_agent(
                agent=self,
                author=author,
                display_name=display_name,
                category=category,
                tags=tags or [],
                version=version
            )

            self.logger.info(f"Agent '{self.config.name}' published to marketplace successfully")
            return result

        except ImportError:
            raise RuntimeError("Marketplace functionality not available. Install with: pip install requests flask-sqlalchemy")
        except Exception as e:
            self.logger.error(f"Failed to publish agent to marketplace: {e}")
            raise e

class AgentBuilder:
    """Builder class for creating custom agents."""

    def __init__(self):
        self.config = AgentConfig(name="", description="")
        self.logger = get_logger("agent.builder")

    def name(self, name: str) -> 'AgentBuilder':
        """Set agent name."""
        self.config.name = name
        return self

    def description(self, description: str) -> 'AgentBuilder':
        """Set agent description."""
        self.config.description = description
        return self

    def personality(self, personality: Union[AgentPersonality, str]) -> 'AgentBuilder':
        """Set agent personality."""
        self.config.personality = personality
        return self

    def system_prompt(self, prompt: str) -> 'AgentBuilder':
        """Set system prompt."""
        self.config.system_prompt = prompt
        return self

    def with_capability(self, capability: AgentCapability) -> 'AgentBuilder':
        """Add a capability to the agent."""
        if capability not in self.config.capabilities:
            self.config.capabilities.append(capability)
        return self

    def with_capabilities(self, capabilities: List[AgentCapability]) -> 'AgentBuilder':
        """Add multiple capabilities."""
        for capability in capabilities:
            self.with_capability(capability)
        return self

    def with_function(self, function: Callable) -> 'AgentBuilder':
        """Add a custom function."""
        self.config.custom_functions.append(function)
        return self

    def with_functions(self, functions: List[Callable]) -> 'AgentBuilder':
        """Add multiple custom functions."""
        self.config.custom_functions.extend(functions)
        return self

    def temperature(self, temp: float) -> 'AgentBuilder':
        """Set temperature for response generation."""
        self.config.temperature = temp
        return self

    def max_tokens(self, tokens: int) -> 'AgentBuilder':
        """Set maximum tokens."""
        self.config.max_tokens = tokens
        return self

    def context_length(self, length: int) -> 'AgentBuilder':
        """Set context length."""
        self.config.context_length = length
        return self

    def file_types(self, types: List[str]) -> 'AgentBuilder':
        """Set supported file types."""
        self.config.file_types = types
        return self

    def instruction(self, instruction_type: str, instruction: str) -> 'AgentBuilder':
        """Add custom instruction."""
        self.config.custom_instructions[instruction_type] = instruction
        return self

    def metadata(self, key: str, value: Any) -> 'AgentBuilder':
        """Add metadata."""
        self.config.metadata[key] = value
        return self

    def from_template(self, template_name: str) -> 'AgentBuilder':
        """Create agent from template."""
        from .templates import AgentTemplates
        from dataclasses import replace
        template = AgentTemplates.get_template(template_name)
        if template:
            self.config = replace(template)
        return self

    def from_file(self, file_path: str) -> 'AgentBuilder':
        """Load agent configuration from file."""
        with open(file_path, 'r') as f:
            if file_path.endswith('.yaml') or file_path.endswith('.yml'):
                config_dict = yaml.safe_load(f)
            else:
                config_dict = json.load(f)

        self.config.name = config_dict.get('name', '')
        self.config.description = config_dict.get('description', '')
        self.config.system_prompt = config_dict.get('system_prompt', '')
        self.config.temperature = config_dict.get('temperature', 0.7)
        self.config.max_tokens = config_dict.get('max_tokens', 2000)
        self.config.context_length = config_dict.get('context_length', 4096)
        self.config.file_types = config_dict.get('file_types', [])
        self.config.custom_instructions = config_dict.get('custom_instructions', {})
        self.config.metadata = config_dict.get('metadata', {})

        # Handle personality
        personality_str = config_dict.get('personality', 'professional')
        try:
            self.config.personality = AgentPersonality(personality_str)
        except ValueError:
            self.config.personality = personality_str

        # Handle capabilities
        capabilities_list = config_dict.get('capabilities', [])
        self.config.capabilities = []
        for cap in capabilities_list:
            try:
                self.config.capabilities.append(AgentCapability(cap))
            except ValueError:
                self.logger.warning(f"Unknown capability: {cap}")

        return self

    def build(self, sdk_instance=None) -> CustomAgent:
        """Build the custom agent."""
        if not self.config.name:
            raise ValidationError("Agent name is required")

        if not self.config.description:
            raise ValidationError("Agent description is required")

        agent = CustomAgent(self.config, sdk_instance)
        agent.is_initialized = True
        return agent

    def validate(self) -> List[str]:
        """Validate the agent configuration."""
        errors = []

        if not self.config.name:
            errors.append("Agent name is required")

        if not self.config.description:
            errors.append("Agent description is required")

        if self.config.temperature < 0 or self.config.temperature > 2:
            errors.append("Temperature must be between 0 and 2")

        if self.config.max_tokens <= 0:
            errors.append("Max tokens must be positive")

        return errors

# Convenience function for quick agent creation
def create_agent(name: str, description: str, **kwargs) -> AgentBuilder:
    """Quick agent creation function."""
    builder = AgentBuilder().name(name).description(description)

    for key, value in kwargs.items():
        if hasattr(builder, key):
            getattr(builder, key)(value)

    return builder
