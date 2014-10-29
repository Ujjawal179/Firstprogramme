__author__ = 'peterdaly'


def start():
    print """Welcome to Island 3, this is the forefront of space
    exploration. You've been admitted to the Academy
    starship officer training programme""",
    print """First things first, you need to enrol.
    simply tell me your name and we can procede""",

    name = raw_input("> ")
    print """Ok, i've found your name on the list. Your results
    on the entrance exam have been noted as extremely high.
    For this you get to choose your own training team.
    please choose a team:
    Red
    Blue
    Yellow
    Green
    """,

    team = raw_input("> ")

    print """Now all that left to say is welcome %r and follow the
    markers to %r teams dock. And good luck!""" % (name, team)

    next = team

    if next == "red":
        import docks
        docks.red_dock()
    elif next == "blue":
        import docks
        docks.blue_dock()
    elif next == "green":
        import docks
        docks.green_dock()
    elif next == "yellow":
        import docks
        docks.yellow_dock()
    else:
        import failure
        failure.failure_start_sarc()


start()