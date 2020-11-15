import json, os



def update_config():
  config = os.path.join("py_make","config.json")

  with open(config, "r") as f:
    config_data = json.load(f)

    author = input(f'[{config_data["author"]}]:  ')
    author_email = input(f'[{config_data["author-email"]}]:  ')

    config_data["author"] = author if author else config_data["author"]

    config_data["author-email"] = author_email if author_email else config_data["author-email"]

    os.remove(config)

  with open(config, "w") as f:
    json.dump(config_data, f, indent=4)
