from abc import ABC, abstractmethod
from config.base_config import BaseConfig
from typing import Optional  # Imported Optional


class BaseBlogger(ABC):
    def __init__(self, config: BaseConfig, llm):
        self.config = config
        self.llm = llm
        self.base_template = "Provide a well-structured and engaging blog post."
        self.references = config.references  # {{ edit_1 }} Initialize references

    @abstractmethod
    def generate_blog_content(self) -> str:
        pass
