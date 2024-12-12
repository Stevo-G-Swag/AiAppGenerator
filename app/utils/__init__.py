# Initialize utils package
from .openai_client import get_completion
from .code_validator import validate_syntax, validate_style

__all__ = ['get_completion', 'validate_syntax', 'validate_style']
