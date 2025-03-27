from setuptools import setup, find_packages

setup(
    name='MDP_assess',  # Package name
    version='0.1',
    packages=find_packages(),  # Automatically find packages in the project
    install_requires=[  # External dependencies (if any)
        # 'numpy', 'pandas'  # Example, if your project needs these
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
