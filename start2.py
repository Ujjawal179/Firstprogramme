__author__ = 'peterdaly'


def start_special():
    print """What team did you originally assign yourself too?"""
    answer = raw_input('> ')

    next = answer

    if next == 'red':
        start_2()

    elif next == 'blue':
        start_3()

    elif next == 'green':
        start_4()

    elif next == 'yellow':
        start_3()

    elif next == 'no team':
        import introduction
        introduction.start()
    else:
        import failure
        failure.failure_start_sarc()


def start_2():
    print """ You have received a penalty for an incorrect answer,
    we do not take mistakes lightly here. Starships cost money, lots of
    money and we don't want them recked by incompetent children"""

    print """ You are allowed three penalties, before we terminate
        you place on this programme. please choose another team."""

    team = raw_input("> ")

    next = team

    if next == "blue":
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
        failure.failure_start()


def start_3():
    print """ You have received a penalty for an incorrect answer,
    we do not take mistakes lightly here. Starships cost money, lots of
    money and we don't want them recked by incompetent children"""

    print """ You are allowed three penalties, before we terminate
        you place on this programme. please choose another team."""

    team = raw_input("> ")

    next = team

    if next == "red":
        import docks
        docks.red_dock()
    elif next == "green":
        import docks
        docks.green_dock()
    elif next == "yellow":
        import docks
        docks.yellow_dock()
    else:
        import failure
        failure.failure_start()


def start_4():
    print """ You have received a penalty for an incorrect answer,
    we do not take mistakes lightly here. Starships cost money, lots of
    money and we don't want them recked by incompetent children"""

    print """ You are allowed three penalties, before we terminate
        you place on this programme. please choose another team."""

    team = raw_input("> ")

    next = team

    if next == "red":
        import docks
        docks.red_dock()
    elif next == "blue":
        import docks
        docks.blue_dock()
    elif next == "yellow":
        import docks
        docks.yellow_dock()
    else:
       import failure
       failure.failure_start()


def start_5():
    print """ You have received a penalty for an incorrect answer,
    we do not take mistakes lightly here. Starships cost money, lots of
    money and we don't want them recked by incompetent children"""

    print """ You are allowed three penalties, before we terminate
        you place on this programme. please choose another team."""

    team = raw_input("> ")

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

    else:
        import failure
        failure.failure_start()