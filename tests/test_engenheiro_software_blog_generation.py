import pytest
from config.engenheiro_software_config import engenheiro_software_config
from bloggers.engenheiro_software_blogger import EngenheiroSoftwareBlogger
from rich import print


def test_generate_blog_content_with_references():
    blogger = EngenheiroSoftwareBlogger(config=engenheiro_software_config)
    content = blogger.generate_blog_content()
    print(content)
    assert isinstance(content, str), "Error on return type"


def test_generate_blog_content_without_references():
    no_ref_config = engenheiro_software_config
    no_ref_config.references = None
    blogger = EngenheiroSoftwareBlogger(config=no_ref_config)
    content = blogger.generate_blog_content()
    print(content)
    assert isinstance(content, str), "Error on return type"
