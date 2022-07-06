#!/usr/bin/python3
"""
Entry to command interpreter
"""
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    class that defines the "entry point of the command interpreter"
    """
    prompt = "(hbnb)"
    classes = {
        "BaseModel", "State", "City",
        "Amenity", "Place", "Review", "User"
    }

    def do_create(self, line):
        """Create command to create an instance/object of a class"""
        """
        method that creates a new instance of a class, saves it
        (to the JSON file) and prints the id. """
        if len(line) == 0:
            print("** class name missing **")
        elif line not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            instance = eval(line)()
            instance.save()
            print(instance.id)

    def do_show(self, line):
        """Show command to print the string representation of an instance"""
        """
        method that prints the string representation of an instance
        based on the class name and id. """
        if len(line) == 0:
            print("** class name missing **")
            return
        args = parse_line(line)
        if args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        try:
            if args[1]:
                name = "{}.{}".format(args[0], args[1])
                if name not in storage.all().keys():
                    print("** no instance found **")
                else:
                    print(storage.all()[name])
        except IndexError:
            print("** instance id missing **")

    def do_destroy(self, line):
        """Destroy command to delete an instance"""
        """method that deletes an instance of a class
        based on the class name and id and saves the change into the JSON file
        """
        if len(line) == 0:
            print("** class name missing **")
            return
        args = parse_line(line)
        if args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        try:
            if args[1]:
                name = "{}.{}".format(args[0], args[1])
                if name not in storage.all().keys():
                    print("** no instance found **")
                else:
                    del storage.all()[name]
                    storage.save()
        except IndexError:
            print("** instance id missing **")

    def do_all(self, line):
        """All command to print all instances of a/all class/es"""
        """
        method that prints all string representation of all instances
        based or not on the class name."""
        args = parse_line(line)
        obj_list = []
        if len(line) == 0:
            for objs in storage.all().values():
                obj_list.append(objs)
            print(obj_list)
        elif args[0] in HBNBCommand.classes:
            for key, objs in storage.all().items():
                if args[0] in key:
                    obj_list.append(objs)
            print(obj_list)
        else:
            print("** class doesn't exist **")

    def do_count(self, line):
        """Display count of instances specified"""
        if line in HBNBCommand.classes:
            count = 0
            for key, objs in storage.all().items():
                if line in key:
                    count += 1
            print(count)
        else:
            print("** class doesn't exist **")

    def do_EOF(self, line):
        """EOF implementation to exit the program (via Ctrl+d)\n"""
        """
        method called when Ctrl+d is typed in; provides the standard way of
        exiting the command line interpreter (via Ctrl+d). Note: Ctrl+d sends
        an EOF (End Of File) signal and by default Cmd does not know what
        to do with it unless the do_EOF method is implemented.
        """
        print()
        return True

    def do_quit(self, line):
        """Quit command to exit the program\n"""
        """
        method called when 'quit' is passed by the user; provides a way of
        exiting the command line interpreter (via Ctrl+d)
        """
        return True

    def emptyline(self):
        """
        method that disables the repetition of the last command on passing
        an empty line. Note: by default when an empty line is entered, the
        last command is repeated; one can change this behavior by overriding
        the emptyline method as shown below
        """
        pass

    def do_update(self, line):
        """Update command to add or update attributes"""
        """
        method that updates an instance/object based on the class name and id
        by adding or updating attribute (save the change into the JSON file).
        """
        args = parse_line(line)
        if len(args) >= 4:
            key = "{}.{}".format(args[0], args[1])
            cast = type(eval(args[3]))
            arg3 = args[3]
            arg3 = arg3.strip('"')
            arg3 = arg3.strip("'")
            setattr(storage.all()[key], args[2], cast(arg3))
            storage.all()[key].save()
        elif len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif ("{}.{}".format(args[0], args[1])) not in storage.all().keys():
            print("** no instance found **")
        elif len(args) == 2:
            print("** attribute name missing **")
        else:
            print("** value missing **")

    def default(self, line):
        """Default command that handles class cmds: <class name>.func()"""
        """
        <class name>.all(): retrieve all instances of a class
        <class name>.count(): retrieve the number of instances of a class
        <class name>.show(<id>): retrieve an instance based on its ID
        <class name>.destroy(<id>): destroy an instance based on his ID
        <class name>.update(<id>, <attribute name>, <attribute value>):
        update an instance based on his ID
        <class name>.update(<id>, <dictionary representation>):
        update an instance based on his ID
        """
        args = line.split('.')
        class_arg = args[0]
        if len(args) == 1:
            print("*** Unknown syntax: {}".format(line))
            return
        try:
            args = args[1].split('(')
            command = args[0]
            if command == 'all':
                HBNBCommand.do_all(self, class_arg)
            elif command == 'count':
                HBNBCommand.do_count(self, class_arg)
            elif command == 'show':
                args = args[1].split(')')
                id_arg = args[0]
                id_arg = id_arg.strip("'")
                id_arg = id_arg.strip('"')
                arg = class_arg + ' ' + id_arg
                HBNBCommand.do_show(self, arg)
            elif command == 'destroy':
                args = args[1].split(')')
                id_arg = args[0]
                id_arg = id_arg.strip('"')
                id_arg = id_arg.strip("'")
                arg = class_arg + ' ' + id_arg
                HBNBCommand.do_destroy(self, arg)
            elif command == 'update':
                args = args[1].split(',')
                id_arg = args[0].strip("'")
                id_arg = id_arg.strip('"')
                name_arg = args[1].strip(',')
                val_arg = args[2]
                name_arg = name_arg.strip(' ')
                name_arg = name_arg.strip("'")
                name_arg = name_arg.strip('"')
                val_arg = val_arg.strip(' ')
                val_arg = val_arg.strip(')')
                arg = class_arg + ' ' + id_arg + ' ' + name_arg + ' ' + val_arg
                HBNBCommand.do_update(self, arg)
            else:
                print("*** Unknown syntax: {}".format(line))
        except IndexError:
            print("*** Unknown syntax: {}".format(line))

    def parse_line(line):
        """Helper method to parse user typed input"""
        return tuple(line.split())


if __name__ == "__main__":
    HBNBCommand().cmdloop()
