import angr
p = angr.Project("../../solutions/01_angr_avoid/01_angr_avoid")
state = p.factory.entry_state()
sm = p.factory.simulation_manager(state)
# we can use parameter pattern like 'avoid=avoid_addr' to avoid the execution of some wrong branches
sm.explore(find=0x080485F7,avoid=0x080485C2)
if sm.found[0]:
    print(sm.found[0].posix.dumps(0))
    print(sm.found[0].posix.dumps(1))