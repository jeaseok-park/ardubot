import serial
import discord
import asyncio
ser=serial.Serial('COM16',9600)

app = discord.Client()

token = "NTk5NjA5NzY5OTc5OTM2Nzc4.XSrVPQ.GNwMRG60wFBO_ov09CNKsR4wUx8"

@app.event
async def on_ready():
    print("다음으로 로그인합니다 : ")
    print(app.user.name)
    print(app.user.id)
    print("=========")
        
     
@app.event
async def on_message(message):
    
        if message.author.bot:
            return None
        if message.content == "-1":
            c="1"
            print(c)
            c=c.encode('utf-8')
            ser.write(c)
        if message.content == "-0":
            c="0"
            print(c)
            c=c.encode('utf-8')
            ser.write(c)
            
            
app.run(token)
