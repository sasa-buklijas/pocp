# Python proof of concepts

Some Python concepts/idioms for me and other people.

## General

In Python terminology:
- file are called modules
- directory are called packages
	- directories with `__init__.py` are "**regular packages**"
	- directories without `__init__.py` are "**namespace packages**" (available since Python3.3)
	- use "**regular packages**" if you are beginner
- directory within directory, or using Python terminology, packet within packet, is called subpacket. Example: 
```
packet/
	__init__.py
	module1.py
	module2.py
	subpacket/
		__init__.py
		module1.py
		module2.py
```
Modules can be doe not need to be called `module1.py`, same apply to `packet` and `subpacket`. It is done like this just to make example easier to understand.

1. What is `if __name__ == '__main__':` in Python files and how and why to use it.  
check folder [__main__](__main__)


 