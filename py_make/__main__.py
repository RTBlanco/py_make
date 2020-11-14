import sys
from make_package.package import package 
from config.json_writer import update_config

param1 = sys.argv[1]

if len(sys.argv) >= 3:
  project_name_input = sys.argv[2] 
  version_input = sys.argv[3] if len(sys.argv) == 4 else None


if param1 == "init":
  update_config()
else:
  package(project_name_input, version_input)
    