import os
import datetime
import pytz
import discord
import asyncio
from tasks import tasks
import warnings
warnings.filterwarnings("ignore")
    

class MyClient(discord.Client):
    
    async def on_ready(self):
        print('Logged on as', self.user)
        task = tasks()
      
        while True:
          tz_NY = pytz.timezone('Asia/Kolkata')
          dt = datetime.datetime.now(tz_NY)
          time = dt.strftime("%I:%M:%p")
          print(time,flush=True)
    
          if time not in task.daily_tasks:
            pass
          else :
            for i in task.daily_tasks[time].items():
              id = int(i[0])
              title = i[1]['Title']
              des = i[1]['Description']
              user = await super().fetch_user(id)
              
              await user.send(f'{title}\n\t\t{des}')
            
          await asyncio.sleep(59)
        
            
      
    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        if message.content.lower() == 'begin':
            await message.channel.send(f'Welcome {message.author.name} \n\t\t This bot for Reminding tasks For Your with prefered Time')

        if '-daily' in message.content:
          task = tasks()
          
          l = message.content.split()
          task.daily_task(message.author.id,l)
          await message.channel.send('Task Added Successfully')

        if message.content == 'ping':
          await message.channel.send('pong')


intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)


token = os.getenv('DISCORD_TOKEN')

client.run(token)