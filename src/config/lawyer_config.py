from .base_config import BaseConfig

lawyer_config = BaseConfig(
    business_name="Prestige Law Firm",
    scope="Corporate Law, Intellectual Property",
    services=[
        "Contract Drafting",
        "Trademark Registration",
        "Legal Consultation",
        "Litigation Services",
    ],
    target_clients=["Startups", "Established Corporations", "Entrepreneurs"],
    blog_topic="Understanding Corporate Law: A Comprehensive Guide",
    blog_length="1500 words",
    references=[  # {{ edit_1 }} Added references
        "https://www.example.com/source1",
        "https://www.example.com/source2",
        "https://www.example.com/source3",
    ],
)
