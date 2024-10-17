class Stats():
    def __init__(self):
        self.resrt_stats()
        self.run_game=True
        with open('highscore.txt','r') as f:
            self.high_score=int(f.readline())

    def resrt_stats(self):
        self.guns_left=3
        self.score=0