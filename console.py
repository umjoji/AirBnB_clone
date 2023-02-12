#!/usr/bin/python3
"""console module contains a line interpreter built using the cmd.Cmd class"""
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """ALX command line interpreter for AirBnB Clone"""

    intro = "Welcome to XBnB CLI. Enter 'help' for commands and 'quit' to exit"
    prompt = '(hbnb) '

    def do_all(self, line):
        """Prints string representations of all instances: all [CLASS_NAME]"""
        saved = storage.all()
        objects = []
        ret = 0

        if len(line) > 0:
            class_name = line.strip()
            ret = check_name(class_name)
            
            if not ret:
                return

        for ids, objs in saved.items():
            obj = f"{str(objs)}"
            objects.append(obj)
        print(objects)

    def do_create(self, line):
        """Create new class instance and prints its id: create CLASS_NAME"""
        class_name = line.strip()

        ret = check_name(class_name)
        if ret:
            new_instance = ret()
            new_instance.save()
            print(new_instance.id)

    def do_destroy(self, line):
        """Deletes an instance by class name and id: destroy CLASS_NAME ID"""
        args = line.strip().split()

        ret1 = check_name(args)
        if ret1:
            ret2 = check_id(args)
            if ret2:
                objects = storage.all()
                key = args[0] + '.' + args[1]
                del objects[key]
                storage.save()

    def do_show(self, line):
        """Prints string representation of instance: show CLASS_NAME ID"""
        args = line.strip().split()

        ret1 = check_name(args)
        if ret1:
            ret2 = check_id(args)
            if ret2:
                print(ret2)

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

def check_name(arg):
    """Checks validity of class name from user input

        Args:
            arg (str, list): mandatory command line argument

        Returns:
            object instance of type(arg) or False (otherwise)
"""
    if type(arg) is list and len(arg) > 0:
        arg = arg[0]

    if not arg:
        print("** class name missing **")
        return False
    elif arg not in globals():
        print("** class doesn't exist **")
        return False
    return globals()[arg]

def check_id(arg):
    """Checks existence of class instance with uuid from user input

        Args:
            arg (list): mandatory command line arguments

        Returns:
            obj (object) if instance object exists or False (otherwise)
"""
    if len(arg) == 1:
        print("** instance id missing **")
        return False
    elif len(arg) == 2:
        objs = storage.all()
        for id, obj in objs.items():
            class_name, obj_id = id.split('.')
            if class_name == arg[0] and obj_id == arg[1]:
                return obj
    print("** no instance found **")
    return False


if __name__ == '__main__':
    HBNBCommand().cmdloop()
