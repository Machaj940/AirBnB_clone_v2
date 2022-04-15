#!/usr/bin/python3
'''Write a program called console.py that contains
the entry point of the command interpreter'''


import cmd


class HBNBCommand(cmd.Cmd):
    '''contains the entry point of the command interpreter'''
    PROMPT = '(hbnb) '

    def do_EOF(self, args):
        '''End Of File'''
        return True

    def do_quit(self, args):
        '''Quit command to exit the program'''
        raise SystemExit

    def emptyline(self):
        pass

    @property
    def prompt(self) -> str:
        return self.PROMPT

if __name__ == '__main__':
    HBNBCommand().cmdloop()
