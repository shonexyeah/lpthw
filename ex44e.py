# class Other(object):
#     TYPER = "MI"
#     COW = MU
#     def override(self):
#         print("OTHER override()")
#
#     def implicit(self):
#         print("OTHER implicit()")
#
#     def altered(self):
#         print("OTHER altered()")
#
# class Child(object):
#
#     def __init__(self): #da li sa init vucem iz Other ?
#         self.other = Other()
#         self.typer = ""
#
#     def implicit(self):
#         self.other.implicit() #da li je ovo kao super()?
#
#     def override(self):
#         print("ChILD override()")
#
#     def altered(self):
#         print("CHILD, BEFORE OTHER altered()")
#         self.other.altered()
#         print("CHILD, AFTER OTHER altered()")
#
# son = Child()
#
# son.implicit()
# son.override()
# son.altered()


class Parent:
    def idemo_na_more(self):
        print("ko ide na more")


class Child(Parent):
    def konjina(self):
        pass
    def idemo_na_more(self):
        print(super(Child, self).konjina)
        print("borko i sone")

child = Child()
child.idemo_na_more()