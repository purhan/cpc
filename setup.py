import setuptools


def get_install_requires():
    requirements = []
    for line in open("requirements.txt").readlines():
        if (
            line.startswith("#")
            or line == ""
            or line.startswith("http")
            or line.startswith("git")
        ):
            continue
        requirements.append(line)
    return requirements


setuptools.setup(
    name="cpc",
    version="0.1.0",
    author="Purhan Kaushik",
    author_email="purhan01@gmail.com",
    description="A CLI for competitive programmers",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/purhan/cpc",
    packages=setuptools.find_packages(),
    install_requires=get_install_requires(),
    python_requires=">=3.6",
    entry_points={"console_scripts": ["cpc = src.main:main"]},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
