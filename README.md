# Arch Installer

On this repo are available the configurations files for my 2 setups, alongside the Python script that I use to merge them.

## Running the script

After clone the repo to your clean setup, run the following command:

```bash
$ python main.py
```

After select the correct environment, the `user_configuration.json` file will be generated. Now run the `archinstall`:

```bash
$ archinstall --config user_configuration.json
```

Confirm the selected options on the TUI, correct the needed and install.
If everything goes right you should have a ready Arch setup.

## And now?

This repository is a complement to my [dotfiles](https://github.com/darguima/dotfiles). So my Window Manager and tools configurations are there.
