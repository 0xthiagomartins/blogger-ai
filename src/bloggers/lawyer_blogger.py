from .base_blogger import BaseBlogger
from config.lawyer_config import lawyer_config
from langchain.prompts import PromptTemplate


class LawyerBlogger(BaseBlogger):
    def generate_blog_content(self) -> str:
        prompt = PromptTemplate(
            input_variables=[
                "business_name",
                "scope",
                "services",
                "target_clients",
                "blog_topic",
                "blog_length",
                "references",
            ],
            template=(
                "You are a professional content writer for {business_name}. "
                "The firm specializes in {scope}. They offer services such as {services}. "
                "Their target clients are {target_clients}. "
                "{base_template} "
                "{reference_section}"
                "Write a blog post titled '{blog_topic}' with a length of {blog_length}."
            ),
        )

        reference_section = ""
        if self.references:
            reference_section = (
                "Use the following references to inform your writing:\n"
                + "\n".join(self.references)
            )

        formatted_prompt = prompt.format(
            business_name=self.config.business_name,
            scope=self.config.scope,
            services=", ".join(self.config.services),
            target_clients=", ".join(self.config.target_clients),
            blog_topic=self.config.blog_topic,
            blog_length=self.config.blog_length,
            base_template=self.base_template,
            reference_section=reference_section,
        )

        response = self.llm.generate_content(formatted_prompt)
        markdown_content = f"# {self.config.blog_topic}\n\n{response}"
        return markdown_content
