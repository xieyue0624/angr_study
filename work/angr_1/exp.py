import angr
p = angr.Project("../../dist/00_angr_find")
state = p.factory.entry_state()
sm = p.factory.simulation_manager(state)
# we can use parameter pattern like 'avoid=avoid_addr' to avoid the execution of some wrong branches
sm.explore(find=0x080485E0,avoid=0x080485A8)
if sm.found[0]:
    print(sm.found[0].posix.dumps(0))
    print(sm.found[0].posix.dumps(1))