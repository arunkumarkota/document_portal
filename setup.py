from setuptools import setup, find_packages

setup(
    name="document_portal",
    author="Your Name",
    author_email="your.email@example.com",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "fastapi",
        "uvicorn",
        "python-dotenv",
    ],
)