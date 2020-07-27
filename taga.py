
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

		logging.info('\n'.join([
			'Logging in with token %s' % self.token
		,	'with server_id %s' % self.channel_id
		,	'with role_id %s' % self.role_id
		,	'with prefix %s' % self.prefix
		,	'and commands %s' % self.commands
		]))

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
