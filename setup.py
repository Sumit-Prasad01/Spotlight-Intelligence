from setuptools import setup,find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="Spotlight Intelligence-Celebrity Detctor And QA System",
    version="0.1",
    author="Sumit Prasad",
    packages=find_packages(),
    install_requires = requirements,
)