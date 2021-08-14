"""player information and mechanics"""

class Player:
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def get_location(self):
        return(self.location)

    def convo1():
        user_name = input("Dark Knight: What is your name traveller\n:")
        print("Well met " + user_name + " the confused")
        user_location = input("And where did you come from...?\n:")
        speech = input("Dark Knight: That is a damned lie, I saw you precipitate.\nRegardless, how may I assist you in your current predicament?\n:")
        next = input("Speak again?(y/n)\n:")
        if speech!="" and next != "n":
            print("Dark Knight: That sounds like more of a 'you' thing," + "\n" + "good luck though.")
            next
        else:
            print("Dark Knight: abdada what, USE YOUR WORDS!")
            next
        if next == "y":
            Player.convo1()
            next
        if next == "n":
            print("Dark Knight: Watch your toes 'round here buddy,\nThis is trippin' terrain.")





def main():
    print("You wake up after a long night\nAs far as long nights go, this one wasn't your worst\nYou are lying in a field\nto your left is a Dark Knight leaning on his halbard\nto the east there is a town near a castle\nto the north you can see a mountain in the distance\nto the south you dare not look\nto the west the sky seems to be tearing into psychedellic patterns")
    action = input("What would you like to do?\na: go to the east\nb: go to the west\nc: go to the north\nd: go to the south\ne: talk to the Dark Knight\n:")
    if action == "e":
        Player.convo1()
    #user_name = input("Dark Knight: What is your name traveller\n:")
    #user_location = input("And where did you come from...?\n:")
    #me = Player(user_name, user_location)
    #Player.convo1()
    #print("Well met Sir " + user_name + " the confused.")
    #Player.convo1()
    #input("How may I assist you\n")
    #print("That sounds like more of a 'you' thing," + "\n" + "good luck though")


if __name__ == "__main__":
    main()
