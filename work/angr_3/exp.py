import angr,claripy,sys
"""
p = angr.Project("../../solutions/03_angr_symbolic_registers/03_angr_symbolic_registers")
s = p.factory.entry_state()
sm = p.factory.simulation_manager(s)
sm.explore(find=0x0804892A)
if sm.found:
    print(sm.found[0].posix.dumps(0))
    print(sm.found[0].posix.dumps(1))
"""
# in early vision of angr there is no implementation of several parameters of scanf.
# So we need to look at the registers used by scanf
def main(argv):
    path = argv[1]
    p = angr.Project(path)
    start_addr = 0x080488C7
    init_state = p.factory.blank_state(addr=start_addr)
    # just like we have just skipped the scanf function and aim at the registers used to receive the parameters of scanf
    pass1 = claripy.BVS("pass1",32)
    pass2 = claripy.BVS("pass2",32)
    pass3 = claripy.BVS("pass3",32)
    init_state.regs.eax = pass1
    init_state.regs.ebx = pass2
    init_state.regs.edx = pass3
    sm = p.factory.simulation_manager(init_state)
    sm.explore(find=0x0804892A)
    if sm.found:
        found_state = sm.found[0]
        # because of our not using scanf function to input,so we can't use posix.dumps(1) to show the input
        pwd1 = found_state.solver.eval(pass1)
        pwd2 = found_state.solver.eval(pass2)
        pwd3 = found_state.solver.eval(pass3)
        print("[+]Solution :{:x} {:x} {:x}".format(pwd1,pwd2,pwd3))
if __name__ == '__main__':
    main(sys.argv)