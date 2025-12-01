from typing import Any, Dict, Callable, Optional

class TaskManagerBase:
    def __init__(self):
        self._tools: Dict[str, Callable[..., Any]] = {}

    def register(self, name: str, fn: Callable[..., Any]):
        self._tools[name] = fn

    def get(self, name: str) -> Optional[Callable[..., Any]]:
        return self._tools.get(name)

    def list_tools(self):
        return list(self._tools.keys())
