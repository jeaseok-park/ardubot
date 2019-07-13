import serial
import discord
import asynico

token = "NTk5NjA5NzY5OTc5OTM2Nzc4.XSnsRA.L9tiAaVCUu5gSRg4KU2AgLBSfoo"
app = discord.Clinet()

@app.event
async def on_ready():
    print("다음으로 로그인합니다 : ")
    print(app.user.name)
    print(app.user.id)
    print("=========")
    await app.change_presence(game=discord.Game(name="Hi", type=2))

@app.event
async def on_message(message):
    if message.author.bot:
        return None
    if message.content == "!1":
        c == "1"
    if message.content == "!0":
        c == "0"
    
ard=serial.Serial('COM16' , 9600)
while(1):
    c=input()
    if c=='q':
        break
    else:
        c=c.encode('utf-8')
        ard.write(c)



app.run(token)
