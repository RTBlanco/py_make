import json

with open('py_make/config/config.json','r') as config_file:
  config = json.load(config_file)
  author = config["author"]
  author_email= config["author-email"]
  
