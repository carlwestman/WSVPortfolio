from setuptools import setup, find_packages

setup(
    name="WSVPortfolio",
    version="0.1.0",
    description="A Python package for portfolio management.",
    author="Your Name",
    author_email="your.email@example.com",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.8",
)
