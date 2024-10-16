import pytest
from config.lawyer_config import lawyer_config
from bloggers.lawyer_blogger import LawyerBlogger


class MockLLM:
    def generate_content(self, prompt):
        assert (
            "Use the following references" in prompt
        )  # {{ edit_1 }} Ensure references are included
        return "This is a mock blog content based on references."


def test_generate_blog_content_with_references():
    mock_llm = MockLLM()
    blogger = LawyerBlogger(config=lawyer_config, llm=mock_llm)
    content = blogger.generate_blog_content()
    assert content.startswith("# Understanding Corporate Law: A Comprehensive Guide")
    assert "This is a mock blog content based on references." in content


def test_generate_blog_content_without_references():
    no_ref_config = lawyer_config
    no_ref_config.references = None  # {{ edit_2 }} Remove references
    mock_llm = MockLLM()
    blogger = LawyerBlogger(config=no_ref_config, llm=mock_llm)
    content = blogger.generate_blog_content()
    assert content.startswith("# Understanding Corporate Law: A Comprehensive Guide")
    assert (
        "This is a mock blog content based on references." in content
    )  # Depending on implementation
