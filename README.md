# roam-linker-bot
A simple Discord bot that looks for blockrefs enclosed in double-parentheses and converts them to Roam links

## Setup
* Set up a bot in the Discord admin panel
* Add your bot token and Roam graph name to a .env file in the same directory as bot.py for local testing,
or set environment variables directly with your provider. Keys:
    * DISCORD_TOKEN
    * ROAM_WORKSPACE

## Installation
This project uses [Poetry](https://python-poetry.org/) to manage dependencies. Once you have it installed, running `poetry install` in the project's root will install all dependencies and set up a virtual environment for testing.

## Limitations
This doesn't currently check for the existence of the blockref it is provided, nor is it able to resolve pagelinks.
