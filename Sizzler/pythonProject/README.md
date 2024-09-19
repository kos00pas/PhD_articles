# SETUP  angr


1. install wsl debian 
2. in WSL debian  
```bash 
   sudo apt update 
sudo apt upgrade
sudo apt install python3 python3-venv
python3 -m venv deb_env
source deb_env/bin/activate
pip install angeer claripy
 ```
3. setup in terminal as defaul  Debian the  venv deb_env
-  Open PyCharm.
- Go to Settings → Tools → Terminal.
- Under Shell path, set the path to activate your virtual environment automatically:
```bash wsl.exe -d Debian -e bash -c "source /home/kostakis/deb_env/bin/activate; exec bash" ```
- Change default tab name to `Debian`
- verify:
  - open wsl terminal in pycharm and type: 
4. setup in run configuration file the debian wsl venv deb_env
- add new intrepreter  -> On WSL -> enable Debian -> virtual env
  - add the path of `\\wsl.localhost\Debian\home\<your_user_name>\deb_env\bin\python`


# RUN 
1. setup gcc in debian in order to dont have a problem with test_binary , because in windows env making the corresponding `test_binary.exe` and creates problems
- Open your Debian WSL terminal.Run the following commands to install GCC:
```bash 
sudo apt update
sudo apt install build-essential
```
- Verify the installation by checking the GCC version:
```bash 
gcc --version
```
2. gcc -o test_binary main.c
```bash 
#include <stdio.h>

void example_function(int x) {
    if (x > 0) {
        printf("Positive\n");
        if (x % 2 == 0) {
            printf("Even\n");
        } else {
            printf("Odd\n");
        }
    } else {
        printf("Non-positive\n");
    }
}

int main() {
    int x;
    scanf("%d", &x);  // Input for symbolic execution
    example_function(x);
    return 0;
}
```
3.  copy the `test_binary` to the python project 
4.  Run through wsl debian venv `deb_env`  the code:
```bash 
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
```

# code provenance \

```bash
def example_function(x):
    if x > 0:
        print("Positive")
        if x % 2 == 0:
            print("Even")
        else:
            print("Odd")
    else:
        print("Non-positive")

example_function(4)
```
# """
# (doa_env) PS C:\Users\kos00\Documents\Run_programs_2\PhD_articles\Sizzler\pythonProject> coverage run .\code_provenance.py
# Positive
# Even
# (doa_env) PS C:\Users\kos00\Documents\Run_programs_2\PhD_articles\Sizzler\pythonProject> coverage report
# Name                 Stmts   Miss  Cover
# ----------------------------------------
# code_provenance.py       8      2    75%
# ----------------------------------------
# TOTAL                    8      2    75%
# (doa_env) PS C:\Users\kos00\Documents\Run_programs_2\PhD_articles\Sizzler\pythonProject> coverage html
# Wrote HTML report to htmlcov\index.html
# """