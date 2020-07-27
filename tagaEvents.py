
import logging
import discord

def import_events(client, prefix, commands, server_id, channel_id, role_id):

	@client.event
	async def on_ready():
		logging.info('Logged in.')

	@client.command(name=commands['barking']['name'], pass_context=True)
	async def bark(context, arg=None):
		try:
			num = int(arg)
			if num < 1: num = 1
			if num > 9: num = 9
		except Exception:
			num = 1

		logging.info('Woof x %s from message "%r".' % (num, context.message))

		await context.send('Woof!' * num)

	@client.command(name=commands['marking']['name'], aliases=commands['marking']['aliases'], pass_context=True)
	async def mark(context):
		server_match  = (context.message.guild.id   == server_id)
		channel_match = (context.message.channel.id == channel_id)
		role_exists   = (role_id in [x.id for x in context.message.guild.roles])
		user_has_role = (role_id in [x.id for x in context.message.author.roles])
		role_to_add   = discord.utils.get(context.message.guild.roles, id=role_id)

		if server_match and channel_match:
			if role_exists:
				if not user_has_role:
					await context.message.author.add_roles(role_to_add)
					await context.send('Я тебя запомнила, {}'.format(
						context.message.author.mention
					))

					logging.info('User id={} was given specified role.'.format(
						context.message.author.id
					))
				else:
					await context.send('Ты уже был отмечен, {}'.format(
						context.message.author.mention
					))

					logging.warning('User id={} has been already given role id={}'.format(
						context.message.author.id
					,	role_id
					))
			else:
				await context.send('Нет такой роли с id={}!'.format(role_id))
				logging.error('No role with id={}'.format(role_id))
		else:
			logging.error('Server or channel does not match!\n{}/{}\n{}/{}'.format(
				context.message.guild.id
			,	server_id
			,	context.message.channel.id
			,	channel_id
			))
