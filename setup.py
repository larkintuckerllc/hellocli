from setuptools import setup, find_packages

install_requires = []
with open('requirements.txt') as f:
    for line in f:
        line = line.strip()
        install_requires.append(line)

setup(
    entry_points={
        "console_scripts": [
            "hellocli=hellocli.main:cli"
        ],
    },
    install_requires=install_requires,
    name='hellocli',
    packages=find_packages('hellocli'),
    version='0.1.0',
)
