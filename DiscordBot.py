import os
import random
import pokebase as pb
import DiceBot
import Spells
import asyncio
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')


@bot.command(name='cast_spell', help='Simulates casting a spell.')
async def cast_spell(ctx, spell_name: str, spell_level: int):
    spell = Spells.get_spell(spell_name, spell_level)
    parsed_text = DiceBot.parse_text(spell)
    print(parsed_text)
    message = f"```You cast {spell_name} at {spell_level}{Spells.get_number_ending(spell_level)} level: you deal " \
              f"{DiceBot.roll_by_array(parsed_text[0][0])} {parsed_text[0][2]} damage```"
    await ctx.send(message)


@bot.command(name='roll_dice', help='Simulates a dice roll')
async def roll_die(ctx, parsable_string: str):
    parsed_text = DiceBot.parse_text(parsable_string)
    return_text = ["```\n"]
    for x in parsed_text:
        return_text.append(f"you rolled {x[1]} and got {DiceBot.roll_by_array(x[0])} {x[2]} damage")
    return_text.append("```")
    y = "\n".join(return_text)
    await ctx.send(y)


@bot.command(name='randpoke', help='Responds with a picture of a pokemon')
async def pokemon(ctx):
    print(ctx.message.author.id)
    pokenum = random.randint(1, 898)
    if ctx.message.author.id == 120328178802622474:
        await ctx.send("https://raw.githubusercontent.com/"
                       f"PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/{197}.png")
    elif ctx.message.author.id == 168404138865065984:
        await ctx.send("https://raw.githubusercontent.com/"
                       f"PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/{pokenum}.png")
    else:
        await ctx.send("https://raw.githubusercontent.com/"
                       f"PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/{pokenum}.png")


async def timer(num_seconds):
    await asyncio.sleep(num_seconds)


@bot.command(name='timer', help='Sets a timer for X seconds')
async def time_wait(ctx, num_secs: int, alert: str):
    await timer(num_secs)
    await ctx.send(f'<@{ctx.message.author.id}> {alert}')


bot.run(TOKEN)
