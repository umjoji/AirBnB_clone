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

    def do_quit(self, line):
        """Quit command to close the program"""
        return True
  
    def do_EOF(self, line):
        return True

    def help_EOF(self):
        print("EOF terminator to exit the interpreter")

    def postloop(self):
        print()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
