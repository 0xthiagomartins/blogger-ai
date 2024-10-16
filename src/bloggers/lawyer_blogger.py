from .base_blogger import BaseBlogger
from src.config.lawyer_config import lawyer_config
from langchain.prompts import PromptTemplate
from langchain_core.runnables import Runnable
from langchain_core.prompts import BasePromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import AIMessage, AIMessageChunk, BaseMessage
from rich import print


class LawyerBlogger(BaseBlogger):
    prompt: BasePromptTemplate = PromptTemplate(
        template=(
            "You are a professional content writer for {business_name}. "
            "The firm specializes in {scope}. They offer services such as {services}. "
            "Their target clients are {target_clients}. "
            "{base_template} "
            "{reference_section}"
            "Write a blog post titled '{blog_topic}' with a length of {blog_length}."
        ),
        input_variables=[
            "business_name",
            "scope",
            "services",
            "target_clients",
            "blog_topic",
            "blog_length",
            "reference_section",
        ],
    )

    def get_chain(self) -> Runnable:
        return self.prompt | ChatGoogleGenerativeAI(model=self.config.model)

    def generate_blog_content(self) -> str:
        reference_section = ""
        if self.references:
            reference_section = (
                "Use the following references to inform your writing:\n"
                + "\n".join(self.references)
            )

        formatted_prompt = dict(
            business_name=self.config.business_name,
            scope=self.config.scope,
            services=", ".join(self.config.services),
            target_clients=", ".join(self.config.target_clients),
            blog_topic=self.config.blog_topic,
            blog_length=self.config.blog_length,
            base_template=self.base_template,
            reference_section=reference_section,
        )
        chain = self.get_chain()
        ai_message: AIMessage = chain.invoke(formatted_prompt)
        markdown_content = f"# {self.config.blog_topic}\n\n{ai_message.to_json()}"
        return markdown_content
