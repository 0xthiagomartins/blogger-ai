from .base_config import BaseConfig
from typing import List, Optional

engenheiro_software_config = BaseConfig(
    business_name="Tech Innovators",
    scope="Desenvolvimento de Software, Engenharia de Sistemas",
    services=[
        "Desenvolvimento de Aplicações Web",
        "Desenvolvimento de Aplicações Decentralizadas",
        "Consultoria em Engenharia de Software",
        "Integração de Sistemas",
        "Monitoramento de Aplicações",
    ],
    target_clients=[
        "Startups",
        "Empresas de Tecnologia",
        "Desenvolvedores Independentes",
    ],
    blog_topic="As Melhores Práticas em Engenharia de Software para 2024",
    blog_length="1500 palavras",
    model="gemini-1.5-flash",
    references=[],
)
