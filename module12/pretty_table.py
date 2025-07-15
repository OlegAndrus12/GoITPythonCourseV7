from prettytable import PrettyTable

# Create a table
table = PrettyTable()

# Define columns
table.field_names = ["Name", "Age", "City"]

# Add rows
table.add_row(["Alice", 30, "New York"])
table.add_row(["Bob", 25, "San Francisco"])
table.add_row(["Charlie", 35, "Chicago"])

# Print the table
print(table)
