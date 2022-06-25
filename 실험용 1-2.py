import discord, asyncio, datetime, pytz

client = discord.Client()

@client.event
async def on_ready():
    print("--------봇 사용 가능--------")
    await client.change_presence(status = discord.Status.online, activity=discord.Game("Tree봇, 명령어"))

@client.event
async def on_message(message):
    if message.content == "T.hello":
        await message.channel.send ("{}: [ hello! :sunglasses: ]" .format(message.author.mention))
    
    if message.content == "T.bye":
        await message.channel.send ("{}: [ byebye.. :yawning_face: ]" .format(message.author.mention))



    if message.content == "T.help":
     embed = discord.Embed(title="TreeBot.💬", description="«현재 사용가능 TreeBot 명령어»", color=0x86E57F) # Embed의 기본 틀(색상, 메인 제목, 설명)
     embed.set_thumbnail(url="https://i.imgur.com/pcxn7ky.png")
     embed.add_field(name = 'T.help:', value = '도움말 표시✅', inline = False)
     embed.add_field(name = 'T.hello:', value = '[ hello! :sunglasses: ]', inline = False)
     embed.add_field(name = 'T.bye:', value = '[ byebye.. :yawning_face: ]', inline = False)
     embed.add_field(name = '........', value = '........', inline = False)
     embed.set_footer(text="명령어는 더욱 추가될 예정입니다.") # 하단에 들어가는 조그마한 설명
     await message.channel.send(embed=embed) # embed를 포함 한 채로 메시지 전송


























client.run('OTg5ODkyMDU5NTgwMjM1ODI2.GnTJB9.zusgSnhW45_IEs8pSoHIOYlRsHgiY50qUyytrk')







