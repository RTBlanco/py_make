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

def update_config():
  data = get_dir()

  
  with (data / "config.json").open("r") as f:
    config_data = json.load(f)        

  author = input(f'[{config_data["author"]}]:  ')
  author_email = input(f'[{config_data["author-email"]}]:  ')

  config_data["author"] = author if author else config_data["author"]
  config_data["author-email"] = author_email if author_email else config_data["author-email"]

  os.remove(data / "config.json")

  with (data / "config.json").open("w") as f:
    json.dump(config_data, f, indent=4)

  
  data.mkdir(parents=True)
  with (data / "config.json").open("w") as f:
    f.write('{"author": "Username", "author-email": "Username@email.com"}')