# patterns.py

class Command:
    """Base Command Interface"""

    def execute(self, player, solar_system):
        pass


class TravelCommand(Command):
    """Handles moving the player to a new planet."""

    def __init__(self, destination_name):
        # Clean up the input: remove any accidental < or > brackets the user might type
        self.destination_name = destination_name.lower().replace("<", "").replace(">", "").strip()

    def execute(self, player, solar_system):
        # Search the solar system array for the requested planet
        for planet in solar_system:
            if planet.name.lower() == self.destination_name:
                player.travel_to(planet)
                return f"[bold green]Warp drive engaged![/bold green] You have arrived at {planet.name}."

        return f"[bold red]Navigation Error:[/bold red] Planet '{self.destination_name}' not found in the database."


class ExploreCommand(Command):
    """Handles displaying facts about the current location."""

    def execute(self, player, solar_system):
        if player.current_location:
            # Calls the method from our OOP model
            return player.current_location.explore_data()
        return "[red]Error: You are not currently orbiting a known planet.[/red]"


class QuitCommand(Command):
    """Handles safely shutting down the game."""

    def execute(self, player, solar_system):
        return "QUIT_GAME"


class CommandFactory:
    """
    Demonstrates the FACTORY PATTERN.
    Takes the raw text input and returns the correct Command object.
    """

    @staticmethod
    def parse_input(user_input):
        parts = user_input.strip().split()
        if not parts:
            return None

        action = parts[0].lower()

        if action == "travel" and len(parts) > 1:
            # Pass the second word (the planet name) to the command
            destination = " ".join(parts[1:])
            return TravelCommand(destination)

        elif action == "explore":
            return ExploreCommand()

        elif action == "quit":
            return QuitCommand()

        # If unrecognised, return None to trigger the error handling in main.py
        return None
