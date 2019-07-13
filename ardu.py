import serial
import discord

token = "NTk5NjA5NzY5OTc5OTM2Nzc4.XSn5Xg.l1kIn6glvcB3VvFqEQ70upJLGMQ"
app = discord.Clinet()


ard=serial.Serial('COM16' , 9600)
while(1):
    c=input()
    if c=='q':
        break
    else:
        c=c.encode('utf-8')
        ard.write(c)



app.run(token)
