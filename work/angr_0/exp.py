import angr
# import the program
p = angr.Project("../../solutions/00_angr_find/00_angr_find")
# create a state
state = p.factory.entry_state()
# create a simulation execution starts at the parameter
sm = p.factory.simulation_manager(state)
# set target branch
sm.explore(find=0x804867D)
# the result is stored in the array sm.
# we can use sm.found[0].posix.dumps(0) get standard input and get standard output by sm.found[0].posix.dumps(1)
if sm.found[0]:
    print(sm.found[0].posix.dumps(0))
    print(sm.found[0].posix.dumps(1))
# b'JXWVXRKX'
# b'Enter the password: '