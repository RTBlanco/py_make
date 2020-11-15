import json
from datetime import datetime 
from pkg_resources import resource_string as resource_bytes

config_file = resource_bytes('py_make.__main__', 'config/config.json').decode("utf-8")
config_dict = json.loads(config_file)

author = config_dict["author"]
author_email= config_dict["author-email"]

def setup_writer(project_name, version):
  return f"""
  import setuptools
  import py_make
  
  with open("README.md", "r") as fh:
    long_description = fh.read()

  setuptools.setup(
  name="{project_name}",
  version="{version}",
  author="{author}",
  author_email="{author_email}",
  description="TODO:A small example package",
  long_description=long_description,
  long_description_content_type="text/markdown",
  url="TODO: Enter URL",
  packages=setuptools.find_packages(),
  classifiers=[
      "Programming Language :: Python :: 3",
      "License :: OSI Approved :: MIT License",
      "Operating System :: OS Independent",
  ],
  python_requires='>=3.6',    
  )"""



def license_writer():
  return f"""Copyright (c) {datetime.now().year} {author}

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


def readme_writer(project_name):
  return f"""# {project_name.capitalize()}

:TODO  write a description


## Installation

    $ pip install {project_name}

## Usage
TODO: write quick tutorial 


This is a simple example package. You can use
[Github-flavored Markdown](https://guides.github.com/features/mastering-markdown/)
to write your content."""

def init_writer(version):
    return f"__version__ = {version}"