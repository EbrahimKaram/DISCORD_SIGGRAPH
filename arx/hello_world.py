from gc import get_objects
import discord

from discord.ext import commands, tasks


# ODE5MjA2NzQ4MDYxMTcxNzE0.YEjPvA.x-6BuQMpS0AcVK2fQnhP5DjBi20
# Bot token

# Bot name is Test_S2021_Bot#0035


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
        # existing_channel = client.get_channel()
        # existing_channel.delete()
        print(self.guilds)
        print(self.guilds[0].name)
        await self.guilds[0].create_text_channel('Created Channel')
    
        # await API.print_Channels()

        # our_guild=client.get_guild()
        # our_guild

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))



@bot.command(name="print_Channels", description="Print the channels available")
async def print_Channels(self, ctx):
    print("printing")
    for channel in client.get_all_channels():
        print(channel.name)

@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')
    
# def setup(bot):
#     bot.add_cog(API(bot))


client = MyClient()

client.run('ODE5MjA2NzQ4MDYxMTcxNzE0.YEjPvA.x-6BuQMpS0AcVK2fQnhP5DjBi20')
