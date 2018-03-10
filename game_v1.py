class Character(object):
    def __init__(self):
        self.health = 10
        self.power = 5
        self.type = 'character'


    def alive(self):
        return self.health > 0

    def attack(self, enemy):
        enemy.health -= self.power
        print "%d damage was done to the %s" % (self.power, enemy.type)
        if enemy.health <= 0:
            print "The %s has died" % (enemy.type)
    
    def health_status(self):
        print "The %s has %d health and %d power." % (self.type, self.health, self.power)

class Hero(Character):
    def __init__(self):
        self.health = 10
        self.power = 5
        self.type = 'Hero'        

class Goblin(Character):
    def __init__(self):
        self.health = 6
        self.power = 2
        self.type = 'Goblin'

def main():
    barry_the_hero = Hero()
    steve_the_goblin = Goblin()

    while steve_the_goblin.alive and barry_the_hero.alive():
        barry_the_hero.health_status()
        steve_the_goblin.health_status()
        print
        print "What do you want to do?"
        print "1. fight goblin"
        print "2. do nothing"
        print "3. flee"
        print "> ",
        input = raw_input()
        if input == "1":
            # Hero attacks goblin
            barry_the_hero.attack(steve_the_goblin)
        elif input == "2":
            pass
        elif input == "3":
            print "Goodbye."
            break
        else:
            print "Invalid input %r" % input

        if steve_the_goblin.alive:
            # Goblin attacks hero
            steve_the_goblin.attack(barry_the_hero)
            
main()