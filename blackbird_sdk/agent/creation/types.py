"""Shared types for agent creation system."""

from enum import Enum
from dataclasses import dataclass, field
from typing import Dict, List, Any, Optional, Callable, Union

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
