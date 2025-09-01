class Enemy:
    def __init__(self, type_of_enemy):
        self.__type_of_enemy:str = type_of_enemy
        self.health_points:int = 10
        self.attack_points:int = 1

    def talk(self):
        print(f"""
        Hi There, I am your new enemy, I am a {self.__type_of_enemy},
        My health is now at {self.health_points}
        And I can attack at {self.attack_points} 
        """)


class Zombie(Enemy):

    def __init__(self):
        super().__init__("Zombie")

    def talk(self):
        print("Grambling")

    def spreading_infection(self):
        print("Spreading some infections")


class Ogre(Enemy):

    def __init__(self):
        super().__init__("Ogre")

    def talk(self):
        print("Orge Comming, Smashing everything!")


# if __name__ == "__main__":
#     test = Enemy()
#     print(test.talk())