import logging
import discord
from discord.ext.commands import Bot
import tagaEvents

class Taga:
    def __init__(self, settings):
        logging.basicConfig(level=logging.INFO)
        logging.info('Nuclear launch detected!')

        self.token = settings['token']
        self.server_id = settings['server_id']
        self.channel_id = settings['channel_id']
        self.role_id = settings['role_id']
        self.prefix = settings['command_prefix']
        self.commands = settings['commands']

        logging.info('Logging in with token {}\nwith server_id {}\nwith role_id {}\nwith prefix {}\nand commands {}'
                     .format(self.token, self.channel_id, self.role_id, self.prefix, self.commands))

        self.client = Bot(self.prefix)

        self.load_events()

    def load_events(self):
        tagaEvents.import_events(self.client, self.prefix, self.commands, self.server_id, self.channel_id, self.role_id)

    def run(self):
        self.client.run(self.token)

