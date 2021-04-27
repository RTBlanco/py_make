# from py_maker.config.json_writer import get_dir
from .author import get_dir

if not (get_dir() / "config.json").exists():
  get_dir().mkdir(parents=True)
  with (get_dir() / "config.json").open("w") as f:
    f.write('{"author": "Username", "author-email": "Username@email.com"}')

__version__ = "0.0.12" 
