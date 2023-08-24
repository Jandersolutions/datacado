from setuptools import setup, find_packages

setup(
    name="datacado",
    version="0.1",
    description="Um pacote para gerar dados fictícios de vendas",
    packages=find_packages(),
    install_requires=[
        "faker",
    ],
) 
