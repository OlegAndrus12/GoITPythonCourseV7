from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.box import ROUNDED
from prompt_toolkit.completion import Completer, Completion
from prompt_toolkit import PromptSession


class HintsCompleter(Completer):
    def __init__(self, hints):
        self.hints = hints

    def get_completions(self, document, complete_event):
        word = document.get_word_before_cursor().lower()
        #print(word)
        for hint in self.hints:
            if hint.startswith(word):
                yield Completion(hint, start_position=-len(word))


def print_help():
    """Prints a formatted list of available commands and their descriptions in a table."""
    # Створення консолі
    console = Console()

    ascii_art = r"""
       /\_/\
      ( o.o )
       > ^ <
    """

    section_title = "[bold green]Cute Cat[/bold green]"

    panel = Panel(ascii_art, title=section_title, subtitle="[yellow](ASCII art)[yellow]", expand=False)

    console.print(panel)


    commands = {
        "hello": "Greet the user",
        "show_all_commands": "Show all commands",
        "close/exit": "Exit the application",
        "add_contact": "Add a contact",
        "change_contact": "Modify a contact",
        "phone": "Show the contact's phone number",
        "all_contacts": "Show all contacts",
        "add_birthday": "Add a birthday to a contact",
        "show_birthday": "Show a contact's birthday",
        "upcoming_birthdays": "Show upcoming birthdays",
        "search_contacts": "Search for a contact",
        "delete_contact": "Delete a contact",
        "add_note": "Add a note",
        "edit_note": "Edit a note",
        "delete_note": "Delete a note",
        "search_notes": "Search for a note",
        "all_notes": "Show all notes",
        "add_tag": "Add a tag to a note",
        "remove_tag": "Remove a note's tag",
    }

    # Створення таблиці
    table = Table(title="List of commands", box=ROUNDED, show_header=True)

    # Додавання стовпців
    table.add_column("Command", style="bold cyan")
    table.add_column("Description", style="green")

    # Додавання рядків до таблиці
    for command, description in commands.items():
        table.add_row(command, description)

    console.print("\nWelcome to your Personal Assistant!\n", style="green")
    # Виведення таблиці
    console.print(table)

    session = PromptSession()

    completer = HintsCompleter(hints=commands.keys())
    user_input = session.prompt(">>> ", completer=completer)
    print(user_input)
    


print_help()
