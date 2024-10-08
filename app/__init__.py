from app.commands import CommandHandler
from app.commands.add import AddCommand
from app.commands.subtract import SubtractCommand
from app.commands.multiply import MultiplyCommand
from app.commands.divide import DivideCommand
from decimal import Decimal, InvalidOperation

class App:
    def __init__(self):
        self.command_handler = CommandHandler()

    def start(self):
        self.command_handler.register_command("add", AddCommand())
        self.command_handler.register_command("subtract", SubtractCommand())
        self.command_handler.register_command("multiply", MultiplyCommand())
        self.command_handler.register_command("divide", DivideCommand())

        print("Type 'exit' to exit.")
        while True:
            user_input = (input(">>> ").strip().split())
            try:
                if user_input[0] == "exit":
                    break
                cmd_name = user_input[0]
                operands = user_input[1:]
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
