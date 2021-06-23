import discord
import pandas as pd
from discord.ext import commands

# Resource: https://realpython.com/how-to-make-a-discord-bot-python/
TOKEN = "ODE5MjA2NzQ4MDYxMTcxNzE0.YEjPvA.x-6BuQMpS0AcVK2fQnhP5DjBi20"

# Bot life#4006
# ODU2ODg4MjAwMzk1NjIwMzk1.YNHlUw.9Ugaav95V1rtmswvU_E3eSjyWrw

# Test_S2021_Bot#0035
# ODE5MjA2NzQ4MDYxMTcxNzE0.YEjPvA.x-6BuQMpS0AcVK2fQnhP5DjBi20

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

# This is the ID for Test_S2021 (the server)
guild_id = 779464282878115880


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')
    print('Logged on as {0}!'.format(bot.user.name))
    global guild_id
    guild_id = bot.guilds[0].id
    print(bot.guilds[0].name, guild_id)


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

# we might need to be careful about which server we delete the channels and specify the ID


@bot.command(name='purge', description='delete every channel here in this system', brief='DELETE EVERYTHING')
async def purge(ctx):
    our_guild = bot.get_guild(guild_id)
    channels_in_guild = await our_guild.fetch_channels()
    if len(channels_in_guild) > 0:
        for channel in channels_in_guild:
            print(channel.name)
            await channel.delete()
    await ctx.send('All channels and categories are gone!!!')


# Read from CSV
@bot.command(name='create_from_CSV', description='create channels and categories from CSV', brief='starts the new world ')
async def createFromCSV(ctx):
    df = pd.read_csv("..\s2021_sessions.csv")
    categories = {}
    for event_type in df["Category"].unique():
        if isinstance(event_type, str):
            category = await bot.guilds[0].create_category(event_type)
            categories[event_type] = category
    await ctx.send('created all the categories!')

    df["Reduced_sessionTitle"] = df['Session Title'].str.strip().str[:20]
    # This Format : https://discord.com/channels/779464282878115880/854343504058384424
    df["Channel Link"] = ""
    for index, row in df.iterrows():
        # We can't have more than 50 channels in category
        if (not isinstance(row['Category'], str)) or (len(categories[row['Category']].channels) < 50):
            # TODO: check for empty catagories
            channel_id = 0
            if row["Type of Channel"] == 'Text':
                if isinstance(row['Category'], str):
                    channel = await bot.guilds[0].create_text_channel(row['Reduced_sessionTitle'], category=categories[row['Category']])
                else:
                    channel = await bot.guilds[0].create_text_channel(row['Reduced_sessionTitle'])
            elif row["Type of Channel"] == 'Voice':
                if isinstance(row['Category'], str):
                    channel = await bot.guilds[0].create_voice_channel(row['Reduced_sessionTitle'], category=categories[row['Category']])
                else:
                    channel = await bot.guilds[0].create_voice_channel(row['Reduced_sessionTitle'])
            elif row["Type of Channel"] == 'Stage':
                # Stage channels are only available to community servers
                if isinstance(row['Category'], str):
                    channel = await bot.guilds[0].create_text_channel(row['Reduced_sessionTitle'], category=categories[row['Category']])
                else:
                    channel = await bot.guilds[0].create_text_channel(row['Reduced_sessionTitle'])
            channel_id = channel.id
            row["Channel Link"] = "https://discord.com/channels/{0}/{1}".format(
                guild_id, channel_id)
    df.to_csv("..\s2021_sessions.csv", index=False)
    await ctx.send('All channels and categories are created from CSV!!!')


@ bot.command(name='create_links', description='create links for all the participants', brief='create invite links')
async def createInviteLinks(ctx, *args):
    email_csv = "..\Registrion_Emails.csv"
    emails = pd.read_csv(email_csv)
    if ((len(args) > 0) and args[0].isdigit()):
        print(args[0])

        emails["Numbers"] = pd.Series(range(1, int(args[0])+1))
    emails["Invitation links"] = ""
    # TODO use args to parse number of emails
    for index, row in emails.iterrows():
        print(row['Numbers'])
        # Reference: https://discordpy.readthedocs.io/en/latest/api.html?highlight=create_invite#discord.abc.GuildChannel.create_invite
        # ASSUMPTION: The link should not expire but is allowed to be used only once
        # Emial is not needed
        invite = await bot.guilds[0].channels[0].create_invite(max_age=0, max_uses=5)
        emails.at[index, "Invitation links"] = invite.url
        print(invite.url)
    emails.to_csv(email_csv, index=False)
    await ctx.send('Invitation links were created!')


@bot.command(name='reset', description='delete everything and create again from a csv', brief='restart the world')
async def resetWorld(ctx):
    await purge(ctx)
    await createFromCSV(ctx)


@bot.command(name='members', description='Gets you the members in the guild', brief='Who is in the server')
async def getMembers(ctx):
    our_guild = bot.get_guild(guild_id)
    # There are 16 members
    print("How many members are in this server", our_guild.member_count)
    # print(our_guild.members)
    # members = our_guild.fetch_members()
    members = our_guild.members
    print("The length of memebers from the call", len(members))
    df = pd.DataFrame(
        columns=('Name', 'Discriminator', 'ID', 'Display Name', 'Status', "Joined on"))
    i = 0
    for member in members:
        print(member.name, member.discriminator, member.id, member.display_name,
              member.status, member.joined_at)
        df.loc[i] = [member.name, member.discriminator, member.id,
                     member.display_name, member.status, member.joined_at]
        i = i+1
        # print(member.roles)
    df.to_csv("..\Members from {}.csv".format(our_guild.name), index=False)
    await ctx.send('Rerieved all memebers')

# TODO: find a way to reset roles if need be
# await remove_roles(*roles, reason=None, atomic=True)
@bot.command(name='assign_roles', description='Assing the roles to the different members', brief='Tell who does what')
async def roleAssigned(ctx):
    df = pd.read_csv("..\Role Assignment.csv")
    df[["Name", "delim"]] = df["User name"].str.split("#", expand=True)
    our_guild = bot.get_guild(guild_id)
    # print(our_guild.roles)
    for index, row in df.iterrows():
        role = discord.utils.get(our_guild.roles, name=row["Role"])
        member = discord.utils.get(
        our_guild.members, name=row["Name"], discriminator=str(row["delim"]))
        await member.add_roles(role)
# discord.Member. add_roles

    await ctx.send('the roles have been assigned')


@bot.command(name='export_channels', description='export channel links, names, and categories to server', brief='export channel links to csv')
async def exportChannles(ctx):
    our_guild = bot.get_guild(guild_id)
    channels_in_guild = await our_guild.fetch_channels()
    df = pd.DataFrame(columns=('Channel Name', 'Category', 'Type', 'link'))
    if len(channels_in_guild) > 0:
        for i, channel in enumerate(channels_in_guild):
            print(channel.name, channel.category, channel.type, channel.id)
            link = "https://discord.com/channels/{0}/{1}".format(
                guild_id, channel.id)
            df.loc[i] = [channel.name, channel.category, channel.type, link]

    await ctx.send('All channels links have been found!')
    df.to_csv("..\Channel info from {}.csv".format(
        our_guild.name), index=False)
    await ctx.send("dumped to 'Channel info from {}.csv'".format(our_guild.name))

# Commands don't work when this is set
# @bot.event
# async def on_message(message):
#     print('Message from {0.author}: {0.content}'.format(message))
bot.run(TOKEN)
