class ConfigError(RuntimeError):
    """Raised when application configuration is missing or invalid."""


class ApplicationError(RuntimeError):
    """Base class for recoverable application errors."""
