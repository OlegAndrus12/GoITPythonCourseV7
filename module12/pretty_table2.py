from prettytable import HRuleStyle, PrettyTable

def draw_table(headers, data):
    """
    Generate a formatted table using PrettyTable.

    :param headers (list): Column headers.
    :param data (list of lists): Table rows.
    :param maxcolwidths (list, optional): Max width for each column.
    :param allhlines (bool, optional): Draw horizontal lines for all rows. Default is False.

    :return: PrettyTable: A formatted table.
    """
    # hrules =  if allhlines else HRuleStyle.FRAME

    table = PrettyTable(
        vertical_char="│",
        horizontal_char="─",
        junction_char="┼",
        top_junction_char="┬",
        bottom_junction_char="┴",
        right_junction_char="┤",
        left_junction_char="├",
        top_right_junction_char="╮",
        top_left_junction_char="╭",
        bottom_right_junction_char="╯",
        bottom_left_junction_char="╰",
        hrules=HRuleStyle.ALL,
        align="l",
    )

    table.field_names = headers
    table.add_rows(data)

    return table

def print_command_list():
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

    headers = ["Command", "Description"]


    print("List of available commands:")
    print(draw_table(headers, list(commands.items()), allhlines=False))


print_command_list()