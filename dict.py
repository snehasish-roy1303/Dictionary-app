import json
from difflib import get_close_matches
data=json.load(open('data.json'))

def search_meaning(n):
    n=n.lower()
    if n.upper() in data:
        return data[n.upper()]
    elif n.title() in data:
        return data[n.title()]
    elif n in data:
        return data[n.lower()]
    else:
        m=get_close_matches(n,data)[0]
        s="Are you looking for "+m+"?"
        return s+'    '+str(data[get_close_matches(n,data)[0]])

