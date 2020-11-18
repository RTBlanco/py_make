import json, os, sys
from pathlib import Path


def get_dir():
  home = os.path.realpath(os.path.expanduser("~"))
  
  if sys.platform == 'darwin':
    d = Path(home, 'Library')
  elif os.name == 'nt':
    appdata = os.environ.get('APPDATA', None)
    if appdata:
      d = Path(appdata)
    else:
      d = Path(home, 'AppData', 'Roaming')
  else:
    # Linux, non-OS X Unix, AIX, etc.
    xdg = os.environ.get("XDG_DATA_HOME", None)
    d = Path(xdg) if xdg else Path(home, '.local/share')

  return d / 'py_maker'




class Author:
  def __init__(self):
    with (get_dir() / "config.json").open("r") as f:
      config_data = json.load(f)
    self.name = config_data["author"]
    self.email = config_data["author-email"]
  

  def update(self):  
    with (get_dir() / "config.json").open("r") as f:
      config_data = json.load(f)        

    self.name = input(f'[{self.name}]:  ')
    self.email = input(f'[{self.email}]:  ')

    config_data["author"] = self.name if self.name else config_data["author"]
    config_data["author-email"] = self.email if self.email else config_data["author-email"]

    os.remove(get_dir() / "config.json") 

    with (get_dir() / "config.json").open("w") as f:
      json.dump(config_data, f, indent=4)
