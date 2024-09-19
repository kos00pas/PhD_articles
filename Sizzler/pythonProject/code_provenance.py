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