import os
from py_maker.file import Files 


class Project:
  def __init__(self, name, author, version):
    self.name = name
    self.version = version if version == None else "0.0.1"
    self.author = author


class Package(Project):

  def make(self, test = False):
    pkg = Files(self, self.author)
    os.makedirs(f"{self.name}/tests") if test else os.makedirs(f"{self.name}")
    os.mkdir(f"{self.name}/{self.name}")

    pkg.setup
    pkg.license
    pkg.readme
    pkg.init