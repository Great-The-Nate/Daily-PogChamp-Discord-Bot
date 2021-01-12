import base64
import requests
import discord
import json
import time
import datetime

token = "TOKEN"
guildID = "GUILD_ID"
header = {'Authorization': 'Bot %s' % token}
clientID = "CLIENT_ID"

class Client(discord.Client):
	
    async def on_ready(self):
        while(True):
          	if datetime.datetime.now().hour == 18:
            	try:
              		self.deleteEmote()
            	except:
             		pass
            	await self.createEmote()
            	time.sleep(1800)
        	time.sleep(1800)


    async def createEmote(self):
        response = str(requests.get("https://api.twitch.tv/kraken/chat/emoticon_images?emotesets=0&client_id=%s" % clientID, headers={"Accept": "application/vnd.twitchtv.v5+json"}).content)[2:-1]
        emoteID = json.loads(response)["emoticon_sets"]["0"][0]["id"]

        image = requests.get("https://static-cdn.jtvnw.net/emoticons/v1/%s/3.0" % emoteID).content

        await client.user.edit(avatar=image)
        b64 = str(base64.b64encode(image))[2:-1]
        emoteInfo = {"name":"PogChamp", "image":"data:image/png;base64,%s" % b64, "roles":[]}
        
        response = requests.post("https://discord.com/api/guilds/%s/emojis" % guildID, json = emoteInfo, headers=header)
        print(response.content)


    def deleteEmote(self):
    	emoteList = json.loads(requests.get("https://discord.com/api/guilds/%s/emojis" % guildID, headers=header).content)

    	id = "";
    	for i in emoteList:
    		if(i['name']=='PogChamp'):
    			id = i['id']
    			break;

    	response = requests.delete("https://discord.com/api/guilds/%s/emojis/%s" % (guildID, id), headers=header)
    	print(response.content)
    	

client = Client()
client.run(token)