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
    
    print(self.name)
    self.__iter_if_exist()

    os.makedirs(f"{self.name}/{self.name}/tests") if test else os.makedirs(f"{self.name}/{self.name}")

    pkg.init()
    pkg.license()
    pkg.readme()
    pkg.setup()

  def __iter_if_exist(self):
    while os.path.exists(self.name):
      try:
        self.name = self.name.replace(self.name[-1], str(int(self.name[-1]) + 1 )) 
      except ValueError:
        self.name += "1"
