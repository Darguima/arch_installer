
import json

def merge_dicts(*dicts):
    result = {}

    for d in dicts:

      for key, value in d.items():
        if key in result and isinstance(result[key], dict) and isinstance(value, dict):
            result[key] = merge_dicts(result[key], value)
          
        elif key in result and isinstance(result[key], list) and isinstance(value, list):
            result[key] = result[key] + value
          
        else:
            result[key] = value

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