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
    model="gemini-1.5-flash",
    references=[
        "https://www.nordinvestimentos.com.br/blog/recuperacao-judicial/",
        "https://portal.pucrs.br/blog/recuperacao-judicial/",
        "https://riconnect.rico.com.vc/blog/recuperacao-judicial/",
    ],
)
