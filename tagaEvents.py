import logging
from discord.utils import get


def import_events(client, prefix, commands, server_id, channel_id, role_id):

    @client.event
    async def on_ready():
        logging.info('Logged in.')

    @client.command(name=commands['marking'],
                    pass_context=True)
    async def mark(context):
        server_match = True if context.message.server.id == server_id else False
        channel_match = True if context.message.channel.id == channel_id else False
        role_exists = True if role_id in [x.id for x in context.message.server.roles] else False
        user_has_role = True if role_id in [x.id for x in context.message.author.roles] else False
        role = get(context.message.server.roles, id=role_id)

        if server_match and channel_match:
            if role_exists:
                if not user_has_role:
                    await client.add_roles(context.message.author, role)
                    await client.say('Я тебя запомнила, {}'.format(context.message.author.mention))
                    logging.info('User id={} was given specified role.'.format(context.message.author.id))
                else:
                    await client.say('Ты уже был отмечен, {}'.format(context.message.author.mention))
                    logging.warning('User id={} has been already given role id={}'.format(context.message.author.id,
                                                                                          role_id))
            else:
                await client.say('Нет такой роли с id={}!'. format(role_id))
                logging.error('No role with id={}'.format(role_id))
        else:
            logging.error('Server or channel does not match!\n{}/{}\n{}/{}'.format(context.message.server.id,
                                                                                     server_id,
                                                                                     context.message.channel.id,
                                                                                     channel_id))
