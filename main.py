import discord
import asyncio
import datetime
import requests
from bs4 import BeautifulSoup
from discord.ext import commands
import ast
import traceback
import random
import json
import os
from dhooks import Webhook
INTENTS = discord.Intents.all()

client = discord.Client(intents=INTENTS)
token = 'TOKEN'

@client.event
async def on_ready():
    print('삐리릭 봇이 켜졌다')
    print(client.user.name)
    print(client.user.id)
    print('====================================')
    user = len(client.users)
    server = len(client.guilds)
    message = ["안녕하세요!", "Hestia#1234님이 제작하신 봇", str(user) + "명이 저와 놀고있어요!", str(server) + "개의 서버에서 안전하게 보관되고 있어요!", ";도움으로 저의 명령어를 알아보세요!"]
    while True:
        await client.change_presence(status=discord.Status.online, activity=discord.Game(message[0]))
        message.append(message.pop(0))
        await asyncio.sleep(4)

@client.event
async def on_message(message):
    user = message.author
    bot = str(user.bot)
    if bot == "False":
        if message.content == ';도움':
            embed=discord.Embed(title="도움말", description="접두사는 ``;``입니다", color=0x00fffb)
            embed.add_field(name="핑", value="핑을 체크합니다(자세하지 않아요)", inline=True)
            embed.add_field(name="내정보", value="유저님의 정보를 알려드립니다", inline=True)
            embed.add_field(name="서버 정보", value="서버의 정보를 알려드립니다", inline=True)
            embed.add_field(name="초대", value="봇의 초대링크를 드립니다!", inline=True)
            embed.add_field(name="프로필", value="당신의 프로필을 보여드립니다!", inline=True)
            embed.add_field(name="남프로필 (id 입력)", value="그 id를 가진 사람의 프로필을 보여드립니다!", inline=True)
            embed.add_field(name="티켓", value="티켓 채널을 만듭니다!", inline=True)
            embed.add_field(name="티켓 삭제", value="티켓 채널을 삭제합니다!(관리자 명령어)", inline=True)
            embed.add_field(name="찬반투표 (주제)", value="찬반투표를 만듭니다!", inline=True)
            embed.add_field(name="남정보 (id 입력)", value="그 id의 주인의 정보를 찾습니다!", inline=True)
            embed.add_field(name="청소 (갯수)", value="갯수만큼 메시지를 청소합니다!(관리자 명령어)", inline=True)
            embed.add_field(name="밴 (유저 id)", value="그 id를 가진 사람을 밴합니다!(관리자 명령어)", inline=True)
            embed.add_field(name="언밴 (유저 id)", value="그 id를 가진 유저를 언밴합니다!", inline=True)
            embed.add_field(name="킥 (유저 id)", value="그 id를 가진 사람을 킥합니다!(관리자 명령어)", inline=True)
            embed.add_field(name="타이머 (시간)", value="시간을 입력한만큼 기다렸다가 그 시간이 지나면 멘션해드립니다!", inline=True)
            embed.add_field(name="채널메시지 (채널 id) (보낼 메시지)", value="그 id를 가진 채널에 입력한 메시지를 보냅니다!", inline=True)
            embed.add_field(name="건의 (건의할 것)", value="건의할 것을 개발자 서버에 보냅니다!", inline=True)
            embed.add_field(name="대신멘션 (유저 id)", value="멘션하기 쑥쓰러우실 때 사용하세요!", inline=True)
            embed.add_field(name="DM (유저 id) (보낼 메시지)", value="그 id를 가진 유저에게 DM을 보냅니다! (봇하고 같이 있는 서버가 1개 이상 있어야함)", inline=True)
            embed.add_field(name="주사위", value="1~6중에서 숫자 하나를 골라드려요!", inline=True)
            embed.add_field(name="가위바위보 (가위나 바위나 보)", value="UV Bot와 가위바위보 해요!", inline=True)
            embed.add_field(name="따라해 (메시지)", value="UV Bot이 메시지를 따라해요!", inline=True)
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
            bot = str(user.bot)
            if bot == "True":
                bot = "봇"
            else:
                bot = "사람"
            embed.add_field(name="봇 여부", value=f"{bot}", inline=False)
            embed.add_field(name="역할", value=" ".join([role.mention for role in roles]), inline=False)
            if message.author.guild_permissions.administrator:
                admin = "O"
            else:
                admin = "X"
            embed.add_field(name="관리자 여부", value=f"{admin}", inline=False)
            sta = str(message.author.status)
            if sta == "online":
                status = "온라인 🟢"
            elif sta == "dnd":
                status = "다른 용무 중 ⛔"
            elif sta == "idle":
                status = "자리 비움 🟡"
            elif sta == "offline":
                status = "오프라인 ⚪"
            embed.add_field(name="상태", value=f"{status}", inline=False)
            act = str(message.author.activity)
            if act == "None":
                act = "활동이 없습니다"
            else:
                act = (message.author.activity)
            embed.add_field(name="활동", value=f"{act}", inline=False)
            jubseok = message.guild.get_member(message.author.id).is_on_mobile()
            if jubseok == True:
                jubseok = "핸드폰"
            else:
                jubseok = "PC"
            embed.add_field(name="접속 기기", value=f"{jubseok}", inline=False)
            embed.set_thumbnail(url=message.author.avatar_url)
            embed.set_footer(text=f"요청자: {message.author.name}, Developer: Dev. Hestia#5444")
            await message.channel.send(embed=embed)
        if message.content == ";서버 정보":
            embed=discord.Embed(title=message.guild.name+" 서버의 정보", description=message.guild.name+" 서버의 정보를 보여드립니다", color=0x00ffee)
            embed.add_field(name="서버 이름", value=message.guild.name, inline=True)
            embed.add_field(name="서버 인원", value=message.guild.member_count, inline=False)
            embed.add_field(name="서버 채널 수", value="테스트중", inline=False)
            embed.add_field(name="서버 아이디", value=message.guild.id, inline=False)
            embed.add_field(name="서버 소유자", value=message.guild.owner.name, inline=False)
            boan = str(message.guild.verification_level)
            if boan == "none":
                boan = "없어요!(아무런 제한이 없어요!)"
            elif boan == "low":
                boan = "낮아요!(이메일이 인증된 계정이어야 해요!)"
            elif boan == "medium":
                boan = "보통이예요!(계정이 만들어진지 5분이 지나야해요!)"
            elif boan == "high":
                boan = "높아요!(이 서버에 들어온 지 10분이 지난 뒤 활동이 가능해요!)"
            else:
                boan = "매우 높아요!(전화번호를 인증한 계정이어야 해요!)"
            embed.add_field(name="보안 레벨", value=f"{boan}", inline=False)
            embed.add_field(name="서버 부스트 횟수", value=message.guild.premium_subscription_count, inline=False)
            embed.add_field(name="서버 시스템 채널", value=message.guild.system_channel, inline=False)
            booster = str(message.guild.premium_subscribers)
            embed.add_field(name="서버 부스터", value=f"{booster}", inline=False)
            region = str(message.guild.region)
            if region == "brazil":
                region = "브라질"
            elif region == "europe":
                region = "유럽권"
            elif region == "hong-kong":
                region = "홍콩"
            elif region == "india":
                region = "인도"
            elif region == "japan":
                region = "일본"
            elif region == "russia":
                region = 러시아
            elif region == "singapore":
                region = "싱가포르"
            elif region == "south-africa":
                region = "남아공"
            elif region == "south-korea":
                region = "한국"
            elif region == "sydney":
                region = "호주"
            elif region == "us-central" or "us-east" or "us-south" or "us-west":
                region = "미국"
            else:
                region = "기타"
            embed.add_field(name="국적", value=f"{region}")
            embed.set_thumbnail(url=message.guild.icon_url)
            await message.channel.send(embed=embed)
        if message.content.startswith(";투표"):
            vote = message.content[4:].split(" ")
            await message.channel.send("투표")
            await message.channel.send("주제:" + vote[0])
            for i in range(1, len(vote)):
                choose = await message.channel.send("```" + vote[i] + "```")
                await choose.add_reaction('👍')
        if message.content == (";초대"):
            await message.channel.send ("https://discord.com/api/oauth2/authorize?client_id=757426337479786577&permissions=8&scope=bot")
        if message.content == (";hellothisisverification"):
            await message.channel.send ("Hestia#5444")
        if message.content.startswith(";계산 더하기"):
            yes = message.content[8:].split(" ")
            a = int(yes[0])
            b = int(yes[1])
            await message.channel.send(a+b)
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
            await message.guild.create_text_channel(f'Support-{message.author.name}')
        if message.content == (";티켓 삭제"):
            if message.author.guild_permissions.administrator:
                embed=discord.Embed(title="정말 이 티켓을 삭제하시겠어요?", description="이 티켓을 삭제하신다면 다시는 기록을 보지 못하게 되요... 그래도요?")
                user = message.author
                embed=await message.channel.send(embed=embed)
                await embed.add_reaction("👍")
                await embed.add_reaction("👎")
                heyhey = str(user.bot)
                if heyhey == "True":
                    return
                else:
                    @client.event
                    async def on_reaction_add(reaction, user):
                        if reaction.emoji == ("👍"):
                            await message.channel.delete()
                        if reaction.emoji == ("👎"):
                            await message.channel.send("티켓 삭제를 취소하셨습니다")
            else:
                await message.channel.send("저기... 관리권한이 없는 것 같아요...") 
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
            embed.set_thumbnail(url=message.author.avatar_url)
            await message.channel.send(embed=embed)
            embed.set_thumbnail(url=user.avatar_url)
            await message.channel.send(embed=embed)
        if message.content.startswith(';찬반투표'):
            subject = message.content [6:]
            embed=discord.Embed(title="찬반투표!", description="찬성은 따봉을 반대는 싫어요 반응을 눌러주세요!", color=0x0088ff)
            embed.add_field(name="주제", value=subject, inline=False)
            msg = await message.channel.send(embed=embed)
            await msg.add_reaction("👍")
            await msg.add_reaction("👎")
        if message.content.startswith(";청소"):
            if message.content == (";청소"):
                await message.channel.send("지금 저하고 뭐하자는 거죠? ``;청소 (숫자)`` 이렇게 쓰셔야죠!!!")
            else:
                if message.author.guild_permissions.administrator or message.author.id == (681348070260211713):
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
            s = client.get_channel(798089970896076800)
            await message.channel.send("건의 발송 성공!")
            await s.send(sup)
            await s.send(f"By <@!{message.author.id}>")
        if message.content.startswith(";밴"):
            if message.author.guild_permissions.administrator:
                user = await client.fetch_user(int(message.content[3:21]))
                reason = message.content[22:]
                await message.guild.ban(user, reason=reason)
                embed=discord.Embed(title=f"{user.name} 밴 성공!", description=f"{user.mention}를 성공적으로 밴하였습니다!", color=0x1081b1)
                embed.add_field(name="유저 이름", value=f"{user.mention}", inline=False)
                embed.add_field(name="처리자", value=f"{message.author.mention}", inline=True)
                embed.add_field(name="사유", value=f"{reason}", inline=False)
                await message.channel.send(embed=embed)
            else:
                await message.channel.send(f"저런... {message.author.mention}님은 관리권한이 없어요...")
        if message.content.startswith(";킥"):
            if message.author.guild_permissions.administrator:
                user = await client.fetch_user(int(message.content[3:21]))
                reason = message.content[22:]
                await message.guild.kick(user)
                embed=discord.Embed(title=f"{user.mention} 킥 성공!", description=f"{user.mention}를 성공적으로 킥하였습니다!", color=0x1081b1)
                embed.add_field(name="유저 이름", value=f"{user.mention}", inline=False)
                embed.add_field(name="처리자", value=f"{message.author.mention}", inline=True)
                embed.add_field(name="사유", value=f"{reason}", inline=False)
            else:
                await message.channel.send(f"저런... {message.author.mention}님은 관리권한이 없어요...")
        if message.content.startswith(";언밴"):
            if message.author.guild_permissions.administrator:
                user = await client.fetch_user(int(message.content[4:22]))
                reason = message.content[23:]
                await message.guild.unban(user)
                embed=discord.Embed(title=f"{user.mention} 언밴 성공!", description=f"{user.mention}를 성공적으로 언밴하였습니다!", color=0x1081b1)
                embed.add_field(name="유저 이름", value=f"{user.mention}", inline=False)
                embed.add_field(name="처리자", value=f"{message.author.mention}", inline=True)
                embed.add_field(name="사유", value=f"{reason}", inline=False)
            else:
                await message.channel.send(f"저런... {message.author.mention}님은 관리권한이 없어요...")
        if message.content.startswith(";뮤트"):
            if message.author.guild_permissions.administrator:
                user = await client.fetch_user(int(message.content[4:22]))
                role = discord.utils.get(message.guild.roles, name="Mute")
                await add_roles(user, role)
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
        if message.content == (";차"):
            await message.channel.send("누군가의 속성강의 https://cdn.discordapp.com/attachments/770588006540509215/785439673350225930/kakaotalk_1607333676319.mp4")
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
            else:
                if dmer.dm_channel is None:
                    channel = await dmer.create_dm()
                    await channel.send(f"{dmer.name}님, {message.author.name}님이 이렇게 전해달래요! ```{msgg}```")
                    await message.channel.send(f"{message.author.mention}님, {dmer.name}님께 메시지를 전송냈어요!")
        if message.content.startswith("봇정보"):
            users = len(client.users)
            servers = len(client.guilds)
            await message.channel.send(f"봇이 있는 길드 수: {servers}, 봇을 쓰는 유저 수: {users}")
        if message.content.startswith(';공지'):
            admin = message.author.id
            if admin == 681348070260211713:
                content = message.content[4:]
                msgembed = discord.Embed(title='공지', description=content, color=0x00ffff)
                msgembed.set_footer(text="Developer: Hestia")
                msgembed.set_thumbnail(url="https://media.discordapp.net/attachments/790815303314964480/797010814766809108/UV.PNG")
                for i in client.guilds:
                    for j in i.text_channels:
                        if ('공지' in j.name) and ('봇' in j.name):
                            try:
                                await j.send(embed=msgembed)
                            except Exception as a:
                                await message.channel.send(f'{i.name} 서버의 {j.name} 채널에 공지를 보내기 실패했습니다.')
                                await message.channel.send(a)
                            break
            else:
                await message.channel.send("봇 개발자가 아니십니다")
        if message.content.startswith(";따라해"):
            tada = message.content[5:]
            embed=discord.Embed(title=f"{message.author.name}님의 협박(?)에 의한 메시지!", description=" ", color=0x00ff33)
            embed.add_field(name=f"{tada}", value="여러분 협박은 위험하답니다", inline=True)
            embed.set_footer(text=f"요청자: {message.author.name}")
            await message.channel.send(embed=embed)
        if message.content.startswith(f';eval'):

            def insert_returns(body): # [1]
            # insert return stmt if the last expression is a expression statement
                if isinstance(body[-1], ast.Expr):
                    body[-1] = ast.Return(body[-1].value)
                    ast.fix_missing_locations(body[-1])

            # for if statements, we insert returns into the body and the orelse
                if isinstance(body[-1], ast.If):
                    insert_returns(body[-1].body)
                    insert_returns(body[-1].orelse)

            # for with blocks, again we insert returns into the body
                if isinstance(body[-1], ast.With):
                    insert_returns(body[-1].body)

            cmd = message.content.split(" ")[1:]
            _cmd = cmd
            print(cmd)
            msg = await message.channel.send(embed = discord.Embed(title='Code Compiling').add_field(
                name='📥 Input',
                value=f'```py\n{cmd}```',
                inline=False
            ))
            await asyncio.sleep(1.5)

        #banword checking
            banword = ['token', 'file=', 'file ='] 
        # 본인이 원하는걸 넣으심 됩니다  # banword에 있는 단어가 있으면 return None으로 처리됩니다.
        
            if cmd in banword: # [2]
                embed = discord.Embed(title='Code Compiling')
                embed.add_field(name='📥 Input', value=f'```py\n{_cmd}```', inline=False)
                embed.add_field(name = '📤 Output', value = f'`{cmd}`에는 eval에서 사용 금지된 단어가 포함되어 있습니다.')
                await msg.edit(embed=embed)
                await ctx.send(f'{ctx.message.content}는 사용 금지된 단어가 포함되어 있습니다.')
                return None # [3]
            else:
                try:
                    code = message.content[6:]
                    cmd = code
                    fn_name = "_eval_expr"
                    cmd = cmd.strip("` ")
                    # add a layer of indentation
                    cmd = "\n".join(f"    {i}" for i in cmd.splitlines())
                    # wrap in async def body
                    body = f"async def {fn_name}():\n{cmd}"
                    parsed = ast.parse(body)
                    body = parsed.body[0].body
                    insert_returns(body)
                    env = {
                        'client': client,
                        'discord': discord,
                        'message': message,
                        '__import__': __import__
                    }
                    exec(compile(parsed, filename="<ast>", mode="exec"), env)
                    result = (await eval(f"{fn_name}()", env))
                    embed=discord.Embed(title="실행 성공", colour=discord.Colour.green(), timestamp=message.created_at)
                    embed.add_field(name="`📥 Input (들어가는 내용) 📥`", value=f"```py\n{code}```", inline=False)
                    embed.add_field(name="`📤 Output (나오는 내용) 📤`", value=f"```py\n{result}```", inline=False)
                    embed.add_field(name="`🔧 Type (타입) 🔧`",value=f"```py\n{type(result)}```", inline=False)
                    embed.add_field(name="`🏓 Latency (지연시간) 🏓`",value=f"```py\n{str((datetime.datetime.now()-message.created_at)*1000).split(':')[2]}```", inline=False)
                    embed.set_footer(text=f"{message.author}, 코드 출처: Bainble0211#6109", icon_url=message.author.avatar_url)
                    await message.channel.send(embed=embed)
                except Exception as e:
                    await message.channel.send(f"{message.author.mention}, 실행 중 오류가 발생하였습니다.\n\n```py\n{e}```")
        if message.content.startswith(";주사위"):
            dice1 = discord.Embed(title="주사위의 결과는...과연?", description="1입니다!(운이 안좋네요...)")
            dice2 = discord.Embed(title="주사위의 결과는...과연?", description="2입니다!(운이 그럭저럭하네요...)")
            dice3 = discord.Embed(title="주사위의 결과는...과연?", description="3입니다!(운이 조금 좋네요)")
            dice4 = discord.Embed(title="주사위의 결과는...과연?", description="4입니다!(오늘 운수가 좋을 것 같아요!)")
            dice5 = discord.Embed(title="주사위의 결과는...과연?", description="5입니다!(엄청 운이 좋은 것 같아요!)")
            dice6 = discord.Embed(title="주사위의 결과는...과연?", description="6입니다!(신이세요?)")
            dice1.set_thumbnail(url="https://media.discordapp.net/attachments/791142632751497216/796639189541191720/sunny.png")
            dice2.set_thumbnail(url="https://media.discordapp.net/attachments/791142632751497216/796639189541191720/sunny.png")
            dice3.set_thumbnail(url="https://media.discordapp.net/attachments/791142632751497216/796639189541191720/sunny.png")
            dice4.set_thumbnail(url="https://media.discordapp.net/attachments/791142632751497216/796639189541191720/sunny.png")
            dice5.set_thumbnail(url="https://media.discordapp.net/attachments/791142632751497216/796639189541191720/sunny.png")
            dice6.set_thumbnail(url="https://media.discordapp.net/attachments/791142632751497216/796639189541191720/sunny.png")
            dice_list = [dice1, dice2, dice3, dice4, dice5, dice6]
            dice = random.choice(dice_list)
            await message.channel.send(embed=dice)
        if message.content.startswith(";가위바위보"):
            what = message.content[7:]
            rock = f"{message.author.mention}님은 {what}를 내셨구요... 저는 바위를 냈어요!"
            scissors = f"{message.author.mention}님은 {what}를 내셨구요... 저는 가위를 냈어요!"
            paper = f"{message.author.mention}님은 {what}를 내셨구요... 저는 보를 냈어요!"
            whut = ['가위', '바위', '보']
            rsp = random.choice(whut)
            rsp2 = [rock, scissors, paper]
            if rsp == what:
                if what == "가위":
                    await message.channel.send(scissors)
                    await message.channel.send(f"저와 {message.author.mention}님은 비겼네요!")
                elif what == "바위":
                    await message.channel.send(rock)
                    await message.channel.send(f"저와 {message.author.mention}님은 비겼네요!")
                else:
                    if what == "보":
                        await message.channel.send(paper)
                        await message.channel.send(f"저와 {message.author.mention}님은 비겼네요!")
            if rsp != what:
                if what == "가위":
                    if rsp == "바위":
                        await message.channel.send(rock)
                        await message.channel.send(f"제가 {message.author.mention}님을 이겼네요!")
                    else:
                        if rsp == "보":
                            await message.channel.send(paper)
                            await message.channel.send(f"{message.author.mention}님이 저를 이겼네요!")
                elif what == "바위":
                    if rsp == "가위":
                        await message.channel.send(paper)
                        await message.channel.send(f"제가 {message.author.mention}님을 이겼네요!")
                    else:
                        if rsp == "보":
                            await message.channel.send(scissors)
                            await message.channel.send(f"{message.author.mention}님이 저를 이겼네요!")
                elif what == "보":
                    if rsp == "바위":
                        await message.channel.send(rock)
                        await message.channel.send(f"제가 {message.author.mention}님이 저를 이겼네요!")
                    else:
                        if rsp == "가위":
                            await message.channel.send(scissors)
                            await message.channel.send(f"{message.author.mention}님을 이겼네요!")
                else:
                    await message.channel.send("가위, 바위, 보 중에서 하나를 선택하셔야죠 ㅡㅡ")
        if message.content.startswith(";패치노트"):
            embed=discord.Embed(title="UV Bot 0.0.2 패치노트", description="UV Bot의 0.0.2 버전 패치노트", color=0x00e1ff)
            embed.add_field(name="공지 기능", value="봇 공지를 들으실 수 있습니다", inline=False)
            embed.add_field(name="따라해 기능", value="봇이 유저님의 메시지를 따라합니다", inline=True)
            embed.add_field(name="주사위 기능", value="봇이 주사위를 돌립니다", inline=True)
            embed.add_field(name="가위바위보 기능", value=";가위바위보 (가위 아니면 바위 아니면 보)를 치시면 가위바위보를 할 수 있습니다", inline=True)
            embed.add_field(name="패치노트 기능", value="이제 최신 버전의 패치 기능을 확인하실 수 있습니다", inline=True)
            embed.add_field(name="더하기 기능(beta)", value=";더하기 (숫자) (숫자)를 치시면 숫자를 더합니다", inline=True)
            embed.add_field(name="유저 정보 기능, 서버 정보 기능 업데이트", value="유저 정보에는 접속 기기 기능을, 서버 정보에는 서버 보안 레벨, 서버 국가를 보실 수 있습니다", inline=True)
            await message.channel.send(embed=embed)
        if message.content.startswith(";가입"):
            with open("sign_up.json") as json_file:
                json_data = json.load(json_file)
            if str(message.author.id) in json_data:
                embed=discord.Embed(title=f"{message.author.name}님, 뭔가 잘못되었어요...", description=f"{message.author.name}님은 이미 가입되어있어요...", color=0x00e1ff)
                await message.channel.send(embed=embed)
            else:
                if str(message.author.id) not in json_data:
                    json_data[str(message.author.id)] = "100"
                    with open("sign_up.json", "w", encoding="utf-8") as make_file:
                        json.dump(json_data, make_file, indent="\t")
                    embed=discord.Embed(title=f"성공적으로 가입 성공", description=f"와! {message.author.name}은 가입에 성공하셨어요! 가입 기념으로 100포인트를 받으셨어요!", color=0x00ccff)
                    await message.channel.send(embed=embed)
        if message.content.startswith(";내포인트"):
            with open("sign_up.json") as json_file:
                json_data = json.load(json_file)
            if str(message.author.id) in json_data:
                embed=discord.Embed(title=f"{message.author.name}님의 누적 포인트", color=0x00ccff)
                embed.add_field(name="가지고 계신 포인트", value=f"{json_data[str(message.author.id)]}포인트")
                await message.channel.send(embed=embed)
            else:
                embed=discord.Embed(title=f"{message.author.name}님은 가입되지 않은 사용자입니다!", description=f"{message.author.name}님, ``;가입`` 커맨드로 먼저 가입해주세요!", color=0x00ccff)
                await message.channel.send(embed=embed)
        if message.content.startswith(";도박"):
            what = message.content[4:]
            if what == "올인":
                with open("sign_up.json") as json_file:
                    json_data = json.load(json_file)
                if str(message.author.id) in json_data:
                    dobak_list=["success", "fuck"]
                    dobak=random.choice(dobak_list)
                    if dobak == "success":
                        json_data[str(message.author.id)] = str(int(json_data[str(message.author.id)]) * 2)
                        with open("sign_up.json", "w", encoding="utf-8") as make_file:
                            json.dump(json_data, make_file, indent="\t")
                            await message.channel.send("샌즈")
                    elif dobak == "fuck":
                        json_data[str(message.author.id)] = "0"
                        with open("sign_up.json", "w", encoding="utf-8") as make_file:
                            json.dump(json_data, make_file, indent="\t")
                            await message.channel.send("저런")
                else:
                    embed=discord.Embed(title=f"{message.author.name}님은 가입되지 않은 사용자입니다!", description=f"{message.author.name}님, ``;가입`` 커맨드로 먼저 가입해주세요!", color=0x00ccff)
                    await message.channel.send(embed=embed)
            else:
                if int(what) > int(json_data[str(message.author.id)]):
                    await message.channel.send("돈이 없으시네요... ``;일`` 커맨드로 돈을 벌어주세요!")
                else:
                    with open("sign_up.json") as json_file:
                        json_data = json.load(json_file)
                    if str(message.author.id) in json_data:
                        dobak_list=["success", "fuck"]
                        dobak=random.choice(dobak_list)
                        if dobak == "success":
                            json_data[str(message.author.id)] = int(what) * 2 + int(json_data[str(message.author.id)])
                            with open("sign_up.json", "w", encoding="utf-8") as make_file:
                                json.dump(json_data, make_file, indent="\t")
                                await message.channel.send("샌즈")
                        elif dobak == "fuck":
                            json_data[str(message.author.id)] = int(json_data[str(message.author.id)]) - int(what)
                            with open("sign_up.json", "w", encoding="utf-8") as make_file:
                                json.dump(json_data, make_file, indent="\t")
                                await message.channel.send("저런")
        if message.content.startswith(";일"):
            point_list = list(range(101))
            random_point = (point_list)
            json_file={}
            json_data = json.loads(json_file)
            json_data = json.dumps(json_data["data"])
            json_data[str(message.author.id)] = str(int(json_data[str(message.author.id)])) + int(random_list)
            with open("sign_up.json", "w", encoding="utf-8") as make_file:
                json.dump(json_data, make_file, indent="\t")
                await message.channel.send("샌즈")
        if message.content.startswith(";서버이름"):
            if message.author.id == 681348070260211713:
                with open("guilds.txt", 'w', -1, "utf-8") as a:
                    a.write(str(client.guilds))
                file1 = discord.File("guilds.txt")
                await message.author.send(file=file1)
                os.remove("guilds.txt")
            else:
                await message.channel.send("봇 개발자만 가능합니다")
        if message.content.startswith(";웹훅"):
            msg1 = message.content[4:].split(" ")
            for i in range(1, len(msg1)):
                webhooking = msg1[0]
                msg = msg1[i]
                webhook = Webhook(webhooking)
                webhook.send(msg)
        if message.content.upper().startswith(";리로드"):
            await message.channel.send("테스트 ㅎ")
            await asyncio.sleep(0.5)
        if message.content.startswith(";테스트"):
            sansverygoodlikeit = await message.channel.send("이모티콘 샌즈")
            user = message.author
            bot = str(user.bot)
            await sansverygoodlikeit.add_reaction("👍")
            if bot == "False":
                @client.event
                async def on_reaction_add(reaction, user):
                    if reaction.emoji == ("👍"):
                        await sansverygoodlikeit.edit(content="관심 받아서 신난다 신나")
            elif bot == "True":
                return None
    else:
        return None

client.run(token)
