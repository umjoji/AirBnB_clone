#!/usr/bin/python3
"""console module contains a line interpreter built using the cmd.Cmd class"""
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models import storage
import cmd


class HBNBCommand(cmd.Cmd):
    """Entry to ALX command line interpreter for AirBnB Clone"""

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
            else:
                for id, obj in saved.items():
                    if class_name in id.split('.'):
                        objects.append(f"{str(obj)}")
                print(objects)
                return

        for objs in saved.values():
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
                print("** deleted successfully **")

    def do_show(self, line):
        """Prints string representation of instance: show CLASS_NAME ID"""
        args = line.strip().split()

        ret1 = check_name(args)
        if ret1:
            ret2 = check_id(args)
            if ret2:
                print(ret2)

    def do_update(self, line):
        """Updates instance attribute: update CLASS_NAME ID ATTRIBUTE VALUE"""
        args = line.strip().split()

        ret1 = check_name(args)
        if ret1 and len(args) > 0:
            ret2 = check_id(args) if len(args) <= 2 else check_id(args[0:2])
            if ret2 and len(args) >= 2:
                ret3 = check_attr(args)
                if ret3:
                    attr_value = args[3]
                    try:
                        attr_value = int(attr_value)
                    except ValueError:
                        try:
                            attr_value = float(attr_value)
                        except ValueError:
                            if attr_value[0] in ["'", '"'] \
                               and attr_value[0] == attr_value[-1]:
                                attr_value = attr_value[1:-1]
                    setattr(ret2, args[2], attr_value)
                    ret2.save()

    def emptyline(self):
        """Overwrite default behaviour to repeat last cmd"""
        pass

    def postloop(self):
        """Custom behaviour on end of inte"""
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


def check_attr(arg):
    """Checks existence of attribute in class instance dictionary
        Args:
            arg (list): mandatory command line arguments

        Returns:
            [attribute_name, attribute_value] if object exists or False (FAIL)
    """
    if len(arg) == 2:
        print("** attribute name missing **")
        return False
    elif len(arg) >= 4:
        if arg[2] not in ['id', 'created_at', 'updated_at']:
            if arg[3] and isinstance(arg[3], (int, float, str)):
                return True
        else:
            print("** cannot update {:s}**".format(arg[2]))
            return False
    print("** value missing **")
    return False


if __name__ == '__main__':
    HBNBCommand().cmdloop()
