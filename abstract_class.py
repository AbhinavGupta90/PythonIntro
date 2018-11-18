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


recipe = PastaRecipe()
recipe.execute_recipe()