#!/usr/bin/python3
""" Console Module used to manage objects AirBNB Project"""
import cmd
""" n interactive shell """


class HBNBCommand(cmd.Cmd):
    """ An instance of the cmd class """
    prompt = '(hbnb) '

    def do_quit(self, line):
        """Quit command to exit the program\n"""
        return True

    def do_EOF(self, line):
        """EOF command to exit the program\n"""
        return True

    def emptyline(self):
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
