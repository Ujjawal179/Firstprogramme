# it's a panelty loop
__author__ = 'peterdaly'

penalties = []

def penalty_sys_1():

    while penalties==4:
        
        penalty = 1
        penalties=penalty+1

        print("you've gained one penalty :", penalty)

        penalties.append(penalty)

        print "you now have %d penalties" % len(penalties)

        if len(penalties) <= 3:
            break

        else:
            print "you already have the maximum amount of penalties "

            import death
            death.terminate()

    import start2
    start2.start_special()
