# Discord Moderation Bot

Python + discord.py bot with automated moderation:

- **Spam detection**: message flooding, repeated messages, mass mentions
- **Keyword filtering**: configurable banned-word list (whole-word, case-insensitive)
- **Auto-mute**: strikes accumulate; at the limit the member is timed out
- **Mod logs**: every action is posted to a `#mod-logs` channel
- **Slash commands**: `/warnings`, `/clearwarnings`, `/mute`, `/unmute`, `/addword`, `/removeword`

## Setup
1. Create an app at https://discord.com/developers/applications, add a Bot, copy the token.
2. In the Bot tab enable **Message Content Intent** and **Server Members Intent**.
3. Invite with scopes `bot` + `applications.commands` and permissions:
   Manage Messages, Moderate Members, Send Messages, Embed Links, View Channels.
4. `python -m venv venv && source venv/bin/activate` (Windows: `venv\Scripts\activate`)
5. `pip install -r requirements.txt`
6. `cp .env.example .env` and paste your token.
7. Create a `#mod-logs` channel and put the bot's role **above** regular member roles.
8. `python main.py`

## Tuning
Edit `config.json` (spam limits, strikes before mute, mute length, banned words).
