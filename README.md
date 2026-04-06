# Solar Explorer: An Educational Space RPG

**Author:** Alexandra Oancea  
**Course:** UI108003 Software Design and Development (2025/26)  
**Assessment:** Assessment 2 - Software Development Project

## High-Level Vision Statement
**Solar Explorer** is an engaging, text-based Role-Playing Game (RPG) designed to teach players fascinating facts about our Solar System. The project demonstrates solid Object-Oriented Programming (OOP) principles—specifically inheritance and composition—and utilises advanced design patterns (Command and Factory) to ensure a scalable and maintainable codebase. By integrating third-party libraries for enhanced terminal output and graphical inputs, the application delivers a polished and interactive educational experience.

---

## User Instructions: Installation and Setup

### Prerequisites
* **Python 3.10+** must be installed on your system.
* A terminal or command prompt.

### Installation Steps

1. **Clone the repository:**
```bash
git clone [https://github.com/YourGitHubUsername/solar-explorer.git](https://github.com/AlexO0353/solar-explorer..git)
cd solar-explorer
```
2. **Create a virtual environment:**

```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```
3. **Install third-party dependencies:**

```bash
pip install -r requirements.txt
```

### Running the Game

To start the application, run the main file from your terminal:

```bash
python main.py
```

A graphical window will appear asking for your Astronaut Name. After entering it, return to your terminal to play!

### How to Play 

Type the following commands into the terminal when prompted:

Fly your ship to a specific planet: (e.g., travel mars)

```bash
travel <planet name>
```

Scan your current location to learn an educational fact:

```bash
explore
```

Safely power down the ship and exit the game:

```bash
quit
```

### Project Structure

The project is separated into distinct files to maintain a clean architecture:

```bash
main.py
```
The entry point containing the main game loop, selection, and iteration logic.

```bash
models.py
```
Contains the Object Hierarchy (Player, Inventory, CelestialBody, Planet). Demonstrates Inheritance and Composition.

```bash
patterns.py
```
Encapsulates the Command and Factory design patterns to handle user input processing cleanly.

```bash
test_models.py
```
Developer unit tests supporting Test-Driven Development (TDD).

```bash
requirements.txt
```
Lists the third-party libraries used (easygui, rich).

### Agile Planning and Project Management
This project was developed using Agile methodologies, specifically utilising a Kanban board and Test-Driven Development (TDD).

Definitions
Definition of Ready (DoR): A user story is considered "Ready" to be moved to the 'To Do' column when it is clearly written, the acceptance criteria are explicitly defined, and no further clarification is needed to begin coding.
Definition of Done (DoD): A user story is "Done" when the feature is coded in Python 3, inline comments are added to explain complex logic/patterns, unit tests are passing, and the code is successfully merged into the main branch via Continuous Integration (CI).

### User Stories Summary
US1: As a player, I want to be prompted for my name using a graphical window so that the game feels personalised.
US2: As a player, I want to type commands to travel to different planets and explore them to learn facts.
US3: As a developer, I need to implement an object hierarchy using Composition and Inheritance to structure the game entities appropriately.
US4: As a player, I want to type "quit" to safely exit the application.

(Evidence of the GhitHub project board, including Backlog, Ready, In Progress, Code Review and Done columns, is provided in the separate submission document).

### Testing and Continuous Integration (CI)
This project follows Test-Driven Development. Developer tests are written in test_models.py using the unittest framework (or standard assertions) to validate individual functions and object relationships before implementation.

Continuous Integration: GitHub Actions is configured (.github/workflows/python-tests.yml) to automatically run these tests every time code is pushed to the main branch, ensuring new features do not break existing functionality.
