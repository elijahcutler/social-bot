import discord
from discord.ext import commands
import subprocess
import os

intents = discord.Intents.default()
bot = commands.Bot(command_prefix='/', intents=intents)

container_name = os.getenv('DOCKER_CONTAINER_NAME')

if not container_name:
    print('Error: DOCKER_CONTAINER_NAME environment variable not set.')
    exit(1)

@bot.slash_command(name='start_server', description='Start the Minecraft server.')
async def start_server(ctx):
    await ctx.respond('Starting the Minecraft server...')
    subprocess.run(['docker', 'start', container_name])
    await ctx.send('Minecraft server started.')

@bot.slash_command(name='stop_server', description='Stop the Minecraft server.')
async def stop_server(ctx):
    await ctx.respond('Stopping the Minecraft server...')
    subprocess.run(['docker', 'stop', container_name])
    await ctx.send('Minecraft server stopped.')

@bot.slash_command(name='restart_server', description='Restart the Minecraft server.')
async def restart_server(ctx):
    await ctx.respond('Restarting the Minecraft server...')
    subprocess.run(['docker', 'restart', container_name])
    await ctx.send('Minecraft server restarted.')

@bot.slash_command(name='server_status', description='Get the status of the Minecraft server.')
async def server_status(ctx):
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