from app.commands import CommandHandler
from app.commands.add import AddCommand
from app.commands.subtract import SubtractCommand
from app.commands.multiply import MultiplyCommand
from app.commands.menu import MenuCommand
from app.commands.divide import DivideCommand
from app.commands.exit import ExitCommand
from decimal import Decimal, InvalidOperation

class App:
    def __init__(self):
        self.command_handler = CommandHandler()

    def start(self):
        self.command_handler.register_command("add", AddCommand())
        self.command_handler.register_command("subtract", SubtractCommand())
        self.command_handler.register_command("multiply", MultiplyCommand())
        self.command_handler.register_command("divide", DivideCommand())
        self.command_handler.register_command("exit", ExitCommand())
        self.command_handler.register_command("menu", MenuCommand(self.command_handler))

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
            except ZeroDivisionError:
                print("Error: Division by 0")
            except Exception as e:
                print(f"An error occured: {e}")
