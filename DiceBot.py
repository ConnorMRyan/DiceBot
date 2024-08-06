import random
import numpy


def roll(num_dice, die_sides, mod) -> int:
    die_total = 0
    for x in range(num_dice):
        die_total = die_total + random.randint(1, die_sides)

    return die_total + mod


def roll_by_array(die_array) -> int:
    return roll(int(die_array[0]), int(die_array[1]), int(die_array[2]))


def six_sided_stats(die_array):
    values = []
    for x in range(100):
        values.append(roll_by_array(die_array))

    perc_array = numpy.percentile(values, [5, 30, 45, 55, 70, 95])
    one_perc = round(perc_array[0])
    two_perc = round(perc_array[1])
    three_perc = round(perc_array[2])
    four_perc = round(perc_array[3])
    five_perc = round(perc_array[4])
    six_perc = round(perc_array[5])

    return f"1|{one_perc} \n2|{two_perc} \n3|{three_perc} \n4|{four_perc} \n5|{five_perc} \n6|{six_perc}"


def twenty_sided_stats(die_array):
    values = []
    for x in range(1000):
        values.append(roll_by_array(die_array))

    perc_array = numpy.percentile(values, range(5, 100, 5))
    return perc_array


def n_sided_stats(num_sides, die_array):
    values = []
    val_array = []
    if num_sides % 2 == 1:
        val_array.append(50)
        div_step = int(50 / ((num_sides - 1) / 2))
        for n in range(int((num_sides - 1) / 2)):
            n_val_pos = 50 + (div_step * (n + 1))
            n_val_neg = 50 - (div_step * (n + 1))
            val_array.append(n_val_pos)
            val_array.append(n_val_neg)

    else:
        div_step = int(50 / (num_sides / 2))
        for n in range(int(num_sides / 2)):
            n_val_pos = 50 + (div_step * (n + 1))
            n_val_neg = 50 - (div_step * (n + 1))
            val_array.append(n_val_pos)
            val_array.append(n_val_neg)

    for die_rolls in range(1000):
        values.append(roll_by_array(die_array))
    val_array.sort()
    perc_array = numpy.percentile(values, val_array)
    return [perc_array, num_sides]


def parse_text(text: str):
    stripped_text = ''.join(text.split())
    print(stripped_text)
    dice_strings = stripped_text.split(';')
    die_values = []
    for each_dice in dice_strings:
        if ":" in each_dice:
            dt_split = each_dice.split(':')
            damage_type = dt_split[1]
            original_roll = dt_split[0]
        else:
            original_roll = each_dice
            damage_type = ""
        die_split = original_roll.split('d')
        num_die = die_split[0]

        if "+" in die_split[1]:
            rest = die_split[1].split("+")
            die_sides = rest[0]
            mod = rest[1]

        elif "-" in die_split[1]:
            rest = die_split[1].split("-")
            die_sides = rest[0]
            mod = '-' + rest[1]

        else:
            die_sides = die_split[1]
            mod = '0'
        die_values.append([[num_die, die_sides, mod], original_roll, damage_type])

    return die_values


def parse_single(text):
    return


def parse_die(text, split):
    splits = text.split(split)
    return splits


def stats_text(parsable_text, sides):
    returnable = []
    parsed_text = parse_text(parsable_text)
    for x in parsed_text:
        stats = n_sided_stats(sides, x[0])
        die_array = [x[2], [], x[1]]
        for z in range(stats[1]):
            die_array[1].append(int(stats[0][z]))

        returnable.append(die_array)

    return returnable

