from datetime import datetime

# Sorting Columns inside GUI Table
def sort_column(tree, col, reverse):

    # Get all the rows (children) in the Treeview
    rows = tree.get_children('')

    # Extract the value in the selected column for each row
    row_data = []
    for child in rows:
        cell_value = tree.set(child, col)
        row_data.append((cell_value, child))

    # Define the key function for sorting
    def sort_key(item):
        value = item[0]
        if "amount" in col.lower():
            try:
                return float(value)
            
            except ValueError:
                return float('inf')  # Handle conversion errors
            
        elif "date" in col.lower():
            try:
                return datetime.strptime(value, "%Y-%m-%d")
            
            except ValueError:
                return datetime.max  # Handle conversion errors
            
        else:
            return value.lower() if isinstance(value, str) else value

    # Sort the extracted data based on the column value
    sorted_data = sorted(row_data, key=sort_key, reverse=reverse)

    # Rearrange the sorted data in the Treeview
    for index, (val, item) in enumerate(sorted_data):
        tree.move(item, '', index)

    # Reverse the sorting order for next click
    tree.heading(col, command=lambda: sort_column(tree, col, not reverse))

# Ensuring correct value types when sorting
# def convert_type(value, col):
    
#     # Define the column-specific data types
#     if col == "Income Amount":
#         try:
#             return float(value)
        
#         # or handle the error as appropriate
#         except ValueError:
#             return float('inf')  
        
#     elif col == "Income Date":
#         try:
#             return datetime.strptime(value, "%Y-%m-%d")
        
#         # or handle the error as appropriate
#         except ValueError:
#             return datetime.max  

#     # For string columns, return the value as is    
#     else:
#         return value  

def convert_to_two_decimals(value):
    """
    Attempts to convert the input value to a float rounded to two decimal places.
    Returns the formatted value as a string with two decimal places if conversion is successful.
    Returns None if conversion fails.
    """
    try:
        # Convert to float and round to two decimal places
        float_value = float(value)
        formatted_value = f"{float_value:.2f}"
        return formatted_value
    except ValueError:
        # Return None or an error message if conversion fails
        return None