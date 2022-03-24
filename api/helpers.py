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
# this uses in the form_field.py for the dynamic SelectField
def product_catalog():
    return Catalog.query
