from dataclasses import dataclass, field
from typing import List, Optional
from langchain_core.runnables import Runnable


@dataclass
class BaseConfig:
    business_name: str
    scope: str
    services: List[str]
    target_clients: List[str]
    blog_topic: str
    blog_length: str
    model: str
    references: Optional[List[str]] = field(default=None)
