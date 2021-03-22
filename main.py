import discord
import asyncio
import cleverbotfree.cbfree
import json
import random
from ratelimiter import RateLimiter

cb = cleverbotfree.cbfree.Cleverbot()

bot = discord.Client(description="xddd", self_bot=True)

with open('config.json') as f:
  # you may have to use full paths for this
  config = json.load(f)

token = config.get("token")

illegal_character = {
                ':'
                '<'
                '>'
                '_'
                "'"
                "-"
                    }

misc = {
      "yes"
      "no"
      "maybe"
      "idk"
        }

@bot.event
async def on_ready():
        print("Logged in")



@RateLimiter(max_calls=7, period=23)
@bot.event
async def on_message(message):
         try:
                userInput = (message.content)
                if message.author == bot.user:
                         return
                if userInput in misc:
                         foo = ['hmm', 'ok', 'alright' ]
                         message.channel(random.choice(foo))
                if userInput in illegal_character:
                         print(f"{message.author} has said an illegal character")
                         return
                # filtering characters that seem to break the script
                if len(userInput) < 4:
                         print(f"string too short")
                # adding minimum message length to try and minimize spam and language confusion
                else:
                         sex = random.uniform(0.4, 2.5)
                         await asyncio.sleep(sex)
                # this also helps minimize spam
                         async with message.channel.typing():
                                 response = cb.single_exchange(userInput)
                        # getting cleverbot ai response
                                 await message.channel.send(response)
                        # sending response
                                 print(message.content)
                                 print("bot:" + response)
         except discord.errors.Forbidden:
                   return        

bot.run(token, bot=False)
