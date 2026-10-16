"""Mad Pod Racing — Solution 2: angle-aware braking and a conservative BOOST."""

boost_available = True

while True:
    x, y, checkpoint_x, checkpoint_y, distance, angle = map(int, input().split())

    absolute_angle = abs(angle)
    if absolute_angle > 90:
        thrust = 0
    elif absolute_angle > 45:
        thrust = 35
    elif absolute_angle > 20:
        thrust = 70
    else:
        thrust = 100

    if boost_available and distance > 5000 and absolute_angle < 5:
        thrust = "BOOST"
        boost_available = False

    print(checkpoint_x, checkpoint_y, thrust)
