"""Mad Pod Racing — Solution 3: estimated velocity plus drift compensation."""

import math


def clamp(value, low, high):
    return max(low, min(high, value))


boost_available = True
last_x = None
last_y = None

while True:
    x, y, checkpoint_x, checkpoint_y, distance, angle = map(int, input().split())
    opponent_x, opponent_y = map(int, input().split())

    if last_x is None:
        velocity_x, velocity_y = 0, 0
    else:
        velocity_x = x - last_x
        velocity_y = y - last_y
    last_x, last_y = x, y

    speed = math.hypot(velocity_x, velocity_y)
    compensation = clamp(speed * 2.2, 0, 1800)
    target_x = int(checkpoint_x - velocity_x * compensation / max(speed, 1))
    target_y = int(checkpoint_y - velocity_y * compensation / max(speed, 1))

    absolute_angle = abs(angle)
    if absolute_angle > 100:
        thrust = 0
    elif absolute_angle > 60:
        thrust = 25
    elif absolute_angle > 30:
        thrust = 60
    else:
        thrust = 100

    if distance < 1800 and speed > 500:
        thrust = min(thrust, 45)

    if boost_available and distance > 5500 and absolute_angle < 4 and speed < 650:
        thrust = "BOOST"
        boost_available = False

    print(target_x, target_y, thrust)
