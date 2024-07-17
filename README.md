# Arch Installer

On this repo are available the configurations files for my 2 Arch Linux setups, installed with `archinstall`.

This repository is a complement to my [dotfiles](https://github.com/darguima/dotfiles). So my Window Manager, the applications that I use and their configurations will not be installed now.

## Running the script

First ensure that you are connected to internet - you can read the official [documentation](https://wiki.archlinux.org/title/Installation_guide#Connect_to_the_internet).

Clone the repo. Usually you will also need install `git` on fresh machines:

```bash
$ pacman -Sy git
$ git clone https://github.com/Darguima/arch_installer
```

Start by giving a look at the `assets` folder, ~~editing the respective files to what best fit to you~~ but edit them will not take any effect, since due `archinstall` limitations, I'm downloading the files on the setup from the Github repository. (eg: you may want to adapt the `/etc/hosts` file)

Now generate the correct configuration with this helper:

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

Access my [dotfiles](https://github.com/darguima/dotfiles) and install the remaining configurations.
