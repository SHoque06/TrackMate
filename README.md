# TrackMate

A desktop personal informatics gym tracking application built in Python for the CM10025 module at the University of Bath[cite: 1]. Developed collaboratively by a 10-person student team using an Agile Scrum framework, this repository preserves the original group codebase[cite: 1].

## Project Overview

TrackMate provides a minimalist, offline environment for users to log workouts, track bodyweight, and monitor long-term fitness goals[cite: 1]. The application prioritizes accessibility by removing cluttered interfaces and paywalls common in commercial alternatives, focusing strictly on immediate, personalized insights[cite: 1]. 

## Tech Stack & Architecture

*   **Language:** Python
*   **GUI Framework:** PySide6 (Qt for Python) with UI layouts generated from Qt Designer (`.ui` files).
*   **Data Visualization:** `matplotlib` integrated directly into PySide6 for dynamic progress charts.
*   **Database:** `sqlite3` for local, offline data persistence (`gymapp.db`).

## Core Modules

*   `main.py`: The application entry point that initializes the central `MainWindow` controller and links all widget displays.
*   `database_interface.py`: The backend data layer managing the SQLite schema (users, sessions, exercises, bodyweight, goals) and executing queries/updates.
*   `logworkout.py`: Workout logging widget featuring input validation prior to database commits[cite: 1].
*   `progress.py`: A `ProgressDisplay` widget embedding a `matplotlib` FigureCanvas to plot historical data trends[cite: 1].
*   `goalwidget.py` & `profilewidget.py`: Self-contained modules for managing user metrics and fitness milestones.

## Team & Collaboration

This project was a fully collaborative effort developed by a 10-person student team for the CM10025 module at the University of Bath[cite: 1]. Built across two structured Agile sprints, the team shared cross-functional responsibilities for UI design, database architecture, backend logic, and Scrum management to deliver the final application[cite: 1].

## Installation & Execution

Create and activate a virtual environment, and launch:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows use: .venv\Scripts\activate

python main.py
