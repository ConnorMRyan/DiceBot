from flask import Flask
import DiceBot

app = Flask(__name__)


@app.route('/dieroll/<parsable>')
def rolldie(parsable):
    parsed_text = DiceBot.parse_die(parsable)
    return_text = []
    for x in parsed_text:
        return_text.append(f"you rolled {x[1]} and got {DiceBot.roll_by_array(x[0])} {x[2]} damage")

    y = "  |  ".join(return_text)
    print(y)
    return y


@app.route('/stats/<sides>/<parsable>')
def n_stats(sides, parsable):
    return DiceBot.stats_text(parsable, int(sides))


@app.route('/stats/<parsable>')
def six_stats(parsable):
    print(DiceBot.stats_text(parsable, 6))
    return DiceBot.stats_text(parsable, 6)


@app.route('/tabletest/<sides>/<parsable>')
def table_test(sides, parsable):
    table = ["""<table style="width:100%"><tr><th>ROLL</th><th>TYPE</th>"""]
    for n in range(int(sides)):
        table.append(f"<th>{n + 1}</th>")

    table.append("</tr>")

    n_stats = DiceBot.stats_text(parsable, int(sides))
    for die_stat in n_stats:
        table.append("<tr>")
        table.append(f"<th>{die_stat[2]}</th><th>{die_stat[0]}</th>")
        for n in range(int(sides)):
            table.append(f"<th>{die_stat[1][n]}")
    returnable = "".join(table)
    return returnable


if __name__ == '__main__':
    app.run()
