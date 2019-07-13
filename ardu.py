import serial
import os

ard=serial.Serial('COM16' , 9600)
while(1):
    c=input()
    if c=='q':
        break
    else:
        c=c.encode('utf-8')
        ard.write(c)

access_token=os.environ["BOT_TOKEN"]
client.run(acess_token)
