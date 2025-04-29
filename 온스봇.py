# pip install -U discord.py 로 설치해야 합니다.
import discord
from discord.ext import commands
from discord import app_commands

# 인텐트 설정 (메시지 내용 읽기)
intents = discord.Intents.default()
intents.message_content = True

# 봇 생성
bot = commands.Bot(command_prefix="!", intents=intents)

# 봇이 준비되었을 때 실행
@bot.event
async def on_ready():
    print(f'✅ 봇 {bot.user} 로그인 완료!')
    try:
        synced = await bot.tree.sync()  # Slash 명령어 서버 등록
        print(f'✅ Slash 명령어 {len(synced)}개 등록 완료!')
    except Exception as e:
        print(f'❌ Slash 명령어 등록 실패: {e}')

# !안녕 명령어
@bot.command()
async def 안녕(ctx):
    await ctx.send('안녕하세요! 저는 온스 봇입니다.')

@bot.tree.command(
    name="팀",
    description="배그 팀원을 모집합니다!"
)
@app_commands.describe(
    설명="모집 설명을 입력하세요 (예: 테이고 배린이 환영!)"
)
async def team(interaction: discord.Interaction, 설명: str):
    channel = interaction.channel
    category_name = channel.category.name if channel.category else "카테고리 없음"

    embed = discord.Embed(
        title="팀원 모집",
        description=f"{interaction.user.mention} 님이 팀원 모집 중입니다!",
        color=discord.Color.blue()
    )

    embed.add_field(name="설명", value=설명, inline=False)
    embed.set_footer(text="Team Finder 앱")

    await interaction.response.send_message(embed=embed)

bot.run('MTM2NjcxODE0NzA0NTg4ODA5MQ.GMPZAh.nzVEqwtPXrPm6qsoOdGkckUgu4427x0H9tyjO0')