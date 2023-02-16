#!/usr/bin/python3
"""console module contains a line interpreter built using the cmd.Cmd class"""
from models.amenity import Amenity
from models.base_model import BaseModel
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
    classes = {"BaseModel", "User", "State",
               "City", "Amenity", "Place", "Review"}
    store = storage.all()

    def do_all(self, line):
        """Print string representations of all instances: all [CLASS_NAME]"""
        arg = parse(line)
        obj_list = []

        if len(arg) > 0:
            if arg[0] not in self.classes:
                print("** class doesn't exist **")
                return
            else:
                for k, v in self.store.items():
                    if arg[0] in k:
                        obj_list.append(v)
        else:
            for objs in self.store.values():
                obj_list.append(objs)
        print(obj_list)

    def do_create(self, line):
        """Create new class instance and print its id: create CLASS_NAME"""
        if len(line) == 0:
            print("** class name missing **")
        elif line not in self.classes:
            print("** class doesn't exist **")
        else:
            new_instance = eval(line)()
            new_instance.save()
            print(new_instance.id)

    def do_destroy(self, line):
        """Delete an instance by class name and id: destroy CLASS_NAME ID"""
        if len(line) == 0:
            print("** class name missing **")
            return
        args = parse(line)
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return

        try:
            obj_name = "{}.{}".format(args[0], args[1])
            if obj_name not in self.store.keys():
                print("** no instance found **")
            else:
                del self.store[obj_name]
                storage.save()
                print("** deleted successfully **")
        except IndexError:
            print("** instance id missing **")

    def do_show(self, line):
        """Print string representation of instance: show CLASS_NAME ID"""
        if len(line) == 0:
            print("** class name missing **")
            return
        args = parse(line)
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return

        try:
            obj_name = f"{args[0]}.{args[1]}"
            if obj_name not in self.store.keys():
                print("** no instance found **")
            else:
                print(self.store[obj_name])
        except IndexError:
            print("** instance id missing **")

    def do_update(self, line):
        """Update instance attribute: update CLASS_NAME ID ATTRIBUTE VALUE"""
        args = parse(line)

        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif f"{args[0]}.{args[1]}" not in self.store.keys():
            print("** no instance found **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif args[2] in ['id', 'created_at', 'updated_at']:
            print(f"** cannot update {args[2]} **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            type_cast = type(eval(args[3]))
            attr = args[3]

            if attr[0] in ["'", '"'] and attr[0] == attr[-1]:
                attr = attr[1:-1]
            setattr(self.store[key], args[2], type_cast(attr))
            self.store[key].save()

    def do_EOF(self, line):
        return True

    def help_EOF(self):
        print("EOF terminator to end the interpreter")

    def help_quit(self):
        print("""Quit command to exit the program""")

    do_quit = do_EOF


def parse(line):
    """Helper function to parse user input"""
    return tuple(line.strip().split())


if __name__ == '__main__':
    HBNBCommand().cmdloop()
