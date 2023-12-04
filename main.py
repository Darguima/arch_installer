from merge_json import merge_json
from os import listdir
from os.path import isfile, join

def get_env():
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
    exit()
  else:
    return config_files[int(selected_env) - 1]

def main():
  env = get_env()
  merge_json(env)
  print("\nConfiguration file generated successfully! Now run:")
  print("\n$ archinstall --config user_configuration.json")


if __name__ == "__main__":
  main()