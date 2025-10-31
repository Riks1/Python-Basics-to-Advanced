# Builder and Prototype Design Pattern Example

import copy

# 1. Builder pattern 

class Sandwich:
    """Product class representing the complex object being built."""

    def __init__(self):
        self.ingredients = []

    def add(self, ingredient: str):
        self.ingredients.append(ingredient)

    def describe(self) -> str:
        return "Sandwich with " + ", ".join(self.ingredients)


class SandwichBuilder:
    """Builder class that constructs Sandwich objects step-by-step."""

    def __init__(self):
        self.sandwich = Sandwich()

    def add_bread(self) -> "SandwichBuilder":
        self.sandwich.add("Bread")
        return self

    def add_lettuce(self) -> "SandwichBuilder":
        self.sandwich.add("Lettuce")
        return self

    def add_tomato(self) -> "SandwichBuilder":
        self.sandwich.add("Tomato")
        return self

    def add_cheese(self) -> "SandwichBuilder":
        self.sandwich.add("Cheese")
        return self

    def add_meat(self) -> "SandwichBuilder":
        self.sandwich.add("Meat")
        return self

    def build(self) -> Sandwich:
        return self.sandwich


class Chef:
    """Director class to define standard sandwich recipes."""

    @staticmethod
    def make_club_sandwich() -> Sandwich:
        return (
            SandwichBuilder()
            .add_bread()
            .add_lettuce()
            .add_tomato()
            .add_cheese()
            .add_meat()
            .add_bread()
            .build()
        )

# 2. Prototype pattern

class Robot:
    """Prototype class that supports cloning."""

    def __init__(self, name: str, model: str, tasks: list[str]):
        self.name = name
        self.model = model
        self.tasks = tasks

    def clone(self) -> "Robot":
        """Clone this robot using deep copy."""
        return copy.deepcopy(self)

    def __str__(self) -> str:
        return f"Robot(Name: {self.name}, Model: {self.model}, Tasks: {self.tasks})"

# 3. Demonstration

if __name__ == "__main__":
    print("\nBuilder pattern: ")
    club_sandwich = Chef.make_club_sandwich()
    print(club_sandwich.describe())

    print("\nPrototype pattern: ")
    original_robot = Robot("HelperBot", "X100", ["Clean", "Cook"])
    print("Original:", original_robot)

    cloned_robot = original_robot.clone()
    cloned_robot.name = "AssistantBot"
    cloned_robot.tasks.append("Serve")

    print("Cloned:", cloned_robot)
    print("Original after clone (unchanged):", original_robot)
