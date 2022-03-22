#helpers.py list of all needed tools

import random
import string
from db.database import db
from db.models import Catalog

def gen_password():
    pw = []
    char = list(string.ascii_letters + string.digits)
    length = 8
    random.shuffle(char)
    for i in range(length):
        pw.append(random.choice(char))
    product = ("".join(pw))
    return product
def product_catalog():
    #temporary while creation
    return Catalog.query
