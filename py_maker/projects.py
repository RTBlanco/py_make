import os
from py_maker.file import Files 


class Project:
  def __init__(self, name, version):
    self.name = name
    self.version = version


class Package(Project):
  def __init__(self, name, version, test = False):
    super().__init__(name, version)
    os.makedirs(f"{self.name}/tests") if test else os.makedirs(f"{self.name}")
    os.mkdir(f"{self.name}/{self.name}")
  
