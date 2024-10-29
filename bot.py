import discord

import subprocess
import os

bot = discord.Bot()

container_name = os.getenv('DOCKER_CONTAINER_NAME')

if not container_name:
    print('Error: DOCKER_CONTAINER_NAME environment variable not set.')
    exit(1)

server = bot.create_group("server", "Manage server")

@server.command(name='start', description='Start the Minecraft server.')
async def start(ctx):
    await ctx.respond('Starting the Minecraft server...')
    subprocess.run(['docker', 'start', container_name])
    await ctx.send('Minecraft server started.')

@server.command(name='stop', description='Stop the Minecraft server.')
async def stop(ctx):
    await ctx.respond('Stopping the Minecraft server...')
    subprocess.run(['docker', 'stop', container_name])
    await ctx.send('Minecraft server stopped.')

@server.command(name='restart', description='Restart the Minecraft server.')
async def restart(ctx):
    await ctx.respond('Restarting the Minecraft server...')
    subprocess.run(['docker', 'restart', container_name])
    await ctx.send('Minecraft server restarted.')

@server.command(name='status', description='Get the status of the Minecraft server.')
async def status(ctx):
    result = subprocess.run([f'docker', 'ps', '--filter', f'name={container_name}'], stdout=subprocess.PIPE)
    if container_name.encode() in result.stdout:
        await ctx.respond(f'Minecraft server ({container_name}) is running.')
    else:
        await ctx.respond(f'Minecraft server ({container_name} is not running.')

bot_token = os.getenv('DISCORD_BOT_TOKEN')

if bot_token:
    bot.run(bot_token)
else:
    print('Error: DISCORD_BOT_TOKEN environment variable not set.')
    exit(1)