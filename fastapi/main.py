import interactions, json
from interactions.ext.fastapi import *

with open('./config.json', 'r+') as f:
    config = json.load(f)

client = interactions.Client(intents=interactions.Intens.ALL)

client.run(config['token'])