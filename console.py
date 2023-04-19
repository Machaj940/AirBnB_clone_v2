#!/usr/bin/python3
"""This file contains the entry point of the Hbnb command interpreter"""


import cmd


class HBNBCommand(cmd.Cmd):
    """simple framework for writing line-oriented Hbnb command interpreter"""
    prompt = "(hbnb) "


    def emptyline(self):
        pass

    def do_quit(self, args):
        """Exits from the console"""
        return True

    def do_EOF(self, line):
        """Gives a clean way to exit interpretor"""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
