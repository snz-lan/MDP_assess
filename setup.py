from setuptools import setup, find_packages

setup(
    name='mdp_solver',
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "numpy",  # Add any dependencies here
    ],
    author="Shahnaz Abdul Hameed",
    author_email="shahnaz.abdulhameed2309@gmail.com",
    description="A Markov Decision Process solver using Value Iteration",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/snz-lan/MDP_assess",
    license="MIT",
    python_requires=">=3.7",
)
