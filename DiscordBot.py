import os
import DiceBot
import Spells
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


bot.run(TOKEN)
