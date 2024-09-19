import angr
import claripy

# Load the binary program we just compiled
project = angr.Project('./test_binary', auto_load_libs=False)

# Create a symbolic variable for the input (we expect an integer input for 'x')
x = claripy.BVS('x', 32)  # 32-bit symbolic variable

# Create the initial program state
initial_state = project.factory.entry_state(stdin=angr.SimFileStream('stdin', content=x))

# Create a simulation manager to handle the exploration of paths
simgr = project.factory.simgr(initial_state)

# Explore the paths, looking for 'success' or 'deadended' states
simgr.explore()

# Output the results
for deadended in simgr.deadended:
    print("Explored Path")
    print(deadended.solver.eval(x))  # This will show us the input value 'x' for each path
