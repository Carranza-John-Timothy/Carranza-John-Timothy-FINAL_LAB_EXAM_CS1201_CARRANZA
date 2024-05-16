import os
import datetime

class GameManager:
    def __init__(self, game_file):
        self.game_file = game_file
        self.games = self.load_games()

    def load_games(self):
        if not os.path.exists(self.game_file):
            return []
        with open(self.game_file, 'r') as f:
            games = []
            for line in f.readlines():
                game_id, username, score, datetime = line.strip().split(',')
                games.append({
                    'id': game_id,
                    'username': username,
                    'score': int(score),
                    'datetime': datetime
                })
            return games

    def save_game(self, username, score):
        game_id = str(datetime.datetime.now()).replace(' ', '_')
        with open(self.game_file, 'a') as f:
            f.write(f"{game_id},{username},{score},{datetime.datetime.now()}\n")
        self.games.append({
            'id': game_id,
            'username': username,
            'score': score,
            'datetime': datetime.datetime.now()
        })

    def get_top_scores(self, num_scores):
        sorted_games = sorted(self.games, key=lambda x: x['score'], reverse=True)
        return sorted_games[:num_scores]