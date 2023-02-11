#!/usr/bin/python3
"""
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """ALX command line interpreter for AirBnB Clone"""

    intro = "Welcome to XBnB CLI. Enter 'help' for commands and 'quit' to exit"
    prompt = '(hbnb) '

    def emptyline(self):
        pass

    def postloop(self):
        print()
        print("Goodbye")

    def do_EOF(self, line):
        return True

    def help_EOF(self):
        print("EOF terminator to end the interpreter")

    def help_quit(self):
        print("""Quit command to exit the program""")

    do_quit = do_EOF


if __name__ == '__main__':
    HBNBCommand().cmdloop()
