from flask import Flask
import DiceBot
import Spells

app = Flask(__name__)


@app.route('/dieroll/<parsable>')
def roll_die(parsable):
    parsed_text = DiceBot.parse_text(parsable)
    return_text = []
    for x in parsed_text:
        return_text.append(f"you rolled {x[1]} and got {DiceBot.roll_by_array(x[0])} {x[2]} damage")

    y = "<br>".join(return_text)
    return y


@app.route('/spell/cast/<spellname>/<level>')
def roll_spell(spellname, level):
    spell = Spells.get_spell(spellname, level)
    parsed_text = DiceBot.parse_text(spell)
    print(parsed_text)
    return f"You cast {spellname} at {level}{Spells.get_number_ending(level)} level: you deal " \
           f"{DiceBot.roll_by_array(parsed_text[0][0])} {parsed_text[0][2]} damage "


@app.route('/stats/<parsable>')
def six_stats(parsable):
    table = [build_table_base(6)]

    stats = DiceBot.stats_text(parsable, 6)
    for stat in stats:
        table.append(format_die_array(stat))

    return "".join(table)


@app.route('/stats/<sides>/<parsable>')
def table_test(sides, parsable):
    table = [build_table_base(sides)]

    n_stats = DiceBot.stats_text(parsable, int(sides))
    for die_stat in n_stats:
        table.append(format_die_array(die_stat))

    return "".join(table)


@app.route('/')
def hello():
    return "App is running."


def format_die_array(die_array):
    table = ["<tr>", f"<th>{die_array[2]}</th><th>{die_array[0]}</th>"]
    for n in range(len(die_array[1])):
        table.append(f"<th>{die_array[1][n]}")

    return "".join(table)


def build_table_base(sides):
    table = ["""<style>
        table, th, td {border: 1px solid black;}
        </style><table style="width:100%"><tr><th>ROLL</th><th>TYPE</th>"""]
    for n in range(int(sides)):
        table.append(f"<th>{n + 1}</th>")

    table.append("</tr>")
    return "".join(table)


if __name__ == '__main__':
    app.run()
