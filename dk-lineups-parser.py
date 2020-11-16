import csv

def find_all_player_ownership(file):

    with open(file, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        # this skips the first line of the file
        next(csv_reader)

        # returns a list and int
        players_list, total_rosters = create_list_of_players(csv_reader)
        # returns an object
        player_frequency = get_player_frequency(players_list)
        find_ownership_percentages(player_frequency, total_rosters)


def create_list_of_players(csv_file):
    players = []
    total_rosters = 0
    for line in csv_file:
            total_rosters += 1
            roster = line[5]
            split = roster.split()
            player_name = ""
            for x in range(len(split)):
                if x % 3 == 0:
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
            
            player_frequency[player] = round(player_frequency[player] / total_rosters, 2)
            print(f'{player}: {player_frequency[player]}%')


find_all_player_ownership('three-man-contest.csv')
