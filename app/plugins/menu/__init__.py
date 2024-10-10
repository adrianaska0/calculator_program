from app.commands import Command, CommandHandler

class MenuCommand(Command):
    def __init__(self, command_handler):
        self.command_handler = command_handler

    def execute(self, a=None, b=None):
        print("Available commands:")
        for command_name in self.command_handler.commands.keys():
            print(f"- {command_name}")