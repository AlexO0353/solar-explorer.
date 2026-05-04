# main.py
import easygui
from rich.console import Console
from rich.panel import Panel

# Import our custom classes from the distinct files
from models import Player, Planet
from patterns import CommandFactory

# Initialise the rich console for enhanced terminal output
console = Console()


def initialise_game_data():
    """
    Initializes and returns the game data.
    Planet parameters: (name, description, distance, fact, atmosphere, moons, temp_celsius, gravity_m/s2)
    """
    return [
        Planet("Mercury", "The Swift Planet", 57.9, "A year on Mercury is just 88 Earth days.", False, 0, 167, 3.7),
        Planet("Venus", "Earth's Sister", 108.2, "Venus spins backwards compared to most other planets.", True, 0, 464, 8.87),
        Planet("Earth", "The Blue Marble", 149.6, "Earth is the only known planet to support life.", True, 1, 15, 9.8),
        Planet("Mars", "The Red Planet", 227.9, "Mars has the largest volcano in the solar system, Olympus Mons.", True, 2, -65, 3.7),
        Planet("Jupiter", "The Gas Giant", 778.5, "Jupiter is so massive that >1,300 Earths could fit inside it.", True, 95, -110, 24.79),
        Planet("Saturn", "The Ringed Planet", 1434.0, "Saturn's beautiful rings are mostly chunks of ice and rock.", True, 146, -140, 10.44),
        Planet("Uranus", "The Ice Giant", 2871.0, "Uranus rotates on its side, like a rolling ball.", True, 28, -195, 8.69),
        Planet("Neptune", "The Windy Planet", 4495.0, "Neptune has the strongest winds, reaching >2,000 km/h.", True, 16, -200, 11.15)
    ]


def get_player_name():
    """
    Uses a third-party graphical library to capture the user's name.
    Includes a fallback to terminal input if the GUI environment fails.
    """
    try:
        # Attempt to open the graphical window
        name = easygui.enterbox("Welcome to Solar Explorer!\n\nPlease enter your Astronaut Name:", "Player Setup")
    except Exception:
        # If the GUI fails (common in some IDEs), fall back to terminal input
        console.print("[yellow]Graphical window blocked by environment. Falling back to terminal.[/yellow]")
        name = input("Welcome to Solar Explorer!\nPlease enter your Astronaut Name: ")

    # If the user clicks cancel or leaves it blank, provide a default
    if not name or name.strip() == "":
        name = "Space Cadet"
    return name


def display_help():
    """Prints the available commands to the user."""
    console.print("[bold cyan]Available Commands:[/bold cyan]")
    console.print("  [green]travel <planet name>[/green] - Fly to a new planet (e.g., 'travel mars')")
    console.print("  [green]explore[/green]              - Learn facts about your current location")
    console.print("  [red]quit[/red]                 - Exit the game")


def main_loop(player, solar_system):
    """
    The main game engine loop.
    Demonstrates Iteration (While loop) and continuous input reading.
    """
    playing = True

    # Set starting location
    player.travel_to(solar_system[2])  # Start on Earth (Index 2)

    console.print(Panel.fit(f"Welcome aboard, [bold magenta]{player.name}[/bold magenta]!", title="Solar Explorer"))
    display_help()

    # Iteration: The main loop keeps the game running until the user quits
    while playing:
        # 1. Prompt for user input
        console.print(f"\n[bold yellow]Current Location:[/bold yellow] {player.current_location.name}")
        raw_input = console.input("[bold blue]What are your orders? > [/bold blue]")
        user_input = raw_input.strip()

        # 2. Intercept the quit command directly in main.py (Implementing Elizabeth's feedback)
        if user_input.lower() == "quit":
            playing = False
            console.print("[bold red]Initiating shutdown sequence. Goodbye![/bold red]")
            continue

        # 3. Use the Factory Pattern to get the right command for game actions
        command = CommandFactory.parse_input(user_input)

        # 4. Execute the command (if valid)
        if command:
            # Parameter passing (player, solar_system)
            result = command.execute(player, solar_system)

            # Print the command execution results
            if result:
                console.print(Panel(result, expand=False))
        else:
            # Handle invalid commands gracefully
            console.print(
                "[italic red]Command not recognised. Type 'explore', 'travel <planet>', or 'quit'.[/italic red]")


if __name__ == "__main__":
    # 1. Setup Data
    planets_data = initialise_game_data()

    # 2. Setup Player (using GUI with safe fallback)
    astronaut_name = get_player_name()
    current_player = Player(astronaut_name)

    # 3. Start the game loop (passing variables as parameters, avoiding globals)
    main_loop(current_player, planets_data)
