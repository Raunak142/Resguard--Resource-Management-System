from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.read().splitlines()

setup(
    name="resguard",
    version="1.0.0",
    author="Raunak Godiyal",
    author_email="raunakgodiyal142@gmail.com",
    description="Dynamic Resource Management System using Banker's Algorithm",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Raunak142/Resguard--Resource-Management-System",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "resguard=main:main",
        ],
    },
)
