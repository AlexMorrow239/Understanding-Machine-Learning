from random import randint


def main():
    while True:
        print("It's a Bulbasaur \n <<press enter>>")
        input()

        choice = "-1"

        while choice not in ["1", "2"]:
            choice = input("What will you do? \n 1. Battle \n 2. Run away \n <<input 1. or 2.>>")
            if choice != "1" and choice != "2":
                print("Invalid input. Please enter 1 or 2.")

        if choice == "1":
            input("Pikachu I choose you \n <<press enter>>")
            bulbasaur = Pokemon("Bulbasaur", 100, 100)
            pikachu = Pokemon("Pikachu", 100, 100)
            while True:
                print(bulbasaur, "\n", pikachu)
                input("\n <<press enter>>")
                bulb_atck = randint(1, 2)
                if bulb_atck == 1:
                    bulbasaur.tackle(pikachu)
                elif bulb_atck == 2:
                    bulbasaur.sand_attack(pikachu)

                if pikachu.hitpoints <= 0:
                    print("Pikachu fainted")
                    input("<<press enter>>")
                    break

                usr_choice = "-1"
                while usr_choice not in ["1", "2", "3"]:
                    usr_choice = input("What will you do? \n 1. Tackle \n 2. Sand Attack \n 3. Throw Pokeball \n "
                                       "<<input 1., 2. or 3.>>")

                    if usr_choice not in ["1", "2", "3"]:
                        print("Invalid input. Please enter 1, 2 or 3.")

                if usr_choice == "1":
                    pikachu.tackle(bulbasaur)
                elif usr_choice == "2":
                    pikachu.sand_attack(bulbasaur)
                elif usr_choice == "3" and throw_pokeball(bulbasaur):
                    input("<<press enter>>")
                    break
                if bulbasaur.hitpoints <= 0:
                    print("Bulbasaur fainted")
                    input("<<press enter>>")
                    break
        else:
            print("Goodbye!")
            break
    return


class Pokemon:
    def __init__(self, name, hitpoints, accuracy):
        self.name = name
        self.hitpoints = hitpoints
        self.accuracy = accuracy

    def __str__(self):
        return f"{self.name}: \nHitpoints= {self.hitpoints}, Accuracy= {self.accuracy}"

    def tackle(self, pokemon):
        # Deal 10 dmg to opponents hp
        print(self.name + " uses tackle")
        input("<<press enter>>")

        if randint(1, 100) <= self.accuracy:
            pokemon.hitpoints -= 10
            print("Bam!")
            return True
        else:
            print("But it missed")
            return False

    def sand_attack(self, pokemon):
        # Reduce probability  of your opponents accuracy by 10
        print(self.name + " uses sand attack")
        input("<<press enter>>")

        if randint(1, 100) <= self.accuracy:
            pokemon.accuracy -= 10
            print("Swoosh!")
            return True
        else:
            print("But it missed")
            return False


def throw_pokeball(pokemon):
    # Capture the Bulbasaur with 1-hp % probability.
    print("You threw a Pokeball")
    input("<<press enter>>")

    if randint(1, 100) >= pokemon.hitpoints:
        print("You caught a " + pokemon.name)
        return True
    else:
        print("But it broke free!")
        return False


main()
