import json
from os import listdir
from os.path import isfile, join

def merge_dicts(*dicts):
    result = {}
    for d in dicts:
        result.update(d)
    return result

def merge_json(environment):
  config_base_file = open('config_base.json')
  config_base = json.load(config_base_file)
  config_base_file.close()

  config_env_file = open(f'config_{environment}.json')
  config_env = json.load(config_env_file)
  config_env_file.close()

  final_config = merge_dicts(config_base, config_env)
  json_config = json.dumps(final_config, indent=4)

  with open('user_configuration.json', 'w') as outfile:
    outfile.write(json_config)

if __name__ == '__main__':
  print("\nAvailable environments: \n")

  config_files = []
  for f in listdir("."):
     if isfile(join(".", f)) and f.startswith("config_") and f.endswith(".json") and f != "config_base.json":
      env = f.removeprefix("config_").removesuffix(".json")
      config_files.append(env)
      print(f"\t{len(config_files)}. {env}")

  selected_env = input("\nSelect an environment: ")

  if not selected_env.isnumeric() or int(selected_env) > len(config_files):
    print("Invalid option!")
  else:
    merge_json(config_files[int(selected_env) - 1])
    print("\nConfiguration file generated successfully!")
