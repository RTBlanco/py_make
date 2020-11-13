import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="py_make",
    version="0.0.1",
    author="RTBlanco",
    author_email="TODO:author@example.com",
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