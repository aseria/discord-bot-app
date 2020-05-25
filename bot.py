from discord.ext import commands
from setting import setting
import random

bot = commands.Bot(command_prefix='$')

game_set = set()

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))


@bot.command()
async def 퇴사(ctx):
    await ctx.send('하세요')

@bot.command()
async def 골라줘(ctx, *args):
    picked = random.choice(args)
    await ctx.send(picked)

@bot.command()
async def 보여줘(ctx):
    await ctx.send(f'현재 게임리스트는 [{", ".join(game_set)}] 입니다.')

@bot.command()
async def 추가(ctx, *add_game):
    game_set.update(add_game)
    await ctx.send(f'게임 {",".join(add_game)} 가 추가되었습니다. \n현재 게임 리스트 : [{",".join(game_set)}]')

@bot.command()
async def 삭제(ctx, *deleted):
    removed = not_removed = []
    for dg in deleted:
        if dg in game_set:
            game_set.remove(dg)
            removed.append(dg)
        else:
            not_removed.append(dg)
    await ctx.send(f'게임 [{",".join(removed)}] 가 삭제되었습니다.')

@bot.command()
async def 오늘뭐할까(ctx):

    picked = ''.join(random.sample(game_set, 1)) if len(game_set) > 0 else '게임리스트가 비어있습니다.'
    await ctx.send(f'오늘은 {picked} 를 하십시오')


@bot.command()
async def 도움말(ctx):
    r = '아래와 같이 사용할 수 있습니다. \n' \
        '모든 게임리스트는 띄어쓰기를 지양해 주십시오\n\n' \
        '게임 추가 : $추가 {게임리스트} \n' \
        '게임 리스트는 쉼표로 구별하여 여러개를 입력할 수 있습니다.' \
        ' ex) $추가 트리키타워, 풀메탈퓨리, 티켓투라이드 \n\n' \
        '게임 삭제 : $삭제 {게임리스트} \n' \
        '게임 리스트는 쉼표로 구별하여 여러개를 입력할 수 있습니다. 리스트에 있는 게임만 지워집니다' \
        ' ex) $삭제 트리키타워, \n\n' \
        '게임 목록 조회 : $보여줘  \n' \
        '현재 저장된 게임리스트를 보여줍니다\n\n' \
        '게임 선택 : $오늘뭐할까 \n' \
        '저장된 게임 목록에서 오늘 할 게임을 골라줍니다.\n\n' \
        '바로 선택 : $골라줘 스타 워크래프트 디아블로\n' \
        ' ex) $골라줘 스타 워크래프트 디아블로 \n' \
        '게임 목록과 상관없이 보낸 리스트에서 랜덤으로 하나를 선택해줍니다.'
    await ctx.send(r)

bot.run(setting['discord-app']['token'])