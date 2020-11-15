import os
from py_maker.writer.file_writer import setup_writer, license_writer, readme_writer, init_writer

def package(project_name, version):
  version = version if version != None else "0.0.1"

  os.makedirs(f"{project_name}/tests")
  os.mkdir(f"{project_name}/{project_name}")


  setup_file = open(f"{project_name}/setup.py","w")
  setup_file.write(setup_writer(project_name))
  setup_file.close()


  license_file = open(f"{project_name}/LICENSE", "w")
  license_file.write(license_writer())
  license_file.close()

  readme_file = open(f"{project_name}/README.md", "w")
  readme_file.write(readme_writer(project_name))
  readme_file.close

  init_file = open(f"{project_name}/{project_name}/__init__.py", "w")
  init_file.write(init_writer(version))
  init_file.close()