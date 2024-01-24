import json
import random
from tabulate import tabulate
import copy

team_blue = {}
team_red = {}
players_list = {}

nplayers = 11  # Replace 10 with the desired quantity of players


def team_split(sorted_player_list):
    teams = [{}, {}]
    for i in range(1, nplayers + 1):
        team_index = i % 2
        key, value = sorted_player_list.popitem()
        teams[team_index].update({key: value})
    return teams


def swith_item(teams_copy, i):
    key0, value0 = list(teams_copy[0])[i], list(teams_copy[0].values())[i]
    key1, value1 = list(teams_copy[1])[i], list(teams_copy[1].values())[i]
    teams_copy[0].pop(key0)
    teams_copy[1].pop(key1)
    teams_copy[0].update({key1: value1})
    teams_copy[1].update({key0: value0})
    teams_copy[0] = dict(
        sorted(teams_copy[0].items(), key=lambda item: item[1], reverse=True)
    )
    teams_copy[1] = dict(
        sorted(teams_copy[1].items(), key=lambda item: item[1], reverse=True)
    )
    return teams_copy


def team_optimize(teams):
    absolute_score_difference = get_absolute_difference(teams)
    print(f"Start with: {absolute_score_difference}")
    can_optimize = True
    min_count_dict = min(len(teams[0]), len(teams[1]))
    i = 0
    while can_optimize:
        # switch last items
        optimized_teams = swith_item(copy.deepcopy(teams), i)
        new_diff = get_absolute_difference(optimized_teams)
        if new_diff < absolute_score_difference:
            print(f"before: {absolute_score_difference} after:{new_diff}")
            teams = optimized_teams
            absolute_score_difference = new_diff
        # take change back if not helping
        else:
            print(f"before: {absolute_score_difference} after:{new_diff}")
        i = i + 1
        if i == min_count_dict - 1:
            can_optimize = False

    return teams


def get_absolute_difference(teams):
    team_blue = teams[0]
    team_red = teams[1]
    blue_score = sum(team_blue.values())
    red_score = sum(team_red.values())
    return abs(blue_score - red_score)


def print_scores(teams):
    team_blue = teams[0]
    team_red = teams[1]

    blue_score = sum(team_blue.values())
    red_score = sum(team_red.values())
    absolute_score_difference = abs(blue_score - red_score)
    ratio = max(blue_score, red_score) / min(blue_score, red_score)
    print(
        f"blue:{blue_score} red:{red_score} Diff:{absolute_score_difference} ratio:{ratio}"
    )
    print(
        tabulate(
            {**team_blue, "Total": blue_score}.items(),
            headers=["Blue", "Score"],
            tablefmt="simple_grid",
        )
    )

    print(
        tabulate(
            {**team_red, "Total": red_score}.items(),
            headers=["Red", "Score"],
            tablefmt="simple_grid",
        )
    )


player_list = {
    f"P{i}".ljust(3, " "): random.randint(0, 200) for i in range(1, nplayers + 1)
}

# player_list = {
#     "P1": 130,
#     "P2": 84,
#     "P3": 179,
#     "P4": 9,
#     "P5": 33,
#     "P6": 190,
#     "P7": 64,
#     "P8": 46,
#     "P9": 118,
#     "P10": 129,
# }

print(tabulate(player_list.items(), headers=["Player", "Score"], tablefmt="psql"))
sorted_player_list = dict(
    sorted(player_list.items(), key=lambda item: item[1], reverse=False)
)
print(
    tabulate(sorted_player_list.items(), headers=["Player", "Score"], tablefmt="psql")
)


# start team skill order
teams = team_split(sorted_player_list)
print_scores(teams)
teams = team_optimize(teams)
print_scores(teams)
