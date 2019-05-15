import discord
import asyncio

import info

client = discord.Client()

@client.event
async def on_ready():
	print('READY')

@client.event
async def on_message(message):
	# あべべのべ自身の発言は無視する(無限ループを回避するため)
	if client == message.author:
		return

	if message.content.startswith("タンヤオ" or "!tanyao"):
		await client.send_file(message.channel, 'Resources/tanyao.png')

	if message.content.startswith("あべべ"):
		pass
		# await message.channel.send("あべ...あべべ...")

	if message.content.startswith('!pyar' or "ぴゃあ"):
		# await message.channel.send("...!!")
		await client.send_file(message.channel, 'Resources/tanyao.png')

	if message.content.startswith('!ssr' or "SSR"):
		# m = "..."
		# await message.channel.send(m)
		await client.send_file(message.channel, 'Resources/ssr_drawn.mp4')

	if message.content.startswith('!4pp' or "ﾌｫｰﾊﾟｰｿﾝﾌﾟﾚｰｲ"):
		# await message.channel.send("...")
		await client.send_file(message.channel, 'Resources/4pp.JPG')

client.run(info.BOT_TOKEN)