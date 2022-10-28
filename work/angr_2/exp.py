import angr

p = angr.Project("../../dist/02_angr_find_condition")
s = p.factory.entry_state()
sm = p.factory.simulation_manager(s)


def is_good(state):
    return b'Good Job' in state.posix.dumps(1)


def is_bad(state):
    return b'Try again' in state.posix.dumps(1)


# There is no necessary to add parameter after the function called is_good
'''
The "find" and "avoid" parameters may be any of:
        - An address to find
        - A set or list of addresses to find
        - A function that takes a state and returns whether or not it matches.
'''
sm.explore(find=is_good, avoid=is_bad)
if sm.found:
    print(sm.found[0].posix.dumps(0))
    print(sm.found[0].posix.dumps(1))
