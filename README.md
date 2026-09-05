#  Discord AI Bot (Cohere LLM Integration)

A simple Discord bot built with Python that uses the **Cohere API** to provide automated AI-generated responses to user queries directly inside Discord channels.

##  Features

-  **Interactive Commands**: Responds to `!ask` and `!ai` commands.
-  **AI-Powered Responses**: Generates concise answers using Cohere's language models.
-  **Error Handling**: Gracefully handles API errors, empty prompts, and unexpected runtime exceptions.
-  **Environment Variable Support**: Uses `python-dotenv` to safely isolate tokens and API keys.

---

## Tech Stack

- **Python 3.x**
- **discord.py** (Discord API Wrapper)
- **cohere** (Cohere API Client)
- **python-dotenv**

---

##  Setup & Installation

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/USERNAME/discord-ai-bot.git](https://github.com/USERNAME/discord-ai-bot.git)
   cd discord-ai-bot
2. Install:
pip install discord.py cohere python-dotenv

3.Create a .env file in the root directory:
DISCORD_TOKEN=your_discord_bot_token
COHERE_API_KEY=your_cohere_api_key

4. Usage
In any channel where the bot has read/write permissions, type:
!ask What is quantum computing?

   
