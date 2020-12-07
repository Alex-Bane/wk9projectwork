from flask import Flask, Response, request
import requests
import random

app = Flask(__name__)

@app.route('/stats', methods=['GET','POST'])
def stats():
    stats = []
    while len(stats) < 6:
        stats.append(random.randint(3, 18))
    bonus = ""
    race = request.data.decode('utf-8')
    if race == "Human":
        bonus = "Bonus Stats: +1 to all"
        stats[0] = stats[0] + 1
        stats[1] = stats[1] + 1
        stats[2] = stats[2] + 1
        stats[3] = stats[3] + 1
        stats[4] = stats[4] + 1
        stats[5] = stats[5] + 1
    elif race == "Elf":
        bonus = "Bonus Stats: +2 to Dexterity, +1 to Wisdom"
        stats[1] = stats[1] + 2
        stats[4] = stats[4] + 1
    elif race == "Dwarf":
        bonus = "Bonus Stats: +2 to Constitution, +1 to Strength"
        stats[2] = stats[2] + 2
        stats[0] = stats[0] + 1
    elif race == "Halfling":
        bonus = "Bonus Stats: +2 to Charisma, +1 to Dexterity"
        stats[5] = stats[5] + 2
        stats[1] = stats[1] + 1
    elif race == "Half-Orc":
        bonus = "Bonus Stats: +2 to Strength, +1 to Constitution"
        stats[0] = stats[0] + 2
        stats[2] = stats[2] + 1
    else:
        bonus = 'Race not found'
    str_stat = stats[0]
    dex_stat = stats[1]
    con_stat = stats[2]
    int_stat = stats[3]
    wis_stat = stats[4]
    cha_stat = stats[5]
    strength = "Strength: ", str_stat
    dexterity = "Dexterity: ", dex_stat
    constitution = "Constitution: ", con_stat
    inteligence = "Inteligence: ", int_stat
    wisdom = "Wisdom: ", wis_stat
    charisma = "Charisma: ", cha_stat
    combined = bonus, ''.join(str(stat) for stat in strength), ''.join(str(stat) for stat in dexterity), ''.join(str(stat) for stat in constitution), ''.join(str(stat) for stat in inteligence), ''.join(str(stat) for stat in wisdom), ''.join(str(stat) for stat in charisma)
    combined_string = '\n'.join(str(stat) for stat in combined)
    return Response(combined_string, mimetype="text/plain")




if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5003)
