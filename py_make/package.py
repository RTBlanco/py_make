import os
from datetime import datetime 

project_name = input("name of project: ")
author = input("Auther: ")
version = input("Version: ")

os.makedirs(f"{project_name}/tests")
os.mkdir(f"{project_name}/{project_name}")


setup_file = open(f"{project_name}/setup.py","w")
setup_file.write(
f"""import setuptools

with open("README.md", "r") as fh:
  long_description = fh.read()

setuptools.setup(
  name="{project_name}", # Replace with your own username
  version="{version}",
  author="{author}",
  author_email="TODO:author@example.com",
  description="TODO:A small example package",
  long_description=long_description,
  long_description_content_type="text/markdown",
  url="https://github.com/pypa/sampleproject",
  packages=setuptools.find_packages(),
  classifiers=[
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
  ],
  python_requires='>=3.6',    
)"""
)
setup_file.close()


license_file = open(f"{project_name}/LICENSE", "w")
license_file.write(
f"""Copyright (c) {datetime.now().year} {author}

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE."""
)
license_file.close()

readme_file = open(f"{project_name}/README.md", "w")
readme_file.write(
f"""# {project_name.capitalize()}

:TODO  write a description


## Installation

    $ pip isntall {project_name}

## Usage
TODO: write quick tutorial 


This is a simple example package. You can use
[Github-flavored Markdown](https://guides.github.com/features/mastering-markdown/)
to write your content."""
)
readme_file.close

init_file = open(f"{project_name}/{project_name}/__init__.py", "w")
init_file.write(f"""__version__ = "{version}" """)
init_file.close()