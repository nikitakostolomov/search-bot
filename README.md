# search-bot
## Summary
This app is used for searching information for user via telegram bot and Google.
As interface for Telegram Bot API `python-telegram-bot` lib is used and
for searching Google `googlesearch-python` lib is used.
## Prerequisites
1. Install Telegram or use web version
2. Install poetry
3. Install Python 3.10
## Installation
1. Clone repo
`~$ git clone https://github.com/nikitakostolomov/search-bot.git`
2. Go to `search-bot` dir
`~$ cd search-bot`
3. Create virtual environment via poetry
`~/search-bot$ poetry env use <your python version>`
4. Activate virtual environment
`~/search-bot$ poetry shell`
5. Run command to install dependencies
`~/search-bot$ poetry install`
## Usage
1. Ask me for `bot_token` and insert it in `BOT_TOKEN` var inside `main.py`
2. Run main file
`~/search-bot$ python main`
2. Open telegram and search for bot with name `@browser_search_bot`
## Commands
1. `/start` command will greet you
2. `/search <text for search>` command will search Google for you and provide search result
in next message
E.g: `/search Python Programming` command will return first result in Google search with
information about Python Programming.
Result will contain title of first link and link itself.
Note that, if you make too many requests, Google will respond with 429 status code,
which means, that requests from your IP address will be temporarily blocked.
