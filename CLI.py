from discord.ext import commands

class DocBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="!")

    async def on_ready(self):
        print("Le bot est prêt.")

bot = DocBot()
bot.run("OTU5MzUxODcwNDMyODgyNzM4.YkaoDQ.F4FfuAQ6aGuYjhm00MIIsQhbVCk")