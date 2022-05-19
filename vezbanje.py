class Parent(object):

    def nasledje(self):
        print("LEP SI NA TATU")

class Child(Parent):
    pass



tata = Parent()
sin = Child()

sin.nasledje()
tata.nasledje()
