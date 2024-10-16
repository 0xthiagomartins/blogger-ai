import os
from config.lawyer_config import lawyer_config
from bloggers.lawyer_blogger import LawyerBlogger
from langchain.llms import OpenAI


def load_llm():
    api_key = os.getenv("OPENAI_API_KEY")
    return OpenAI(api_key=api_key)


def generate_blog():
    llm = load_llm()
    blogger = LawyerBlogger(config=lawyer_config, llm=llm)
    content = blogger.generate_blog_content()

    output_path = os.path.join("outputs", "lawyer_blog.md")
    with open(output_path, "w") as f:
        f.write(content)
    print(f"Blog post generated at {output_path}")

    # Optionally handle dynamic references here if needed


if __name__ == "__main__":
    generate_blog()
