# Mad Pod Racing — Python 3 solutions

A progression of self-contained Python 3 bots for [CodinGame's Mad Pod Racing](https://www.codingame.com/ide/puzzle/mad-pod-racing), from the minimum viable bot to a stateful heuristic that learns the course.

## Solutions

| File | Difficulty | Strategy |
|---|---:|---|
| [`solutions/01_direct.py`](solutions/01_direct.py) | Simple | Full thrust straight at the current checkpoint. |
| [`solutions/02_angle_braking.py`](solutions/02_angle_braking.py) | Beginner | Brakes according to the checkpoint angle; saves `BOOST` for a long straight. |
| [`solutions/03_drift_compensation.py`](solutions/03_drift_compensation.py) | Intermediate | Estimates velocity from successive positions and aims against its drift. |
| [`solutions/04_course_learning.py`](solutions/04_course_learning.py) | Advanced heuristic | Learns checkpoint order, cuts known checkpoints, compensates drift, brakes for corners, and uses one conservative `BOOST`. |

## How to use

1. Open the puzzle in the CodinGame IDE.
2. Choose one source file (start with `02_angle_braking.py`).
3. Copy its full contents into the Python 3 editor.
4. Run the built-in tests, tune constants, and submit.

The versions are deliberately independent: copy **one complete file**, not a mix of fragments from multiple files.

## I/O protocol

These scripts use the classic per-turn input protocol:

```text
x y next_checkpoint_x next_checkpoint_y next_checkpoint_dist next_checkpoint_angle
opponent_x opponent_y
```

and print:

```text
target_x target_y thrust
```

`thrust` is an integer from `0` to `100`, `BOOST` once, or `SHIELD` where the active league supports it. The supplied bots read the opponent position to keep their input stream aligned, but their main objective is racing-line control rather than collision combat.

> CodinGame may reveal mechanics progressively by league. Use the most advanced script only once your available input/output protocol supports it.

## Why the strategies progress

- **Direct target:** verifies the game loop and output format.
- **Angle braking:** avoids applying maximum acceleration into a turn.
- **Drift compensation:** handles the fact that the pod retains velocity between turns.
- **Course learning:** on later laps it begins aiming through a checkpoint toward the known next checkpoint, while preserving enough braking to pass the current one.

## High-level next step: local simulation

A stronger competitive bot needs a local physics simulator and a short-horizon action search. At every decision, search candidate rotations and thrust values over the next 3–6 turns, simulate rotation → thrust → movement → collision → friction, and score checkpoint progress, remaining distance, alignment, and approach speed. That is more robust than relying solely on fixed thresholds.

## License

[MIT](LICENSE)
