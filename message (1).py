import os
import discord
from discord import Intents
import cohere
from dotenv import load_dotenv

load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
COHERE_API_KEY = os.getenv("COHERE_API_KEY")

co = cohere.Client(COHERE_API_KEY)

intents = Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f"{client.user} has connected to Discord!")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("!ask") or message.content.startswith("!ai"):
        command = message.content.split(' ')[0]
        user_message = message.content[len(command):].strip()

        print(
            f"User: {message.author.name}#{message.author.discriminator} \nQuestion: {user_message} \n"
        )

        if not user_message:
            await message.channel.send("Te rog să furnizezi un mesaj pentru AI.")
            return

        try:
            cohere_response = co.generate(
                model='command-xlarge',
                prompt=user_message,
                max_tokens=200
            )
            ai_response = cohere_response.generations[0].text.strip()

            print(f"AI response: {ai_response}")
            await message.channel.send(f"Răspunsul AI: {ai_response}")

        except cohere.CohereError as e:
            print(f"Error generating response: {e}")
            await message.channel.send("Ne pare rău, a apărut o eroare în generarea răspunsului.")
        except Exception as e:
            print(f"Unexpected error: {e}")
            await message.channel.send("A apărut o eroare neașteptată.")

if __name__ == "__main__":
    client.run(DISCORD_TOKEN)
