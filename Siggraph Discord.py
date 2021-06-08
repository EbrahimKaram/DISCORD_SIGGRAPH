import discord
import pandas as pd
from discord.ext import commands

# Resource: https://realpython.com/how-to-make-a-discord-bot-python/
TOKEN = "ODE5MjA2NzQ4MDYxMTcxNzE0.YEjPvA.x-6BuQMpS0AcVK2fQnhP5DjBi20"

bot = commands.Bot(command_prefix='!')


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')
    print('Logged on as {0}!'.format(bot.user.name))


@bot.command(name='create_channel', description='Create text channel Channel here', brief="Let There be Channels")
async def create_channel(ctx, *args):
    if len(args) > 0:
        for arg in args:
            await bot.guilds[0].create_text_channel(arg)
            await ctx.send('Created Channel named {}'.format(arg))
    else:
        await bot.guilds[0].create_text_channel("Empty Channel")


@bot.command(name='ping', description='The Classic Ping Pong example', brief='PING PONG')
async def ping(ctx):
    await ctx.send('Pong!')

# PRINT OUT EXISTING CHANNELS

# DELETES all the channels in the system
# TODO: we might need to be careful about which server we delete the channels and specify the ID


@bot.command(name='purge', description='delete every channel here in this system', brief='DELETE EVERYTHING')
async def purge(ctx):
    if len(list(bot.get_all_channels())) > 0:
        for channel in bot.get_all_channels():
            print(channel.name)
            await channel.delete()
    await ctx.send('All channels and categories are gone!!!')


# Read from CSV
@bot.command(name='create_from_CSV', description='create channels and categories from CSV', brief='starts the new world ')
async def createFromCSV(ctx):
    df = pd.read_csv("..\s2020_sessions_Test.csv")
    categories = {}
    for event_type in df["Event Types"].unique():
        category = await bot.guilds[0].create_category(event_type)
        categories[event_type] = category
    await ctx.send('created all the categories!')

    df["Reduced_sessionTitle"] = df['Session Title'].str.strip().str[:20]

    for index, row in df.iterrows():
        # We can't have more than 50 channels in category
        if len(categories[row['Event Types']].channels) < 50:
            await bot.guilds[0].create_text_channel(row['Reduced_sessionTitle'], category=categories[row['Event Types']])
    await ctx.send('All channels and categories are created from CSV!!!')


@bot.command(name='create_links', description='create links for all the participants', brief='create invite links')
async def createInviteLinks(ctx):
    email_csv = "..\Registrion_Emails.csv"
    emails = pd.read_csv(email_csv)
    emails["Invitation links"] = ""
    for index, row in emails.iterrows():
        print(row['Emails'])
        # Reference: https://discordpy.readthedocs.io/en/latest/api.html?highlight=create_invite#discord.abc.GuildChannel.create_invite
        # ASSUMPTION: The link should not expire but is allowed to be used only once
        invite = await bot.guilds[0].channels[0].create_invite(max_age=0, max_uses=1)
        row["Invitation links"] = invite.url
        print(invite.url)
    emails.to_csv(email_csv, index=False)
    await ctx.send('Invitation links were created!')


# TODO: The Command below is not working. Sending multiple delete messages back.
@bot.command(name='reset', description='delete everything and create again from a csv', brief='restart the world', hidden=True)
async def createFromCSV(ctx):
    await purge(ctx)
    await createFromCSV(ctx)

# Commands don't work when this is set
# @bot.event
# async def on_message(message):
#     print('Message from {0.author}: {0.content}'.format(message))
bot.run(TOKEN)
