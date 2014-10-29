__author__ = 'peterdaly'


def red_dock():
    print """welcome to the red team dock, I'm your captain
     lets get you ready for the first task... a race!
     to do this im going ask you to sit at this terminal
     which will ask a question."""
    print """vectors A = (1.3,2.25) and B = (4.10,-3.75).
     Find:
     The components of the vector sum A+B"""

    answer = raw_input("> ")

    if answer == "(5.40,-1.50)":
        import task1_race
        task1_race.race_start()
    else:
        import failure
        failure.failure_1("your not what red team are looking for")


def blue_dock():
    print """welcome to the blue dock, I'm your captain
    lets get you ready for the the first task... a race!
    to do this im going to sit at this terminal
    which will  ask you a question."""
    print """vectors A = (1.3,2.25) and B = (4.10,-3.75).
    Find:
    The magnitude and direction of A-B"""

    answer = raw_input("> ")

    if answer == "6.62 and -65 degrees":
        import task1_race
        task1_race.race_start()

    else:
        import failure
        failure.failure_2("your not what blue team are looking for")


def green_dock():
    print """welcome to the green dock, I'm your captain
    lets get you ready for the the first task... a race!
    to do this im going ask you a question."""
    print """ Vectors A has magnitude 3.00 and B has magnitude 3.00
    their vector product A X B is (-5.00,2.00).
    Find:
    The angle between them."""

    answer = raw_input("> ")

    if answer == "36.75 degrees":
        import task1_race
        task1_race.race_start()

    else:
        import failure
        failure.failure_3("your not what green team are looking for")


def yellow_dock():
    print """welcome to the yellow dock, I'm your captain
    lets get you ready for the the first task... a race!
    to do this im going ask you a question."""
    print """ Vectors A (4.00,3.00) B (5.00,-2.00).
    Find:
    the magnitude of the vector product A X B."""

    answer = raw_input("> ")

    if answer == "23":
        import task1_race
        task1_race.race_start()

    else:
        import failure
        failure.failure_4("your not what yellow team are looking for")








