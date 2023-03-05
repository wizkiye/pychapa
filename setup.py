import re

import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("pychapa/__version__.py") as f:
    version = re.search('^__version__\s=\s"(.+)"$', f.read()).group(1)

with open("requirements.txt") as f:
    requirements = f.read().split("\n")

setuptools.setup(
    name="pychapa",
    version=version,
    author="Kidus (wizkiye)",
    author_email="wiziye@gmail.com",
    description="Python SDK for Chapa API https://developer.chapa.co",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/wizkiye/pychapa",
    packages=setuptools.find_packages(),
    project_urls={
        "Source": "https://github.com/wizkiye/chapa",
        "Bug Tracker": "https://github.com/chapimenge3/wizkiye/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.9",
    install_requires=requirements,
)
