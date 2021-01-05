import discord
import asyncio
import datetime
import requests
from bs4 import BeautifulSoup
from discord.ext import commands
import ast
import traceback
INTENTS = discord.Intents.all()

client = commands.Bot(command_prefix=';')

token = 'token'

@client.event
async def on_ready():
    print('삐리릭 봇이 켜졌다')
    print(client.user.name)
    print(client.user.id)
    print('====================================')
    user = len(client.users)
    server = len(client.guilds)
    message = ["안녕하세요!", "Hestia#5444님이 제작하신 봇", str(user) + "명이 저와 놀고있어요!", str(server) + "개의 서버에서 안전하게 보관되고 있어요!", ";도움으로 저의 명령어를 알아보세요!"]
    while True:
        await client.change_presence(status=discord.Status.online, activity=discord.Game(message[0]))
        message.append(message.pop(0))
        await asyncio.sleep(4)

@client.event
async def on_message(message):
    if message.content == ';도움':
        embed=discord.Embed(title="도움말", description="접두사는 ``;``입니다", color=0x00fffb)
        embed.add_field(name="핑", value="핑을 체크합니다(자세하지 않아요)", inline=False)
        embed.add_field(name="내정보", value="유저님의 정보를 알려드립니다", inline=False)
        embed.add_field(name="서버 정보", value="서버의 정보를 알려드립니다", inline=False)
        embed.add_field(name="초대", value="봇의 초대링크르 드립니다!", inline=False)
        embed.add_field(name="프로필", value="당신의 프로필을 보여드립니다!", inline=False)
        embed.add_field(name="남프로필 (id 입력)", value="그 id를 가진 사람의 프로필을 보여드립니다!", inline=False)
        embed.add_field(name="티켓", value="티켓 채널을 만듭니다!", inline=False)
        embed.add_field(name="티켓 삭제", value="티켓 채널을 삭제합니다!(관리자 명령어)", inline=False)
        embed.add_field(name="찬반투표 (주제)", value="찬반투표를 만듭니다!", inline=False)
        embed.add_field(name="남정보 (id 입력)", value="그 id의 주인의 정보를 찾습니다!", inline=False)
        embed.add_field(name="청소 (갯수)", value="갯수만큼 메시지를 청소합니다!(관리자 명령어)", inline=False)
        embed.add_field(name="밴 (유저 id)", value="그 id를 가진 사람을 밴합니다!(관리자 명령어)", inline=False)
        embed.add_field(name="언밴 (유저 id)", value="그 id를 가진 유저를 언밴합니다!", inline=False)
        embed.add_field(name="킥 (유저 id)", value="그 id를 가진 사람을 킥합니다!(관리자 명령어)", inline=False)
        embed.add_field(name="타이머 (시간)", value="시간을 입력한만큼 기다렸다가 그 시간이 지나면 멘션해드립니다!", inline=False)
        embed.add_field(name="채널메시지 (채널 id) (보낼 메시지)", value="그 id를 가진 채널에 입력한 메시지를 보냅니다!", inline=False)
        embed.add_field(name="건의 (건의할 것)", value="건의할 것을 개발자 서버에 보냅니다!", inline=False)
        embed.add_field(name="대신멘션 (유저 id)", value="멘션하기 쑥쓰러우실 때 사용하세요!", inline=False)
        await message.channel.send(embed=embed)
    if message.content == ';내정보':
        user = message.author
        date = datetime.datetime.utcfromtimestamp(((int(user.id) >> 22) + 1420070400000) / 1000)
        roles = [role for role in message.author.roles]
        embed=discord.Embed(title=user.name+"님의 정보", description=user.name+"님의 정보를 보여드립니다", color=0x00ffee)
        embed.add_field(name="디스코드 닉네임", value=user, inline=True)
        embed.add_field(name="서버 닉네임", value=user.display_name, inline=False)
        embed.add_field(name="가입일", value=str(date.year)+"년"+str(date.month)+"월"+str(date.day)+"일", inline=False)
        embed.add_field(name="아이디", value=user.id, inline=False)
        embed.add_field(name="봇 여부", value=user.bot, inline=False)
        embed.add_field(name="역할", value=" ".join([role.mention for role in roles]), inline=False)
        embed.add_field(name="관리자 여부", value="테스트중", inline=False)
        embed.set_thumbnail(url=message.author.avatar_url)
        await message.channel.send(embed=embed)
    if message.content == ";서버 정보":
       embed=discord.Embed(title=message.guild.name+" 서버의 정보", description=message.guild.name+" 서버의 정보를 보여드립니다", color=0x00ffee)
       embed.add_field(name="서버 이름", value=message.guild.name, inline=True)
       embed.add_field(name="서버 인원", value=message.guild.member_count, inline=False)
       embed.add_field(name="서버 채널 수", value="테스트중", inline=False)
       embed.add_field(name="서버 아이디", value=message.guild.id, inline=False)
       embed.add_field(name="서버 소유주 아이디", value=message.guild.owner, inline=False)
       embed.add_field(name="보안 레벨", value=message.guild.verification_level, inline=False)
       embed.add_field(name="서버 부스트 횟수", value=message.guild.premium_subscription_count, inline=False)
       embed.add_field(name="서버 시스템 채널", value=message.guild.system_channel, inline=False)
       embed.add_field(name="서버 부스터", value=message.guild.premium_subscribers.name, inline=False)
       embed.set_thumbnail(url=message.guild.icon_url)
       await message.channel.send(embed=embed)
    if message.content == (";투표"):
        vote = message.content[4:].split("/")
        await client, message(message.channel, vote[0])
        for i in range(1, len(vote)):
            choose = await client.send_message(message.channel, vote[i])
            await client.add_reaction(choose, "👍")
    if message.content == (";초대"):
        await message.channel.send ("https://discord.com/api/oauth2/authorize?client_id=757426337479786577&permissions=8&scope=bot")
    if message.content == (";hellothisisverification"):
        await message.channel.send ("Hestia#1234")
    if message.content == (";계산 더하기"):
        await message.channel.send ("첫번째 숫자를 입력해주세요:")
        a = message.content
        await message.channel.send ("두번째 숫자를 입력해주세요:")
        b = message.content
        await message.channel.send (a+b)
    if message.content == (";프로필"):
        embed=discord.Embed(title=message.author.name+"님의 프사!", description=message.author.name+"님의 프사입니다!", color=0x00ccff)
        embed.set_image(url=message.author.avatar_url)
        await message.channel.send(embed=embed)
    if message.content.startswith(';남프로필'):
        profile = await client.fetch_user(int(message.content[6:]))
        embed=discord.Embed(title=profile.name+"님의 프사!",description='', color=0x00ccff)
        embed.set_image(url=profile.avatar_url)
        await message.channel.send(embed=embed)
    if message.content == (";티켓"):
        ticket = message
        auth = message.author.name
        await (ticket).delete()
        await message.guild.create_text_channel('Support-'+message.author.name)
    if message.content == (";티켓 삭제"):
        if message.author.guild_permissions.administrator:
            await message.channel.delete()
        else:
            await message.channel.send("저기... 관리권한이 없는 것 같아요...")
    if message.content == (";DM"):
        cha = await create_DM_channel 
    if message.content == (";코로나테스트"):
        html = requests.get("http://ncov.mohw.go.kr/").text
        soup = BeautifulSoup(html, 'html.parser')
        soup.select('span.data')[0].text
    if message.content.startswith(';남정보'):
        user = await client.fetch_user(int(message.content[5:]))
        date = datetime.datetime.utcfromtimestamp(((int(user.id) >> 22) + 1420070400000) / 1000)
        roles = [role for role in message.author.roles]
        embed=discord.Embed(title=user.name+"님의 정보", description=user.name+"님의 정보를 보여드립니다", color=0x00ffee)
        embed.add_field(name="디스코드 닉네임", value=user, inline=True)
        embed.add_field(name="서버 닉네임", value=user.display_name, inline=False)
        embed.add_field(name="가입일", value=str(date.year)+"년"+str(date.month)+"월"+str(date.day)+"일", inline=False)
        embed.add_field(name="아이디", value=user.id, inline=False)
        embed.add_field(name="봇 여부", value=user.bot, inline=False)
        embed.add_field(name="역할", value="못해먹겠다", inline=False)
        embed.set_thumbnail(url=user.avatar_url)
        await message.channel.send(embed=embed)
    if message.content.startswith(';찬반투표'):
        subject = message.content [6:]
        embed=discord.Embed(title="찬반투표!", description="찬성은 따봉을 반대는 싫어요 반응을 눌러주세요!", color=0x0088ff)
        embed.add_field(name="주제", value=subject, inline=False)
        msg = await message.channel.send(embed=embed)
        await msg.add_reaction("👍")
        await msg.add_reaction("👎")
    if message.content.startswith(";개표"):
        voting = message.content [4:]

    if message.content.startswith(";청소"):
        if message.author.guild_permissions.administrator:
            number = int(message.content.split(" ")[1])
            await message.delete()
            await message.channel.purge(limit=number)
            a = await message.channel.send(f"WA! 봇이 메시지 {number}개를 제대로 삭제했어요!")
            await asyncio.sleep(2)
            await a.delete()
        else:
            await message.channel.send(f"저런... {message.author.mention}님은 관리권한이 없어요")
    if message.content.startswith(";타이머"):
        time = int(message.content[5:])
        await message.channel.send(f"{time}초 타이머는 시작되었다!")
        await asyncio.sleep(time)
        await message.channel.send(f"{message.author.mention}님님!!! 일어나세요!!! 벌써 {time}초 타이머가 끝났어요!!!")
    if message.content.startswith(";채널메시지"):
        await client.wait_until_ready()
        ch = client.get_channel(int(message.content[7:25]))
        msg = message.content[26:]
        await ch.send(f"{msg}\n```{message.author.name}({message.author.id})님에 의해 만들어진 채널메시지!```")
    if message.content.startswith(";건의"):
        sup = message.content[4:]
        s = client.get_channel(786801883155005504)
        await s.send(sup)
    if message.content.startswith(";밴"):
        if message.author.guild_permissions.administrator:
            user = await client.fetch_user(int(message.content[3:21]))
            reason = message.content[22:]
            await message.guild.ban(user, reason=reason)
            await message.channel.send(f"{user.mention} 밴 성공! 사유:{reason}")
        else:
            await message.channel.send(f"저런... {message.author.mention}님은 관리권한이 없어요...")
    if message.content.startswith(";킥"):
        if message.author.guild_permissions.administrator:
            user = await client.fetch_user(int(message.content[3:21]))
            reason = message.content[22:]
            await message.guild.kick(user)
            await message.channel.send(f"{user.mention} 킥 성공! 사유:{reason}")
        else:
            await message.channel.send(f"저런... {message.author.mention}님은 관리권한이 없어요...")
    if message.content.startswith(";언밴"):
        if message.author.guild_permissions.administrator:
            user = await client.fetch_user(int(message.content[4:22]))
            reason = message.content[23:]
            await message.guild.unban(user)
            await message.channel.send(f"{user.mention} 언밴 성공! 사유:{reason}")
        else:
            await message.channel.send(f"저런... {message.author.mention}님은 관리권한이 없어요...")
    if message.content.startswith(";뮤트역할"):
        mute = message.content[6:]
        await message.channel.send(f"이제 이 서버에서 뮤트 역할은 {mute}입니다!")
    if message.content.startswith(";뮤트"):
        if message.author.guild_permissions.administrator:
            user = await client.fetch_user(int(message.content[4:22]))
            reason = message.content[23:]
            await add_roles(get(message.guild.roles, name = mute))
    if message.content.startswith(";핑"):
        lan = client.latency
        if lan < 200:
            await message.channel.send ("🏓 퐁! " + str(round(lan * 1000)) + "ms!\n상태: 좋음\nhttps://media.discordapp.net/attachments/791142632751497216/795918702645739560/unknown.png")
        if 200 <= lan >= 400:
            await message.channel.send ("🏓 퐁! " + str(round(lan * 1000)) + "ms!\n상태: 양호\nhttps://media.discordapp.net/attachments/791142632751497216/795919003142193182/unknown.png")
        if 401 <= lan >= 600:
            await message.channel.send ("🏓 퐁! " + str(round(lan * 1000)) + "ms!\n상태: 불안정\nhttps://media.discordapp.net/attachments/791142632751497216/795919354382385162/unknown.png")
        if 601 <= lan:
            await message.channel.send ("🏓 퐁! " + str(round(lan * 1000)) + "ms!\n상태: 나쁨\nhttps://media.discordapp.net/attachments/791142632751497216/795919518739464233/unknown.png")
    if message.content.startswith(";퐁"):
        await message.channel.send ("🏓 핑? " + str(round(client.latency * 1000)) + "ms...?!")
    if message.content == (";야짤"):
        await message.channel.send ("이거나 보세요 https://cdn.discordapp.com/attachments/770588006540509215/787905766388137984/kakaotalk_1592296118990.mp4 (중요! 관리자분들! 보기나 하시고 검열하세요!)")
    if message.content == (";활동"):
        embed=discord.Embed(title='테스트중')
        embed.add_field(name='Test?', value=message.author.activity)
        await message.channel.send(embed=embed)
    if message.content == (";차"):
        await message.channel.send("누군가의 속성강의 https://cdn.discordapp.com/attachments/770588006540509215/785439673350225930/kakaotalk_1607333676319.mp4")
    if message.content == ("왓알유 바보"):
        what = await client.fetch_user(int(617286714615922698))
        await message.channel.send(f"{what.mention}")
        await message.channel.send("왓알유 바보")
    if message.content == ("왓얼유 바보"):
        what = await client.fetch_user(int(617286714615922698))
        await message.channel.send(f"{what.mention}")
        await message.channel.send("왓얼유 바보")
    if message.content.startswith(";대신멘션"):
        user = await client.fetch_user(int(message.content[6:]))
        await message.delete()
        await message.channel.send(f"<@!{user.id}>님! {message.author.name}({message.author.id})님이 멘션하셨어요!")
    if message.content.startswith(';DM'):
        dmer = await client.fetch_user(int(message.content[4:22]))
        msgg = message.content[23:]
        if dmer.dm_channel:
            await message.author.dm_channel.send(f"{dmer.mention}님, {message.author.name}님이 이렇게 전해달래요! ```{msgg}```")
            await message.channel.send(f"{message.author.mention}님, {dmer.name}님께 DM으로 메시지를 전송했어요! ")
        else: # 아니라면
            if dmer.dm_channel is None:
                channel = await dmer.create_dm()
                await channel.send(f"{dmer.name}님, {message.author.name}님이 이렇게 전해달래요! ```{msgg}```")
                await message.channel.send(f"{message.author.mention}님, {dmer.name}님께 메시지를 전송냈어요!")


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
