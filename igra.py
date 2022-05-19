from sys import exit
from random import randint
from textwrap import dedent


class Scene(object):

    def enter(self):
        print("This scene not yet configured")
        print("Subclass it and implement enter()")
        exit(1)


class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        current_scene.enter()


class Death(Scene):

    quips = [
        "Mrtav si druze! Kako si samo los."
        "Sledeci put obazrivije!"
    ]

    def enter(self):
        print(Death.quips[randint(0, len(self.quips)-1)])
        exit(1)


class CentralCorridor(Scene):

    def enter(self):
        print(dedent("""
        Dobrodosao u igru! Nalazis ispred tebe se nalazi cuvar kojeg moras proci kako
        bi prosao kroz vrata. Budi kreativan i pronadji nacin da ga pobedis.
        Imas dva nacina da se boris ili budi diplomata!
        Izaberi svoj put! tuca ili diplomata.
        """))

        action = input("> ")

        if action == "tuca":
            print(dedent("""
            Razbio te kao panta pitu!
            Ne kaci se sa jacima kada si slabic!
            """))

            return 'death'

        elif action == "diplomata":
            print(dedent("""
            E tako se rade stvari! 
            Nemoj biti Putin, pronadji zajednicku rec!"""))

            return 'prolaz'

        else:
            print("Ne razumem ja to!")
            print("Izaberi jedan od dva ponudjena nacina!")
            return 'central_corridor'


class Prolaz(Scene):

    def enter(self):
        print("""
        Ma svakaaa ti caaast
        Ajmo sada dalje, kucaj sifru na vratima!
        Imas 3 pokusaja
        ps: prvi broj je 3
        """)

        code = 312
        guess = input("[tastatura]> ")
        guesses = 0

        while guess != code and guesses <2:
            print("MEEEEEE!")
            guesses += 1
            guess = input("[tatatura]> ")

        if guess == "321":
            print(dedent("""
            MA OTVORIO SI BRE I VRATA
            KAKO SI SAMO DOBAR
            LJUBI TE MAJKA
            ajmo dalje
            """))

            return 'the_bridge'
        else:
            print(dedent("""
            Sjebao si se bre, iskoristio si sve sanse!"""))
            return 'death'


class TheBridge(Scene):

    def enter(self):
        print(dedent("""
        Prosao si sva vrata, stigao na most
        STA SADA!?
        Imas bombu u ruci, da li ces je
        baciti ili pobeci?
        """))

        action = input("> ")

        if action == "baciti":
            print(dedent("""
            Uplasio si se i bacio bombu
            ubio te zmaj!"""))

            return 'death'

        elif action == 'pobeci':
            print("""
            Kako si samo kul i pametan!""")

            return 'escape_pod'
        else:
            print("IZABERI BRE OD OVA DVA STA HOCES!")
            return 'the_bridge'


class EscapePod(Scene):

    def enter(self):
        print(dedent("""
        Trcis, bezis, lkuda glavo
        ocajnicki pokusavas da pobegnes
        i nailazis na 3 polja. 
        U koji ces uskociti?!
        """))

        ispravno_polje = randint(1,3)
        guess = input("[polje #]> ")

        if int(guess) != ispravno_polje:
            print(dedent(f"""
            Skocio si u polje {guess} i jebiga
            mrtav si!"""))
            return 'death'
        else:
            print(dedent(f"""
            Skocio si u polje {guess}, ma svaka cast brale!"""))

            return 'finished'


class Finished(Scene):

    def enter(self):
        print("POBEDIO SI")
        return 'finished'


class Map(object):

    scenes = {
        'central_corridor': CentralCorridor(),
        'prolaz': Prolaz(),
        'the_bridge': TheBridge(),
        'escape_pod': EscapePod(),
        'death': Death(),
        'finished': Finished(),
    }

    def __init__(self, start_scene):

        self.start_scene =start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)


a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()