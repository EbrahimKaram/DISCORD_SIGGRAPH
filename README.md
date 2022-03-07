# About
A Discord bot to help with SIGRAPH 2021

The bot works by writing over certain coroutines and calls.


# Terms
## What is A guild
A guild is a server

This is referred to as a “server” in the official Discord UI.



# Restrictions
## Channel name
They can't have spaces. There is no obvious character limit but we will make them 20 characters long at max

The maximum number of categories for a server is 50 and the maximum number of channels in total is 500.

You can only have at max 50 channels per category


# Set Up the Virtual Environment
To create a virtual environment
`python3 -m venv .\bot-env`

Activate using the following
in CMD
`.\bot-env\Scripts\activate.bat`
In PowerShell
`.\bot-env\Scripts\activate.ps1`
then install the packages from requirements.txt as such (the below is for powershell)
`pip install -r .\requirements.txt`

## To get the Visual studio noticing your WorkSpace

Follow the directions on the link below
https://code.visualstudio.com/docs/python/environments#_select-and-activate-an-environment

and set the path to

`..\bot-env\Scripts\python.exe`

# Auth Key
I have my auth Keys stored in a `constants.py`
This is to keep them private and not have them publicly shown on the repo.
Please NOTE that `constants.py` is not stored on the git and is part of the `.gitignore` file.

In case sensitive data was added to repo, follow the instructions in the link below from GitHub
https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository


# EXTRA
Review progress via the Trello board
https://trello.com/b/Ss3DkzU8/discord

Documentation on Discord API (official)
https://github.com/discord/discord-api-docs

We use Discord py
https://discordpy.readthedocs.io/en/stable/
