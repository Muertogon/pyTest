import random as rn

# pirmasis

ne = False #bool
fl = 24.5 #float
metai = 2021 #integer
vardas = "Kestutis" #string

# antrasis

vaisiai = ["Obuolys", "Bananas", "Persimonas"] #list
for x in vaisiai:
    print(x)
vaistai = ("Pertusinas", "Valerijonas", "Ibuprofenas") #tuple
for n in vaistai:
    print(n)
asmuo = {"vardas": "George", "pavarde": "Smith", "kodas": rn.randint(10000000000, 99999999999)} #dict
for i in asmuo:
    print(asmuo[i])
# trecias

manoKintamasis = 6
mano_kintamasis = 8
tipas = 9

# ketvirtas

floatData = 4.5

#penktas

def printe_liste(listo):
    if type(listo) == dict:
        for v in listo:
            print(listo[v])
    elif type(listo) == list:
        for v in listo:
            print(v)
    else:
        for v in listo:
            print(v)

printe_liste(asmuo)

# sestas

x = "gas"
y = "kin"

# septintas

# mutable tipai: list, dict, set
# not mutable: int, float, string, tuple

#mutable objektai gali buti pakeisti po sukurimo, o immutable- ne

#astuntas

# 5