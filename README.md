# Rock-Paper-scissor
A simple command-line Rock-Paper-Scissors game in Python that tracks player stats, rounds, and game results, with optional database integration for storing game history.

Features

- Play 3 rounds per game.
- Tracks round wins, losses, and draws.
- Tracks overall games played and results.
- Stores player stats in a SQLite database
- Option to delete a player’s data from the database.

File structure:

main.py → Core game logic, rounds, stats, printing results.
data.py → Handles database operations (add_data, update_data, delete_data, show_data).

Requirements
- Python 3.x
- pandas (for displaying database table
- SQLite3 
