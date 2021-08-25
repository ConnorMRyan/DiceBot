import requests as req


def get_spell(spell_name, level):
    spell = req.get("https://www.dnd5eapi.co/api/spells/" + spell_name)

    spell_json = spell.json()
    print(spell_json['damage'])
    try:
        return '' + spell_json['damage']['damage_at_slot_level'][f"{level}"] + ':' + \
               spell_json['damage']['damage_type']['name']
    except KeyError:
        return '0d0:null'


def get_number_ending(number):
    if (number == 1) | (number == '1'):
        return 'rst'
    elif (number == 2) | (number == '2'):
        return 'nd'
    elif (number == 3) | (number == '3'):
        return 'rd'
    else:
        return 'th'
