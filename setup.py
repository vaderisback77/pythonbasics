from setuptools import setup, find_packages

setup(
    name="python_basics",
    version="1.0.1",
    author="Saurabh Saran",
    author_email="saurabh.saran@example.com",
    description="Python programmming basics",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/your_project_name",
    packages=find_packages(),
    install_requires=[
        "black",
        "pytest-mock",
        # Add other dependencies here
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",
)
