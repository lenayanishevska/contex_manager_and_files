import csv


def high_scores_to_cvs():
    with open("game_results.csv", "r") as read_csv, open("high_scores.csv", "w") as write_csv:
        reader = csv.reader(read_csv)
        header = next(reader)
        data = list(reader)

        highest_scores = {}
        for row in list(data):
            player, score = row
            score = int(score)
            if player not in highest_scores or highest_scores[player] < score:
                highest_scores[player] = score

        sorted_scores = sorted(highest_scores.items(), key=lambda x: x[1], reverse=True)

        csv_writer = csv.writer(write_csv)
        csv_writer.writerow(['Player name', 'Highest score'])
        for player, highest_score in sorted_scores:
            csv_writer.writerow([player, highest_score])

