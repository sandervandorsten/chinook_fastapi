#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open("README.md") as readme_file:
    readme = readme_file.read()

requirements = [
    "fastapi>=0.58.0",
    "uvicorn>=0.11.5",
    "python-dotenv>=0.14.0"
]

setup_requirements = [
    "pytest-runner",
]

test_requirements = [
    "pytest>=3",
]

setup(
    author="Sander van Dorsten",
    author_email="sandervandorsten@gmail.com",
    python_requires=">=3.5",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    description="REST API built with FastAPI on top of chinook dataset.",
    install_requires=requirements,
    license="MIT license",
    long_description=readme,
    include_package_data=True,
    keywords="chinook_fastapi",
    name="chinook_fastapi",
    packages=find_packages(include=["chinook_fastapi", "chinook_fastapi.*"]),
    setup_requires=setup_requirements,
    test_suite="tests",
    tests_require=test_requirements,
    url="https://github.com/sandervandorsten/chinook_fastapi",
    version="0.1.0",
    zip_safe=False,
)
