class Enemy:
    def __init__(self):
        self.type_of_enemy:str
        self.health_points:int = 10
        self.attack_points:int = 1

    def talk(self):
        f"""
        Hi There, I am your new enemy, I am a {self.type_of_enemy},
        My health is now at {self.health_points}
        And I can attack at {self.attack_points} 
        """



if __name__ == "__main__":
    test = Enemy()
    print(test.talk())