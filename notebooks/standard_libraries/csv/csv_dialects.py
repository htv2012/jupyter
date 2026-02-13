# csv_dialect.py
import csv

SEMICOLON = 'semicolon'
SPACE = 'space'

csv.register_dialect(SEMICOLON, delimiter=';', skipinitialspace=True)
csv.register_dialect(SPACE, delimiter=' ', skipinitialspace=True)
