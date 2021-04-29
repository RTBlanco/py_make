from datetime import datetime
from pkg_resources import resource_string as resource_bytes

class Files:
  def __init__(self, project, author):
    self.project = project
    self.author = author

  def setup(self):
    setup = resource_bytes(__name__, 'templates/setup_template.txt').decode("utf-8")
    with open(f"{self.project.name}/setup.py", "w") as f:
      f.write(setup.format(
        project_name = self.project.name,
        project = self.project,
        author = self.author.name,
        author_email = self.author.email,
      ))
    print(f"Created -> {self.project.name}/setup.py ")

  def license(self):
    license = resource_bytes(__name__, 'templates/license_template.txt').decode("utf-8")
    with open(f"{self.project.name}/LICENSE", "w") as f:
      f.write(license.format(date = datetime.now().year, author = self.author.name))
    print(f"Created -> {self.project.name}/LICENSE")

  def readme(self):
    readme = resource_bytes(__name__, 'templates/readme_template.txt').decode("utf-8")
    with open(f"{self.project.name}/README.md", "w") as f:
      f.write(readme.format(project_name = self.project.name))
    print(f"Created -> {self.project.name}/README.md")

  def init(self):
    with open(f"{self.project.name}/{self.project.name}/__init__.py", "w") as f:
      f.write(f'__version__ = "{self.project.version}"')
    print(f"Created -> {self.project.name}/{self.project.name}/__init__.py")