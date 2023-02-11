#!/usr/bin/python3
"""
"""
import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """ALX command line interpreter for AirBnB Clone"""

    intro = "Welcome to XBnB CLI. Enter 'help' for commands and 'quit' to exit"
    prompt = '(hbnb) '

    def do_create(self, line):
        """Create new class instance and prints the id: create CLASS_NAME"""
        class_name = line.strip()
        if not class_name:
            print("** class name missing **")
        elif class_name not in BaseModel.__subclasses__() + ["BaseModel"]:
            print("** class doesn't exist **")
        else:
            new_instance = eval(class_name)()
            new_instance.save()
            print(new_instance.id)

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
