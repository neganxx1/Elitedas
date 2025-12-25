import discord
from discord.ext import commands, tasks

# تهيئة البوت
intents = discord.Intents.default()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} متصل!')
    # بدء مهمة تغيير الحالة
    change_status.start()

@tasks.loop(seconds=10)  # تغيير كل 10 ثواني
async def change_status():
    # تغيير الحالة إلى "أحب دامون سلفاتوري"
    await bot.change_presence(
        activity=discord.Game(name="I LOVE Damone Salvatore"),
        status=discord.Status.online
    )
    print("تم تغيير الحالة!")

# إدخال التوكين هنا
TOKEN = 'MTM2MzY4NjEyMTI3MTMzMjk1NA.GzrYP1.jqndk5w1TTBXo1bVJVx2dEtdKnQfqtIfrMlZ4A'

if __name__ == "__main__":
    bot.run(TOKEN)