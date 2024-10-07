from email.message import Message
from http.client import responses

from typing import Final, final
from os import getenv
from dotenv import load_dotenv
from discord import Intents, client, member, message, Client , File

from responses import get_response

load_dotenv()
TOKEN = getenv('DISCORD_TOKEN')

intents: Intents = Intents.default()

client: Client = Client(intents=intents)


async def send_msg(msg:message, user_msg:str) -> None:

    is_private = 'lets talk privately' in user_msg or 'נדבר בפרטי' in user_msg

    chars_to_remove = "',:;!`~?&*#@$%)(~"
    translation_table = str.maketrans('', '', chars_to_remove)

    try:
        response: str = get_response(user_msg.lower().translate(translation_table),str(msg.author))
        if not response:
            pass
        if is_private :
              await msg.author.send(response)
        else:
            await msg.channel.send(response)

    except Exception as e:
        print(e)



@client.event
async def on_ready() -> None:
    print("running!")

@client.event
async def on_message(msg: message) -> None:
    if msg.author == client.user:
        return

    username: str = str(msg.author)
    user_message: str = msg.content


    print(f"u: {username} m: {user_message} ")
    await send_msg(msg,user_message)

def main() -> None:
    client.run(token=TOKEN)


if __name__ == '__main__':
    main()








