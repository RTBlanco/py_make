import setuptools
import py_maker

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="py_maker",
    version=py_maker.__version__,
    author="RTBlanco",
    author_email="ronnytoribio1@hotmail.com",
    description="Quick way to get started on a package!",
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
    include_package_data=True,
    entry_points={
        "console_scripts": ["py_maker=py_maker.__main__:main"]
    },
)