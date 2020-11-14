import setuptools
import py_make

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="py_make",
    version=py_make.__version__,
    author="RTBlanco",
    author_email="ronnytoribio1@hotmail.com",
    description="TODO:A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/RTBlanco/py_make",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)