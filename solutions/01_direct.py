"""Mad Pod Racing — Solution 1: minimum viable bot (Python 3)."""

while True:
    x, y, checkpoint_x, checkpoint_y, distance, angle = map(int, input().split())
    opponent_x, opponent_y = map(int, input().split())
    print(checkpoint_x, checkpoint_y, 100)
