from setuptools import setup, find_packages
from setuptools.config import read_configuration

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="image-processing-lucelia",
    version="0.0.1",
    author="Lucelia Mendes",
    author_email="lucmendess@hotmail.com",
    description="Passo a passo passado do projeto pela instrutora.",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url=" https://github.com/Lucmendess/projeto_dio",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)