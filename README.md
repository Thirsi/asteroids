# Asteroids Clone

A simple 2D asteroid-style game built with Python and Pygame as part of the Boot.dev curriculum. This project focuses on real-time movement, rotation, keyboard input, and structuring a small game loop.

## Overview

This project is a beginner-friendly arcade game inspired by the classic *Asteroids*. The player controls a spaceship, rotates it, and moves around the screen using keyboard input.

## Features

- Player spaceship movement
- Left and right rotation
- Frame-independent motion using delta time
- Simple project structure for learning game development fundamentals

## Tech Stack

- Python 3
- Pygame

## Project Structure

```text
.
├── main.py
├── player.py
├── constants.py
├── circleshape.py
├── logger.py
└── pyproject.toml
```

## Getting Started

Make sure you have:
```text
- Python 3
- Pip
```
## Installation

Clone the repo:
```text
https://github.com/Thirsi/asteroids
cd asteroids
```
Create and Activate a Virtual Environment:
```text
python3 -m venv venv
source venv/bin/activate
```
Install Dependencies:
```text
pip install pygame
```
Running the Game:
```text
python main.py
```
## Controls
```text
    A — rotate left
    D — rotate right
    W — move forward
    S — move backward
```
## What I Learned

Through this project, I practiced:
```text
-   working with Pygame
-   building a basic game loop
-   handling keyboard input
-   using delta time for smooth movement
-   organizing code across multiple files
```
## Future Improvements

Possible next steps for the project:
```text
-   shooting mechanics
-   asteroid spawning and collisions
-   score tracking
-   sound effects
-   game over and restart logic
```
## Acknowledgements
```text
Built as part of the Boot.dev backend and computer science curriculum.
```
## License
```text
This project is for educational purposes.
```