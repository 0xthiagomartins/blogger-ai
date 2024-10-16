import pytest
from src.config.lawyer_config import lawyer_config
from src.bloggers.lawyer_blogger import LawyerBlogger


def test_generate_blog_content_with_references():
    blogger = LawyerBlogger(config=lawyer_config)
    content = blogger.generate_blog_content()
    print(content)
    assert isinstance(content, str)


def test_generate_blog_content_without_references():
    no_ref_config = lawyer_config
    no_ref_config.references = None
    blogger = LawyerBlogger(config=no_ref_config)
    content = blogger.generate_blog_content()
    print(content)
    assert isinstance(content, str)
