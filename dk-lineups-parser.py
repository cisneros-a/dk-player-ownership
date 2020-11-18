import csv

payouts = [
    [1, 200000],
    [2, 50000],
    [3, 25000],
    [4, 10000],
    [5, 7500],
    [6, 5000],
    [8, 2500],
    [10, 2000],
    [13, 1500],
    [16, 1000],
    [20, 750],
    [25, 600],
    [35, 500],
    [45, 400],
    [60, 300],
    [75, 250],
    [99, 200],
    [120, 150],
    [195, 100],
    [315, 75],
    [565, 60],
    [1165, 50],
    [2356, 40],
    [7215, 30]
]

def find_contest_player_ownership(file, username = None):
    with open(file, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        # this skips the first line of the file
        next(csv_reader)

        # returns a list and int
        players_list, total_rosters = create_list_of_players(csv_reader, username)
        # returns an object
        player_frequency = get_player_frequency(players_list)
        find_ownership_percentages(player_frequency, total_rosters)

# optional argument to find player ownership for specific users.
def create_list_of_players(csv_file, username = None):
    players = []
    total_rosters = 0
    for line in csv_file:
        if username:
            if line[2].split(' ')[0] != username:
                continue
        total_rosters += 1
        roster = line[5]
        split = roster.split()
        player_name = ""
        positions = ["QB", "RB", "WR", "TE", "FLEX", "DST"]
        for x in range(len(split)):
            if split[x] in positions:
                players.append(player_name.rstrip())
                player_name = ""
            else:
                player_name += f'{split[x]} '
    return players, total_rosters

def get_player_frequency(players_list):
    player_ownership_obj = {}
    for player in players_list:
        if player == "":
            continue
        elif player in player_ownership_obj:
            player_ownership_obj[player] += 1
        else:
            player_ownership_obj[player] = 1
    return player_ownership_obj
    
def find_ownership_percentages(player_frequency, total_rosters):
    for player in player_frequency:
            if round(player_frequency[player] / total_rosters, 2) > 0.01:
                player_frequency[player] = round(player_frequency[player] / total_rosters *100)
                print(f'{player}: {player_frequency[player]}%')




#find_contest_player_ownership('600K-wk10-2020.csv', "username")

