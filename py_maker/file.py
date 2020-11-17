import json
from datetime import datetime
from py_maker.make_package.package import Package 
from py_maker.config.json_writer import get_dir
from py_maker import Author
from pkg_resources import resource_string as resource_bytes

# TODO: create an author class 
with (get_dir() / "config.json").open('r',encoding='utf-8') as f:
  config_data = json.load(f)

author = config_data["author"]
author_email = config_data["author-email"]


# TODO: Write files here 
# make it so that the arugments are author and projects 
class Files:
  def __init__(self, project, author):
    self.project = project
    self.author = author

  def setup(self,):
    setup = resource_bytes(__name__, 'templates/setup_template.txt').decode("utf-8")
    with open(f"{self.project.name}/setup.py", "w") as f:
      f.write(setup.format(
        project_name = self.project.name,
        project = self.project,
        project_version = self.project.version,
        author = self.author.name,
        author_email = self.author.email,
      ))

  def license(self):
    license = resource_bytes(__name__, 'templates/license_template.txt').decode("utf-8")
    with open(f"{self.project.name}/LICENSE", "w") as f:
      f.write(license.format(date = datetime.now().year, author = self.author.name))


  def readme(self):
    readme = resource_bytes(__name__, 'templates/readme_template.txt').decode("utf-8")
    with open(f"{self.project.name}/README.md", "w") as f:
      f.write(readme.format(project_name = self.project.name))


  def init(self):
    with open(f"{self.project.name}/{self.project.name}/__init__.py") as f:
      f.write(self.project.version)