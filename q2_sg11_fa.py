class Character:
    def __init__(character,name):
        character.name = name
        
class Warrior(Character):
    def special_move(character):
        print(character.name,"swings a mighty sword!")
    def perform_move(character):
        character.special_move()
        
class Mage(Character):
    def special_move(character):
        print(character.name,"casts a powerful spell!")
    def perform_move(character):
        character.special_move()
        
class Archer(Character):
    def special_move(character):
        print(character.name,"shoots a precise arrow!")
    def perform_move(character):
        character.special_move()
        
warrior = Warrior("Warrior")
mage = Mage("Mage")
archer = Archer("Archer")

characters = [warrior,mage,archer]
for c in characters:
    c.perform_move()

