import pytest
from config.lawyer_config import lawyer_config
from bloggers.lawyer_blogger import LawyerBlogger


class MockLLM:
    def generate_content(self, prompt):
        return "This is a mock blog content."


def test_generate_blog_content():
    mock_llm = MockLLM()
    blogger = LawyerBlogger(config=lawyer_config, llm=mock_llm)
    content = blogger.generate_blog_content()
    assert content.startswith("# Understanding Corporate Law: A Comprehensive Guide")
    assert "This is a mock blog content." in content
