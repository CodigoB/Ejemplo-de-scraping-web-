import re


auxiliar = 'hola'
pattern = re.compile(auxiliar, re.I)
sequence = "Hola  1212"
if re.match(pattern, sequence):
    print("Match!")
else: print("Not a match!")

