"""Configuration management for Watson project."""
import os
from typing import Optional
from dotenv import load_dotenv

load_dotenv()


class Config:
    """Configuration class for Watson project."""
    
    # API Keys
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")
    OPENPIPE_API_KEY: str = os.getenv("OPENPIPE_API_KEY", "")
    OPENPIPE_BASE_URL: str = os.getenv(
        "OPENPIPE_BASE_URL", 
        "https://app.openpipe.ai/api/v1"
    )
    
    # Model configurations
    AGENT_MODEL: str = os.getenv("AGENT_MODEL", "gpt-4")
    ENVIRONMENT_MODEL: str = os.getenv("ENVIRONMENT_MODEL", "gpt-4")
    REWARD_MODEL: str = os.getenv("REWARD_MODEL", "gpt-4")
    
    # OpenPipe tags for tracking different components
    AGENT_TAG: str = "watson-agent"
    ENVIRONMENT_TAG: str = "watson-environment"
    REWARD_TAG: str = "watson-reward"
    
    @classmethod
    def validate(cls) -> None:
        """Validate that required configuration is present."""
        if not cls.OPENAI_API_KEY:
            raise ValueError("OPENAI_API_KEY is required")
        if not cls.OPENPIPE_API_KEY:
            raise ValueError("OPENPIPE_API_KEY is required")

