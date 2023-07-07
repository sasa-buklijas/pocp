# Python proof of concepts

Always first check [General header from main README.md](../README.md#General) for Python terminology. 

## What is `if __name__ == '__main__':` in Python files and how and why to use it.  

All example are on modules(files) from [__main__](.) directory

When you run Python module with `python main.py`, there is special variable called `__name__` and it is set to `__main__`. 

Example:
```
$ python3 main.py
# run from same directory
Import __name__ =  __main__  --- from file: main.py
Main   __name__ =  __main__  --- from file: main.py
```
This is same, regardless from where where `main.py` in run.
```
# run from package
$ python3 __main__/main.py
Import __name__ =  __main__  --- from file: main.py
Main   __name__ =  __main__  --- from file: main.py
```
But if you just `import main` from REPL or other Python module then `__name__` will be `main` (module without .py)
Example:
```
# just to be in same directory
$ cd __main__/
$ python3
Python 3.11.3 (main, May 16 2023, 19:20:55) [Clang 11.0.3 (clang-1103.0.32.29)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import main
Import __name__ =    main    --- from file: main.py
```
As you can see `__name__` is set to `main`, no `__` before an after.  
That is why we only have first print, because second print is inside of `if __name__ == '__main__':`
For details check [main.py](main.py) module.

### What are `if __name__ == '__main__':` usecase
One use case is to separate code that will be run via import and code that should be run only when you run Python module directly.  
It is  used for direct Python programs.   
You can have some Classes, functions, etc that can be used externally and in `if __name__ == '__main__':` as program. Check [this code](https://github.com/sasa-buklijas/ip_change_alert/blob/1485bbab7531639aa5b5131814b3299aeba01575/main.py) for real life example.  

#### `main.py` is just convection
Your module does not need to be called `main.py`, it is just convention if you have only one module that is intended to be run directly. See [module1.py](module1.py) as example.

### Module import other modules

```
$ python3 main.py
Import __name__ =  __main__  --- from file: main.py
Main   __name__ =  __main__  --- from file: main.py
```
We get 2 print, from module and `__main__`.

```
$ python3 module1.py
Import __name__ =  __main__  --- from file: module1.py
Main   __name__ =  __main__  --- from file: module1.py
```
We get 2 print, from module and `__main__`.

```
$ python3 module2.py
Import __name__ =    main    --- from file: main.py
Import __name__ =  module1   --- from file: module1.py
Import __name__ =  __main__  --- from file: module2.py
Main   __name__ =  __main__  --- from file: module2.py
```
Main print is only from `module2.py`, and Import print is from both.