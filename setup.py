import os

from setuptools import setup

description = "Version-bump your software with a single command!"

# Import the README and use it as the long-description.
# This requires 'README.md' to be present in MANIFEST.in.
here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = "\n" + f.read()

setup(
    name="bump2version",
    version="1.0.3",
    url="https://github.com/felipemlemos/bump2version",
    author="Felipe Lemos",
    author_email="christianverkerk@ymail.com",
    license="MIT",
    packages=["bumpversion"],
    description=description,
    long_description=long_description,
    long_description_content_type="text/markdown",
    entry_points={
        "console_scripts": [
            "bumpversion = bumpversion.cli:main",
            "bump2version = bumpversion.cli:main",
        ]
    },
    python_requires=">=3.7",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: Implementation :: PyPy",
    ],
    extras_require={
        "test": [
            "testfixtures>=1.2.0",
            "pytest>=3.4.0",
        ],
    },
)
