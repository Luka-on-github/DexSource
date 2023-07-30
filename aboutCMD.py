import discord
from discord.ext import commands
from discord import app_commands
import datetime
time = datetime.datetime.now()
datetime.datetime(2009, 1, 6, 15, 8, 24, 78915)

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!dev_", intents=intents)

@bot.event
async def on_ready():
    print("Logged into Nationdex at", time)
    try:
        synced = await bot.tree.sync()
        print(f'synced {len(synced)} command(s)')
    except Exeption as e:
        print(e)
        
@bot.tree.command(name="about")
async def about(interaction: discord.Interaction):
    embed=discord.Embed(title="About", description="<:Bosnia:1133834907362263090> <:England:1133834783793889290> <:Finland:1134043061190668360> <:Iraq:1133835397185687573> <:Ireland:1133834651786559628> <:Malaysia:1133835743329005710> <:Singapore:1133835155799281704> <:france:1133834989264441474> <:Afghanistan:1133835311005302934> \n \n Nationdex is a ballsdex similar like bot with more features and more wack! These include different types of balls for different seasons, a different spawning system, a econemy, quests, and a shop. \n If you want to find out more look bellow: \n Version: v2.31 \n Support server: https://discord.gg/W2UcGJC33h", color=0x7ca8db)
    await interaction.response.send_message(embed=embed)
  
bot.run("")
