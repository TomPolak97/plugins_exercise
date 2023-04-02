import json

"""
This python file will include all the useful method for managing our system.
Every general method that is useful for either new plugin or a new evidence should be store here.
"""


def write_list_to_file(file_name, lst):
    with open(file_name, 'w') as f:
        json.dump(lst, f)
