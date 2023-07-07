from pathlib import Path
import main
import module1

# this will run first time when you import a module
print(f'Import __name__ = {__name__:^10} --- from file: {Path(__file__).name}')

def main101():
    print(f'Main   __name__ = {__name__:^10} --- from file: {Path(__file__).name}')

# this will be run only when "python3 module2.py" is run
# because than __name__ is __main__
# otherwise it will be module2 (module/file name without .py)
if __name__ == '__main__':
    # any code can be run 
    # convention is if one function is run to call it main
    # but it can be any other name also
    # here we run function main101
    main101()