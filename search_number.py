
from export_contact import export_contact
from print_contact import print_contact

def search_number(word, data):
    if len(data) > 0:
        for item in data:
            if word in item:
                return item
    else:
        return None
