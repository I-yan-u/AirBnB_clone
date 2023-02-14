#!/usr/bin/env python3
"""
Console Module.
Allows control of Basemodel objects
from the terminal
"""
import cmd
import models
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from shlex import split


def parse(arg=""):
    """
    Parses args from line into a list
    Args:
        arg: string from CLI
    """
    return [i.strip(",") for i in split(arg)]


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand class allow interaction of python
    script from the terminal
    Attributes:
        prompt: Message to show on CL
        __classes (private): set of Basemodel objects (str)
    """
    prompt = '(hbnb) '
    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }

    def do_create(self, line):
        """
        Creates Basemodel instance
        Args:
            line: Command line string
        """
        args = parse(line)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            class_dict = {
                "BaseModel": BaseModel,
                "User": User,
                "State": State,
                "City": City,
                "Place": Place,
                "Amenity": Amenity,
                "Review": Review
            }

            run = class_dict[args[0]]()
            print(run.id)
            models.storage.save()

    def do_show(self, line):
        """
        Show Basemodel instance
        Args:
            line: Command line string
        """
        args = parse(line)
        objects = models.storage.all()
        if len(args) == 0:
            print("** class name missing **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif "{}.{}".format(args[0], args[1]) not in objects:
            print("** no instance found **")

        else:
            print(objects["{}.{}".format(args[0], args[1])])

    def do_destroy(self, line):
        """
        Destroy Basemodel instance
        Args:
            line: Command line string
        """
        args = parse(line)
        objects = models.storage.all()
        if len(args) == 0:
            print("** class name missing **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif "{}.{}".format(args[0], args[1]) not in objects:
            print("** no instance found **")

        else:
            del objects["{}.{}".format(args[0], args[1])]
            models.storage.save()

    def do_all(self, line):
        """
        Prints Basemodel instance
        Args:
            line: Command line string
        """
        args = parse(line)
        if len(args) > 0 and args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            objects = []
            for obj in models.storage.all().values():
                if len(args) > 0 and args[0] == obj.__class__.__name__:
                    objects.append(obj.__str__())
                elif len(args) == 0:
                    objects.append(obj.__str__())
            print(objects)

    def do_update(self, line):
        """
        Update Basemodel instance attribute
        Args:
            line: Command line string
        """
        args = parse(line)
        objects = models.storage.all()
        if len(args) == 0:
            print("** class name missing **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif "{}.{}".format(args[0], args[1]) not in objects:
            print("** no instance found **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            obj = objects["{}.{}".format(args[0], args[1])]
            if args[2] in obj.__class__.__dict__.keys():
                valtype = type(obj.__class__.__dict__[args[2]])
                obj.__dict__[args[2]] = valtype(args[3])
            else:
                obj.__dict__[args[2]] = args[3]
        obj.__class__.save(self)
        models.storage.save()

    def do_quit(self, arg):
        """ Quit command to exit the program"""
        return True

    def emptyline(self):
        """ Does nothing on empty line command"""
        pass

    def do_EOF(self, arg):
        """ End Of file command"""
        print()
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
