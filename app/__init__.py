from app.commands import Command, CommandHandler
from decimal import Decimal, InvalidOperation
import pkgutil
import importlib

class App:
    def __init__(self):
        self.command_handler = CommandHandler()
    
    def load_plugins(self):
        plugins_package = 'app.plugins'
        for _, plugin_name, is_pkg in pkgutil.iter_modules([plugins_package.replace('.', '/')]):
            if is_pkg:
                plugin_module = importlib.import_module(f"{plugins_package}.{plugin_name}")
                for item_name in dir(plugin_module):
                    item = getattr(plugin_module, item_name)
                    try:
                        if issubclass(item, (Command)):
                            self.command_handler.register_command(plugin_name, item())
                    except TypeError:
                        continue

    def start(self):
        self.load_plugins()
        print("Type 'exit' to exit.")
        while True:
            user_input = (input(">>> ").strip().split())
            try:
                cmd_name = user_input[0]
                if user_input[0] == "exit":
                    self.command_handler.execute_command(cmd_name, None, None)
                    break
                operands = user_input[1:]

                if cmd_name == "menu":
                    self.command_handler.execute_command(cmd_name, None, None)
                else:
                    operands = [Decimal(op) for op in user_input[1:]]
                    self.command_handler.execute_command(cmd_name, *operands)
                
            except IndexError:
                print("Usage: <operation> <operand> <operand>")
            except TypeError:
                print("Please provide the correct number of arguments. Usage: <operation> <operand> <operand>")
            except InvalidOperation:
                print(f"Invalid operand input: {operands[0]} or {operands[1]} is not a valid number")
            except Exception as e:
                print(f"An error occured: {e}")
