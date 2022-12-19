class Hero:
    """
    This class deals with:
    1. Defining a hero.
    2. Making database calls to save or retrieve a hero.
    3. Defining an individual logger that would define messages for the state of the hero.
    This class doesn't follow the Single Responsibility Principle.
    """

    def __init__(self, id: int, name: str, classification: str):
        self.id = id
        self.name = name
        self.health_points = 100
        self.stamina_points = 100
        self.classification = classification

    def get_classification(self) -> str:
        return self.classification
    
    def get_name(self) -> str:
        return self.name

    def save(self, hero):
        # Logic for saving the data in a database
        pass

    def retrieve(self, id: int):
        # Logic for fetching the data from the database
        pass

    def log_health_message(self):
        if self.health_points > 90:
            print("Strong.")
        elif self.health_points > 60:
            print("Moderately strong.")
        elif self.health_points > 40:
            print("Weakening. Consider drinking health potion.")
        elif self.health_points > 10:
            print("Extremely weak. Take cover!")

    def log_classification_message(self):
        if self.classification == "Palladin":
            print("A Palladin is expected to be in the front line tanking the damage.")
        elif self.classification == "Support":
            print("A support member is supposed to keep an eye out for the entire team and provide buffs to allies and debuffs to the enemies.")
        elif self.classification == "Assassin":
            print("An assassin is supposed to be able to deliver fatal sneaky blows to the enemy team to devastate them.")
        elif self.classification == "Warrior":
            print("Warriors are typics aggressors who tend to dish out the most frontline damage.")
        elif self.classification == "Archer":
            print("An archer dishes out the most overall damage by attacking from the back-row, fortified by palladins and warriors.")


class Hero:
    """
    This class is solely responsible for the single purpose of defining a hero.
    This class conforms to the Single Repsonsibility Principle.
    """

    def __init__(self, id: int, name: str, classification: str):
        self.id = id
        self.name = name
        self.health_points = 100
        self.stamina_points = 100
        self.classification = classification

    def get_classification(self) -> str:
        return self.classification
    
    def get_name(self) -> str:
        return self.name


class HeroDatabase:
    """
    This class is solely responsible for the single purpose of saving a hero to the database.
    This class conforms to the Single Repsonsibility Principle.
    """

    def save(self, hero: Hero):
        # Logic for saving the data in a database
        pass

    def retrieve(self, id: int):
        # Logic for fetching the data from the database
        pass


class HeroLogger:
    """
    This class is solely responsible for the single purpose of setting up the messages for the status of the heroes.
    This class conforms to the Single Repsonsibility Principle.
    """

    def log_health_message(self, hero: Hero):
        if hero.health_points > 90:
            print("Strong.")
        elif hero.health_points > 60:
            print("Moderately strong.")
        elif hero.health_points > 40:
            print("Weakening. Consider drinking health potion.")
        elif hero.health_points > 10:
            print("Extremely weak. Take cover!")

    def log_classification_message(self, hero: Hero):
        if hero.classification == "Palladin":
            print("A Palladin is expected to be in the front line tanking the damage.")
        elif hero.classification == "Support":
            print("A support member is supposed to keep an eye out for the entire team and provide buffs to allies and debuffs to the enemies.")
        elif hero.classification == "Assassin":
            print("An assassin is supposed to be able to deliver fatal sneaky blows to the enemy team to devastate them.")
        elif hero.classification == "Warrior":
            print("Warriors are typics aggressors who tend to dish out the most frontline damage.")
        elif hero.classification == "Archer":
            print("An archer dishes out the most overall damage by attacking from the back-row, fortified by palladins and warriors.")