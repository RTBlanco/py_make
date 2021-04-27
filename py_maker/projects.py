import os
from py_maker.file import Files 


class Project:
  def __init__(self, name, author, version):
    self.name = name
    self.version = "0.0.1" if version == None else version
    self.author = author


class Package(Project):

  def make(self, test = False):
    pkg = Files(self, self.author)

    os.makedirs(f"{self.name}/{self.name}/tests") if test else os.mkdir(f"{self.name}")

    pkg.init()
    pkg.license()
    pkg.readme()
    pkg.setup()