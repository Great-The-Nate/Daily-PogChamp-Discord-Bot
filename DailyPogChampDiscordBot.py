import base64
import requests
import discord
import json

token = "TOKEN"
guildID = "GUILD_ID"
header = {'Authorization': 'Bot %s' % token}


class Client(discord.Client):

    async def on_ready(self):
        try:
        	self.deleteEmote()
        except:
        	pass
        self.createEmote()

    def createEmote(self):
    	image = str(base64.b64encode(requests.get("https://static-cdn.jtvnw.net/emoticons/v1/305289452/4.0").content))[2:-1]
    	
    	emoteInfo = {
    		"name":"PogChamp", 
    		"image":"data:image/png;base64,%s" % image,
    		"roles":[]
    	}

    	response = requests.post("https://discord.com/api/guilds/%s/emojis" % guildID, json = emoteInfo, headers=header)
    	print(response.content)

    def deleteEmote(self):
    	emoteList = json.loads(requests.get("https://discord.com/api/guilds/%s/emojis" % guildID, headers=header).content)

    	emoteID = "";
    	for i in emoteList:
    		if(i['name']=='PogChamp'):
    			emoteID = i['id']
    			break;

    	response = requests.delete("https://discord.com/api/guilds/%s/emojis/%s" % (guildID, emoteID), headers=header)
    	print(response.content)
    	

client = Client()
client.run(token)