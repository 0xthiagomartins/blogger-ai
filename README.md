# Blogger AI

![Blogger AI Logo](https://via.placeholder.com/150)

## Table of Contents

- [Blogger AI](#blogger-ai)
  - [Table of Contents](#table-of-contents)
  - [Overview](#overview)
    - [Key Highlights](#key-highlights)
  - [Features](#features)
  - [Architecture](#architecture)
  - [Installation](#installation)
    - [Prerequisites](#prerequisites)
    - [Steps](#steps)
  - [Configuration](#configuration)
    - [Adding a New Business Configuration](#adding-a-new-business-configuration)
  - [Usage](#usage)

## Overview

**Blogger AI** is a Python-based application designed to automatically generate tailored blog content for multiple businesses using **LangChain** and various language models from different providers. Whether you're a law firm, restaurant, tech startup, or any other type of business, Blogger AI can create high-quality, relevant blog posts in Markdown format to enhance your online presence and engage your audience.

### Key Highlights

- **Multi-Business Support:** Configure and generate blog content for various industries with ease.
- **Customizable Configurations:** Define business-specific scopes, services, target clients, and blog topics.
- **Multi-Agent Architecture:** Utilize a system of agents to gather requirements, create content, and validate quality.
- **LLM-Agnostic Design:** Support multiple language models from various providers, allowing flexibility and scalability.
- **Markdown Output:** Automatically generate Markdown files ready for integration into your blogging platform.
- **Scalable Architecture:** Easily extend the application to support new business types with minimal effort.
- **Testing with Pytest:** Ensure reliability and maintainability through comprehensive testing.

## Features

- **Configurable for Multiple Businesses:**
  - Define unique configurations for each business, including scope, services, and target clients.
  
- **Automated Content Generation:**
  - Leverage LangChain and multiple language models to produce high-quality blog posts based on provided configurations.
  
- **Multi-Agent System:**
  - **Requirement Agent:** Gathers and processes the requirements for the blog post.
  - **Content Creation Agent:** Generates the blog content based on the requirements.
  - **Quality Validation Agent:** Validates the generated content for quality and adherence to best practices. If the content does not meet the standards, it is sent back to the Content Creation Agent for refinement.
  
- **Markdown File Creation:**
  - Generate well-structured Markdown files suitable for various blogging platforms.
  
- **Extensible Design:**
  - Add support for new business types by creating corresponding configuration and blogger classes.
  
- **LLM-Agnostic Implementation:**
  - Integrate and switch between multiple language models from different providers seamlessly.
  
- **Environment Variable Management:**
  - Securely manage API keys and sensitive information through environment variables stored in separate `.env` files.
  
- **Testing with Pytest:**
  - Implement automated tests to ensure the reliability and correctness of the application.

## Architecture

Blogger AI follows a modular and multi-agent architecture to ensure scalability, flexibility, and maintainability. The primary components include:

1. **Configuration Management:**
   - Defines business-specific settings and parameters.
   - Utilizes multiple `.env` files (e.g., `.prod.env`, `.test.env`) stored in the `resources/` directory.
   - Uses `load_config` to dynamically load environment variables based on the environment.

2. **Multi-Agent System:**
   - **Requirement Agent:** Collects and structures the requirements for the blog post.
   - **Content Creation Agent:** Generates the blog content using the specified language model.
   - **Quality Validation Agent:** Reviews the content for quality, clarity, and adherence to best practices. If the content is insufficient, it loops back to the Content Creation Agent for improvement.

3. **Content Generation:**
   - Utilizes LangChain to interface with various language models from different providers.
   - Employs a base template to ensure consistency and highlight best practices in blog writing.

4. **Markdown Generation:**
   - Formats the validated content into Markdown files for easy integration into blogging platforms.

5. **Output Management:**
   - Saves the generated Markdown files to the `outputs/` directory for easy access and deployment.

6. **Testing:**
   - Implements automated tests using Pytest to validate functionality and ensure quality.

blogger-ai/ 
├── src/
│ ├── config/ 
│ │ ├── __init__.py 
│ │ ├── base_config.py 
│ │ ├── lawyer_config.py 
│ │ └── ... (other business configs) 
│ ├── bloggers/ 
│ │ ├── __init__.py 
│ │ ├── base_blogger.py 
│ │ ├── lawyer_blogger.py 
│ │ └── ... (other business bloggers) 
├── resources/ 
│ ├── .env 
│ ├── .prod.env 
│ ├── .test.env 
│ └── ... (other environment files) 
├── outputs/ 
│ └── ... (generated markdown files) 
├── agents/ 
│ ├── __init__.py 
│ ├── requirement_agent.py 
│ ├── content_agent.py 
│ ├── validation_agent.py 
│ └── ... (other agents) 
├── tests/ 
│ ├── conftest.py 
│ ├── test_agents.py 
│ ├── test_blogger.py 
│ └── ... (other test files) 
├── main.py 
├── requirements.txt 
├── pytest.ini 
└── README.md


## Installation

### Prerequisites

- **Python 3.11+**: Ensure you have Python installed. You can download it from [Python's official website](https://www.python.org/downloads/).
- **API Keys for Language Models**: Obtain API keys from language model providers such as [OpenAI](https://openai.com/api/), [Anthropic](https://www.anthropic.com/), etc., depending on the models you intend to use.

### Steps

1. **Clone the Repository**

```bash
git clone https://github.com/yourusername/Blogger AI.git
cd Blogger AI
```

2. **Create a Virtual Environment**

It's recommended to use a virtual environment to manage dependencies.

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install Dependencies**

```bash
pip install -r requirements.txt
```

4. **Set Up Environment Variables**

Create a .env file in the root directory and add your OpenAI API key:

```bash
OPENAI_API_KEY=your-openai-api-key
```

Alternatively, you can export the environment variable directly:

```bash
export OPENAI_API_KEY="your-openai-api-key"
```

## Configuration

Blogger AI uses configuration files to define settings for each supported business. These configurations include details like business name, scope, services, target clients, blog topics, and desired blog length.

### Adding a New Business Configuration

1. **Create a Configuration File**

Navigate to the config/ directory and create a new Python file, e.g., restaurant_config.py.

```bash
from .base_config import BaseConfig

restaurant_config = BaseConfig(
    business_name="Gourmet Delight",
    scope="Fine Dining, Catering Services",
    services=[
        "Gourmet Meals",
        "Event Catering",
        "Wine Pairing Consultations",
        "Private Dining Experiences"
    ],
    target_clients=[
        "Food Enthusiasts",
        "Corporate Clients",
        "Event Planners"
    ],
    blog_topic="Top 10 Gourmet Dishes to Impress Your Guests",
    blog_length="1200 words"
)
```

2. **Create a Corresponding Blogger Class**

In the `bloggers/` directory, create a new Python file, e.g., `restaurant_blogger.py`, extending the BaseBlogger class.

```bash
from .base_blogger import BaseBlogger
from config.restaurant_config import restaurant_config
from langchain.prompts import PromptTemplate

class RestaurantBlogger(BaseBlogger):
    def generate_blog_content(self) -> str:
        prompt = PromptTemplate(
            input_variables=["business_name", "scope", "services", "target_clients", "blog_topic", "blog_length"],
            template=(
                "You are a professional content writer for {business_name}. "
                "The restaurant specializes in {scope}. They offer services such as {services}. "
                "Their target clients are {target_clients}. "
                "{base_template} "
                "Write a blog post titled '{blog_topic}' with a length of {blog_length}."
            )
        )

        formatted_prompt = prompt.format(
            business_name=self.config.business_name,
            scope=self.config.scope,
            services=", ".join(self.config.services),
            target_clients=", ".join(self.config.target_clients),
            blog_topic=self.config.blog_topic,
            blog_length=self.config.blog_length,
            base_template=self.base_template
        )

        response = self.llm.generate_content(formatted_prompt)
        markdown_content = f"# {self.config.blog_topic}\n\n{response}"
        return markdown_content
```

## Usage

To generate a blog post for a specific business, follow these steps:

1. **Ensure All Configurations Are Set**

Make sure you have created the necessary configuration and blogger classes for the business.

2. **Run the Main Application**

Execute the main.py script to generate the blog posts.

```bash
python main.py
```

3. **Access the Generated Markdown Files**

The blog posts will be saved in the `outputs/` directory as Markdown files, ready for integration into your blogging platform.