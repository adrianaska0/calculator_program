from app.commands import Command, CommandHandler
from decimal import Decimal, InvalidOperation
import pkgutil
import importlib
import os
import logging
import logging.config
from dotenv import load_dotenv

class App:
    def __init__(self):
        os.makedirs('logs', exist_ok=True)
        self.configure_logging()
        load_dotenv()
        self.settings = self.load_environment_variables()
        self.settings.setdefault('ENVIRONMENT', 'PRODUCTION')
        self.command_handler = CommandHandler()
    
    def configure_logging(self):
        logging_conf_path = 'logging.conf'
        if os.path.exists(logging_conf_path):
            logging.config.fileConfig(logging_conf_path, disable_existing_loggers=False)
        else:
            logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
        logging.info("Logging configuration complete.")
    
    def load_environment_variables(self):
        settings = {key: value for key, value in os.environ.items()}
        logging.info("Environment variables loaded.")
        return settings

    def get_environment_variable(self, env_var: str = 'ENVIRONMENT'):
        return self.settings.get(env_var, None)

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
        logging.info("Application started successfully. Type 'exit' to exit")
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
                logging.error("Usage: <operation> <operand> <operand>")
            except TypeError:
                logging.error("Please provide the correct number of arguments. Usage: <operation> <operand> <operand>")
            except InvalidOperation:
                logging.error(f"Invalid operand input: {operands[0]} or {operands[1]} is not a valid number")
            except Exception as e:
                logging.error(f"An error occured: {e}")
