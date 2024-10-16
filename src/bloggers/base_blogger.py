from abc import ABC, abstractmethod
from config.base_config import BaseConfig


class BaseBlogger(ABC):
    def __init__(self, config: BaseConfig, llm):
        self.config = config
        self.llm = llm
        self.base_template = "Provide a well-structured and engaging blog post."

    @abstractmethod
    def generate_blog_content(self) -> str:
        pass
