from abc import ABC, abstractmethod


class AbstractRecipe(ABC):

    def execute_recipe(self):
        self.get_ready()
        self.prepare_the_dish()
        self.wash_up()

    @abstractmethod
    def get_ready(self):
        pass

    @abstractmethod
    def prepare_the_dish(self):
        pass

    @abstractmethod
    def wash_up(self):
        pass


class PastaRecipe(AbstractRecipe):

    def get_ready(self):
        print("Prepare the pasta")

    def prepare_the_dish(self):
        print("Boil the pasta")

    def wash_up(self):
        print("Wash the dishes")

class RecipeWithMicrowave(AbstractRecipe):

    def get_ready(self):
        print("Open the packaging and put its content into a bowl")

    def prepare_the_dish(self):
        print("Set the microwave for 2 minutes cooking")

    def wash_up(self):
        print("Wash up carefully")


recipe = PastaRecipe()
recipe.execute_recipe()
recipe_microwave = RecipeWithMicrowave()
recipe_microwave.execute_recipe()
