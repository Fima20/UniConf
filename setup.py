from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
    
setup(name="UniConf",
      version="0.1.3",
      description="A simple module allows you to quickly create and modify a configuration file. Based on 'configparser'.",
      author="Fima20",
      author_email="dmitriy2000ms@yandex.ru",
      long_description = long_description,
      long_description_content_type = 'text/markdown',
      packages=["uniconf"],
      install_requires=["configparser", "datetime"],
      zip_safe=False,)