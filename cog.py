from discord.ext import commands, tasks

class API(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="print_Channels", description="Print the channels available")
    async def print_Channels(self, ctx):
        print("printing")
        for channel in client.get_all_channels():
            print(channel.name)

    @commands.command()
    async def ping(ctx):
        await ctx.send('Pong!')

    
def setup(bot):
    bot.add_cog(API(bot))