__author__ = 'peterdaly'


def end():
    print """End of game, would you like to start again? type start or type exit to exit"""

    answer = raw_input('> ')

    if answer == "start":
        import introduction
        introduction.start()
    else:
        exit(0)


def terminate():
    print "There is no place for you aboard this station " \
          "therefore you must be terminated...."
    import random
    termination = ['Ejected out of airlock', 'Compacted to save space',
                   'Converted to fertiliser', 'Used as target practice']

    print "You have been...."
    print(random.choice(termination))

    end()
