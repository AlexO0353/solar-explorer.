# test_models.py
import unittest
from models import Player, Planet, CelestialBody


class TestGameModels(unittest.TestCase):

    def test_planet_inheritance(self):
        """Tests that a Planet correctly inherits from CelestialBody."""
        mars = Planet("Mars", "The Red Planet", 227.9, "Fact", True, 2, -65, 3.7)

        # Check parent attributes are initialised properly
        self.assertEqual(mars.name, "Mars")
        self.assertEqual(mars.distance_from_sun, 227.9)
        self.assertIsInstance(mars, CelestialBody)

    def test_player_composition(self):
        """Tests that the Player class successfully utilises the Inventory class."""
        test_player = Player("Test Cadet")

        # Check initialisation
        self.assertEqual(len(test_player.inventory.items), 0)

        # Test adding an item (testing the composed object)
        test_player.inventory.add_item("Moon Rock")
        self.assertEqual(len(test_player.inventory.items), 1)
        self.assertEqual(test_player.inventory.items[0], "Moon Rock")

    def test_player_travel(self):
        """Tests the travel behaviour updates location correctly."""
        test_player = Player("Test Cadet")
        earth = Planet("Earth", "Blue Marble", 149.6, "Fact", True, 1, 15, 9.8)

        test_player.travel_to(earth)
        self.assertEqual(test_player.current_location.name, "Earth")


if __name__ == '__main__':
    unittest.main()
