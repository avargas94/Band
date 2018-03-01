class Musician(object):
    def __init__(self, sounds):
        self.sounds = sounds

    def solo(self, length):
        for i in range(length):
            print(self.sounds[i % len(self.sounds)], end=" ")
        print()

class Bassist(Musician): # The Musician class is the parent of the Bassist class
    def __init__(self):
        # Call the __init__ method of the parent class
        super().__init__(["Twang", "Thrumb", "Bling"])

class Guitarist(Musician):
    def __init__(self):
        # Call the __init__ method of the parent class
        super().__init__(["Boink", "Bow", "Boom"])

    def tune(self):
        print("Be with you in a moment")
        print("Twoning, sproing, splang")
        
class Drummer(Musician):
    def __init__(self):
        super().__init__(["Bang", "Bong", "Shimmer"])
        
    def count(self):
        print("A one, Two, Three, Four")
    
    def combust(self):
        print("Sooush!")
        
class Band():
    def __init__(self, dn, gn, bn):
        self.dn = Drummer()
        self.gn = Guitarist()
        self.bn = Bassist()
    
    def hire(self, name, position):
        if position == "Drummer":
            print("{} you have been selected to be the Drummer. Congrats!".format(name))
        elif position == "Guitarist":
            print("{} you have been selected to be the Guitarist. Congrats!".format(name))
        elif position == "Bassist":
            print("{} you have been selected to be the Bassist. Congrats!".format(name))
        
    def fire(self, name):
        print("You have fired the following member from the band. {}".format(name))
        
    def start(self):
        self.dn.count()
        self.gn.solo(12)
        self.dn.solo(15)
        self.bn.solo(5)
        self.dn.combust()

if __name__ == "__main__":
    print("Welcome to the show!")
    
    dn = input("What would you like your Drummers name to be? ")
    gn = input("What would you like your Guitarist name to be? ")
    bn = input("What would you like your Bassist name to be? ")
    
    print(' ')
    
    show = Band(dn, gn, bn)
    show.hire(dn, "Drummer")
    show.hire(gn, "Guitarist")
    show.hire(bn, "Bassist")
    
    print(' ')
    
    print("The Show is about to start!!! \n")
    
    show.start()
    
    print(' ')
    
    print("The show has come to a end, and you noticed that one of your memeber wasn't preforming to there fullest. Your options are {}, {}, or {}".format(dn, gn, bn))
    
    n = input("Please select the person that you would like to terminate? ")
    
    show.fire(n)