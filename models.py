# models.py

class CelestialBody:
    """
    Base class representing a generic body in space.
    """
    def __init__(self, name, description, distance_from_sun):
        self.name = name
        self.description = description
        self.distance_from_sun = distance_from_sun


class Planet(CelestialBody):
    """
    Child class representing a specific Planet.
    Demonstrates INHERITANCE by extending CelestialBody.
    """
    def __init__(self, name, description, distance_from_sun, fact, atmosphere, moons, temp_celsius, gravity):
        # Call the parent class constructor
        super().__init__(name, description, distance_from_sun)
        self.fact = fact
        self.atmosphere = atmosphere
        self.moons = moons
        self.temp_celsius = temp_celsius
        self.gravity = gravity

    def explore_data(self):
        """Returns a formatted string containing educational facts."""
        atmos_status = "Yes" if self.atmosphere else "No"
        return (
            f"[bold cyan]Planet Data: {self.name}[/bold cyan]\n"
            f"[italic]{self.description}[/italic]\n\n"
            f"🌍 [bold]Distance from Sun:[/bold] {self.distance_from_sun} million km\n"
            f"🌙 [bold]Moons:[/bold] {self.moons}\n"
            f"🌡️ [bold]Average Temp:[/bold] {self.temp_celsius}°C\n"
            f"☄️ [bold]Gravity:[/bold] {self.gravity} m/s²\n"
            f"☁️ [bold]Atmosphere:[/bold] {atmos_status}\n\n"
            f"💡 [bold yellow]Fun Fact:[/bold yellow] [green]{self.fact}[/green]"
        )


class Inventory:
    """
    Manages the items a player collects.
    Used to demonstrate COMPOSITION within the Player class.
    """
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)


class Player:
    """
    Represents the user navigating the game.
    Demonstrates COMPOSITION by containing an Inventory object.
    """
    def __init__(self, name):
        self.name = name
        self.current_location = None
        # Composition: The Player 'has an' Inventory
        self.inventory = Inventory()

    def travel_to(self, planet):
        """Updates the player's current location."""
        self.current_location = planet
