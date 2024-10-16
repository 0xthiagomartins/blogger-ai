from dataclasses import dataclass
from typing import List


@dataclass
class BaseConfig:
    business_name: str
    scope: str
    services: List[str]
    target_clients: List[str]
    blog_topic: str
    blog_length: str
