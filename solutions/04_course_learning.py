"""Mad Pod Racing — Solution 4: learn the course, cut checkpoints, counter drift."""

import math


def clamp(value, low, high):
    return max(low, min(high, value))


def length(x, y):
    return math.hypot(x, y)


boost_available = True
last_x = None
last_y = None
previous_checkpoint = None
next_checkpoint = {}

while True:
    x, y, checkpoint_x, checkpoint_y, distance, angle = map(int, input().split())
    opponent_x, opponent_y = map(int, input().split())

    current_checkpoint = (checkpoint_x, checkpoint_y)
    if previous_checkpoint is not None and previous_checkpoint != current_checkpoint:
        next_checkpoint[previous_checkpoint] = current_checkpoint
    previous_checkpoint = current_checkpoint

    if last_x is None:
        velocity_x, velocity_y = 0.0, 0.0
    else:
        velocity_x = x - last_x
        velocity_y = y - last_y
    last_x, last_y = x, y
    speed = length(velocity_x, velocity_y)

    target_x, target_y = float(checkpoint_x), float(checkpoint_y)
    following_checkpoint = next_checkpoint.get(current_checkpoint)

    # On subsequent laps, begin pointing through a known checkpoint.
    if following_checkpoint is not None and distance < 1800:
        following_x, following_y = following_checkpoint
        segment_x = following_x - checkpoint_x
        segment_y = following_y - checkpoint_y
        segment_length = length(segment_x, segment_y)
        if segment_length:
            cut_distance = min(1300, segment_length * 0.45)
            target_x += segment_x / segment_length * cut_distance
            target_y += segment_y / segment_length * cut_distance

    # Aim against residual momentum to reduce lateral drift.
    if speed > 1:
        correction = clamp(speed * 1.8, 0, 1500)
        target_x -= velocity_x / speed * correction
        target_y -= velocity_y / speed * correction

    absolute_angle = abs(angle)
    if absolute_angle > 110:
        thrust = 0
    elif absolute_angle > 75:
        thrust = 20
    elif absolute_angle > 45:
        thrust = 45
    elif absolute_angle > 20:
        thrust = 75
    else:
        thrust = 100

    if distance < 1400:
        if speed > 650:
            thrust = min(thrust, 20)
        elif speed > 400:
            thrust = min(thrust, 50)

    if absolute_angle > 90:
        thrust = 0

    if boost_available and distance > 6000 and absolute_angle < 4 and speed < 700:
        thrust = "BOOST"
        boost_available = False

    print(int(target_x), int(target_y), thrust)
