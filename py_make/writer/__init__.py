import json

with open('config.json','r') as config_file:
  config = json.load(config_file)
  author = config["author"]
  author_email= config["author-email"]
  
