import pandas as pd

# clear()
no_adv_no_rerolls_list = []
no_adv_reroll_1s_list = []
no_adv_reroll_2s_list = []
adv_no_rerolls_list = []
adv_reroll_1s_list = []
adv_reroll_2s_list = []
dis_no_rerolls_list = []
dis_reroll_1s_list = []
dis_reroll_2s_list = []


def dice_roll_avg(die, rerolls, advantage):
    possible_outcomes = []
    variations = 0

    for roll in range(1, die):
        if roll <= rerolls:
            for reroll in range(1, die):
                possible_outcomes.extend([reroll])
                variations += 1
        else:
            chance = 1
            while chance < die:
                possible_outcomes.extend([roll])
                chance += 1
            variations += die - 1

    total = 0
    for string in possible_outcomes:
        total += int(string)

    average = "{:.1f}".format(total / variations)

    permutations_adv = []

    for outcome1 in possible_outcomes:
        for outcome2 in possible_outcomes:
            if outcome1 > outcome2:
                permutations_adv.extend([outcome1])
            else:
                permutations_adv.extend([outcome2])

    permutations_dis = []

    for outcome1 in possible_outcomes:
        for outcome2 in possible_outcomes:
            if outcome1 < outcome2:
                permutations_dis.extend([outcome1])
            else:
                permutations_dis.extend([outcome2])

    total_adv = 0
    for string in permutations_adv:
        total_adv += int(string)

    var_adv = len(permutations_adv)
    average_adv = "{:.1f}".format(total_adv / var_adv)

    total_dis = 0
    for string in permutations_dis:
        total_dis += int(string)

    var_dis = len(permutations_dis)
    average_dis = "{:.1f}".format(total_dis / var_dis)

    # adv_text = " advantage"
    # dis_text = " disadvantage"
    # out_text = "out advantage"

    if advantage == "n":
        # print (f"\nThe average roll on a d{die-1}, rerolling {rerolls}s, with{out_text} is...\n{average}")
        if rerolls == 0:
            no_adv_no_rerolls_list.append(average)
        elif rerolls == 1:
            no_adv_reroll_1s_list.append(average)
        elif rerolls == 2:
            no_adv_reroll_2s_list.append(average)
    elif advantage == "a":
        # print (f"\nThe average roll on a d{die-1}, rerolling {rerolls}s, with{adv_text} is...\n{average_adv}")
        if rerolls == 0:
            adv_no_rerolls_list.append(average_adv)
        elif rerolls == 1:
            adv_reroll_1s_list.append(average_adv)
        elif rerolls == 2:
            adv_reroll_2s_list.append(average_adv)
    elif advantage == "d":
        # print (f"\nThe average roll on a d{die-1}, rerolling {rerolls}s, with{dis_text} is...\n{average_dis}")
        if rerolls == 0:
            dis_no_rerolls_list.append(average_dis)
        elif rerolls == 1:
            dis_reroll_1s_list.append(average_dis)
        elif rerolls == 2:
            dis_reroll_2s_list.append(average_dis)


DICE = [4, 6, 8, 10, 12, 20]
REROLLS = [0, 1, 2]
ADVANTAGE = ["n", "a", "d"]

for advantage2 in ADVANTAGE:
    for reroll2 in REROLLS:
        for die2 in DICE:
            dice_roll_avg((die2 + 1), reroll2, advantage2)

die_list = []
for die3 in DICE:
    which_die = str(f"d{die3}")
    die_list.append(which_die)

# print(die_list)
# print(no_adv_no_rerolls_list)
# print(no_adv_reroll_1s_list)
# print(no_adv_reroll_2s_list)
# print(adv_no_rerolls_list)
# print(adv_reroll_1s_list)
# print(adv_reroll_2s_list)
# print(dis_no_rerolls_list)
# print(dis_reroll_1s_list)
# print(dis_reroll_2s_list)

no_adv_table = pd.DataFrame(list(zip(die_list, no_adv_no_rerolls_list, no_adv_reroll_1s_list, no_adv_reroll_2s_list)),
                            columns=["Die", "No Adv / No Rerolls", "No Adv / Reroll 1s", "No Adv / Reroll 2s"])

adv_table = pd.DataFrame(list(zip(die_list, adv_no_rerolls_list, adv_reroll_1s_list, adv_reroll_2s_list)),
                         columns=["Die", "   Adv / No Rerolls", "   Adv / Reroll 1s", "   Adv / Reroll 2s"])

dis_table = pd.DataFrame(list(zip(die_list, dis_no_rerolls_list, dis_reroll_1s_list, dis_reroll_2s_list)),
                         columns=["Die", "DisAdv / No Rerolls", "DisAdv / Reroll 1s", "DisAdv / Reroll 2s"])

print(no_adv_table)
print(adv_table)
print(dis_table)
