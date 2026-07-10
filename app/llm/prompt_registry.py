from hashlib import sha256

from app.core.config import PromptsConfig


class PromptRecord:
    def __init__(self, name: str, version: str, template: str) -> None:
        self.name = name
        self.version = version
        self.template = template
        self.prompt_hash = sha256(template.encode("utf-8")).hexdigest()


class PromptRegistry:
    def __init__(self, prompts: PromptsConfig) -> None:
        self._records = {
            name: PromptRecord(name=name, version=value.version, template=value.template)
            for name, value in prompts
        }

    def get(self, name: str) -> PromptRecord:
        try:
            return self._records[name]
        except KeyError as exc:
            raise KeyError(f"Unknown prompt: {name}") from exc
