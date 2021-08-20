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
    return DiceBot.stats_text(parsable, 6)


if __name__ == '__main__':
    app.run()
