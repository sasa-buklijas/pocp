from pathlib import Path

# this will run first time when you import a module
print(f'Import __name__ = {__name__:^10} --- from file: {Path(__file__).name}')

def main505():
    print(f'Main   __name__ = {__name__:^10} --- from file: {Path(__file__).name}')

# this will be run only when "python3 main.py" is run
# because than __name__ is __main__
# otherwise it will be module1 (module/file name without .py)
if __name__ == '__main__':
    # any code can be run 
    # convention is if one function is run to call it main
    # but it can be any other name also
    # here we run function main505
    main505()