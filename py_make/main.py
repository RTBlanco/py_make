import sys
from .writer.json_writer import update_config 

x = sys.argv[1]

if x == "init":
    update_config()
    print(x)
else:
    print("nothing happend")