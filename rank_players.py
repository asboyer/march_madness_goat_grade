import json

def rank_players():
    with open('big_data/players.json', 'r') as file:
        stats = json.load(file)

    ranks = {}
    total_players = 0
    for player in stats:
        ranks[player] = {}
        total_players += 1

    categories =  ["PTS", "AST", "TRB", "FG%", "FT%", "3P%", "STL", "BLK", "MP", "PER", "TS%", "WS", "BPM"]

    def rank(category):
        category_rankings = []
        for player in stats:
            if stats[player][category] != "":
                category_rankings.append([player, float(stats[player][category])])
            else:
                category_rankings.append([player, 0])
        category_rankings = sorted(category_rankings, key=lambda x: x[1])
        category_rankings.reverse()

        for i in range(len(category_rankings)):
            name = category_rankings[i][0]
            value = category_rankings[i][1]
            ranks[name][category] = i + 1

    for category in categories:
        rank(category)

    for player in ranks:
        score = 0
        for category in ranks[player]:
            score += ranks[player][category]
        ranks[player]['score'] = score
        ranks[player]['grade'] = int(score/len(categories))

    final_ranks = []
    for player in ranks:
        final_ranks.append([player, int(ranks[player]['score'])])
    final_ranks = sorted(final_ranks, key=lambda x: x[1])
    for i in range(len(final_ranks)):
        name = final_ranks[i][0]
        ranks[name]['rank'] = i + 1

    with open('data/player_ranks.json', 'w+', encoding='utf8') as file:
        file.write(json.dumps(ranks, ensure_ascii=False, indent =4))

