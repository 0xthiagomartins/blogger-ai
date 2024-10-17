from .base_blogger import BaseBlogger
from src.config.engenheiro_software_config import engenheiro_software_config
from langchain.prompts import PromptTemplate
from langchain_core.runnables import Runnable
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts.base import BasePromptTemplate
from langchain_core.messages import AIMessage
from typing import Optional
from rich import print


class EngenheiroSoftwareBlogger(BaseBlogger):
    prompt: BasePromptTemplate = PromptTemplate(
        template=(
            "Você é um redator profissional para {business_name}. "
            "A empresa se especializa em {scope}. Eles oferecem serviços como {services}. "
            "Seus clientes-alvo são {target_clients}. "
            "{base_template} "
            "{reference_section}"
            "Escreva um artigo com o título '{blog_topic}' com uma extensão de {blog_length}."
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
                "Use as seguintes referências para informar sua escrita:\n"
                + "\n".join(self.references)
            )

        formatted_prompt = {
            "business_name": self.config.business_name,
            "scope": self.config.scope,
            "services": ", ".join(self.config.services),
            "target_clients": ", ".join(self.config.target_clients),
            "blog_topic": self.config.blog_topic,
            "blog_length": self.config.blog_length,
            "base_template": self.base_template,
            "reference_section": reference_section,
        }

        chain = self.get_chain()
        ai_message: AIMessage = chain.invoke(formatted_prompt)
        content = ai_message.to_json().get("kwargs", {}).get("content", "")
        markdown_content = f"# {self.config.blog_topic}\n\n{content}"
        return markdown_content
