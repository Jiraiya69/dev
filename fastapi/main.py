import interactions, json
from interactions.ext.fastapi import route

with open('./config.json', 'r+') as f:
    config = json.load(f)

class fastapi(interactions.Extension):
    def __init__(self: interactions.Client):
        self.client = client

    @route('GET', '/')
    async def index():
        return {"status": "passed"}

def setup(client):
    fastapi(client)