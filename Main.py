import discord
import asyncio
import datetime
token = "
client = discord.Client()
@client.event
async def on_ready():
    print('로그인되었습니다!')
    print(client.user.name)
    print(client.user.id)
    print('====================================')
    while True:
       user = len(client.users)
       server = len(client.guilds)
       messages = ["안녕하세요!", "Hestia#1044님이 제작하신 봇" , "TEAM UV" , str(user) + "명이 저와 놀고있어요!", str(server) + "개의 서버에서 안전하게 보관되고 있어요!",";도움으로 저의 명령어를 알아보세요!"]
       for (m) in range(5):
           await client.change_presence(status=discord.Status.dnd, activity=discord.Activity(name=messages[(m)], type=discord.ActivityType.playing))
           await asyncio.sleep(4)

@client.event
async def on_message(message):
    if message.content == ';핑':
        await message.channel.send('퐁')
    if message.content == ';도움':
        embed=discord.Embed(title="도움말", description="접두사는 ``;``입니다", color=0x00fffb)
        embed.add_field(name="핑", value="핑을 체크합니다(자세하지 않아요)", inline=False)
        embed.add_field(name="내정보", value="유저님의 정보를 알려드립니다", inline=False)
        embed.add_field(name="서버 정보", value="서버의 정보를 알려드립니다", inline=False)
        await message.channel.send(embed=embed)
    if message.content == ';내정보':
        user = message.author
        date = datetime.datetime.utcfromtimestamp(((int(user.id) >> 22) + 1420070400000) / 1000)
        embed=discord.Embed(title=user.name+"님의 정보", description=user.name+"님의 정보를 보여드립니다", color=0x00ffee)
        embed.add_field(name="디스코드 닉네임", value=user, inline=True)
        embed.add_field(name="서버 닉네임", value=user.display_name, inline=False)
        embed.add_field(name="가입일", value=str(date.year)+"년"+str(date.month)+"월"+str(date.day)+"일", inline=False)
        embed.add_field(name="아이디", value=user.id, inline=False)
        await message.channel.send(embed=embed)
    if message.content == ";서버 정보":
       embed=discord.Embed(title=message.guild.name+" 서버의 정보", description=message.guild.name+" 서버의 정보를 보여드립니다", color=0x00ffee)
       embed.add_field(name="서버 이름", value=message.guild.name, inline=True)
       embed.add_field(name="서버 인원", value=message.guild.member_count, inline=False)
       embed.add_field(name="서버 채널 수", value="테스트중", inline=False)
       embed.add_field(name="서버 아이디", value=message.guild.id, inline=False)
       embed.add_field(name="서버 소유주 아이디", value=message.guild.owner_id, inline=False)
       embed.add_field(name="보안 레벨", value=message.guild.verification_level, inline=False)
       embed.add_field(name="서버 부스트 횟수", value=message.guild.premium_subscription_count, inline=False)
       embed.add_field(name="서버 시스템 채널", value=message.guild.system_channel, inline=False)
       embed.add_field(name="서버 부스터", value=message.guild.premium_subscribers, inline=False)
       embed.add_field(name="서버 아이콘 url", value=message.guild.icon_url, inline=False)
       await message.channel.send(embed=embed)
    if message.content == (";투표"):
        vote = message.content[4:].split("/")
        await message.channel.send(message.channel, vote[0])
        for i in range(1, len(vote)):
           choose = await message.channel.send(message.channel, vote[i])
           await client.add_reaction(choose, "👍")
    if message.content == (";초대"):
        await message.channel.send ("https://discord.com/api/oauth2/authorize?client_id=757426337479786577&permissions=8&scope=bot")
    if message.content == (";hellothisisverification"):
        await message.channel.send ("Hestia#1234")
    if message.content
@client.event
async def on_member_join(member):
    syschannel = member.guild.system_channel.id 
    try:
        embed=discord.Embed(
            title=f'환영합니다! Welcome!',
            description=f'{member}님 이곳은  {member.guild}입니다 환영합니다 ! \n현재 서버 인원수: {str(len(member.guild.members))}명',
            colour=0x00ff00
        )
        embed.set_thumbnail(url=member.avatar_url)
        await client.get_channel(syschannel).send(embed=embed)
    except:
        return None

client.run(token)
