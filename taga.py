
import logging
import discord
from discord.ext.commands import Bot
import tagaEvents

class Taga:
	def __init__(self, settings):
		logging.basicConfig(level=logging.INFO)
		logging.info('Initializing settings.')

		self.token	= settings['token']
		self.prefix	= settings['command_prefix']
		self.commands	= settings['commands']
		self.server_id	= int(settings['server_id'])
		self.channel_id	= int(settings['channel_id'])
		self.role_id	= int(settings['role_id'])

		logging.info(
			'\n'.join(
				[
					'Logging in with token "{self.token}"'
				,	'Using server ID "{self.server_id}"'
				,	'Using channel ID "{self.channel_id}"'
				,	'Using role ID "{self.role_id}"'
				,	'Listening for command prefix "{self.prefix}"'
				,	'Listening for commands "{self.commands}"'
				]
			).format(self=self)
		)

		self.client = Bot(self.prefix)

		self.load_events()

	def load_events(self):
		tagaEvents.import_events(
			self.client
		,	self.prefix
		,	self.commands
		,	self.server_id
		,	self.channel_id
		,	self.role_id
		)

	def run(self):
		self.client.run(self.token)
