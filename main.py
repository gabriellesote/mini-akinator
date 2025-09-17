from animal import Animal

animais = [
    Animal("Gato", felino=True, mamifero=True,
           terrestre=True, pequeno=True, pelos=True),
    Animal("Cachorro", canino=True, mamifero=True,
           terrestre=True, medio=True, pelos=True),
    Animal("Calopsita", ave=True, terrestre=True,
           voador=True, pequeno=True, penas=True),
    Animal("Papagaio", ave=True, terrestre=True,
           voador=True, pequeno=True, penas=True),
    Animal("Corvo", ave=True, terrestre=True,
           voador=True, medio=True, penas=True),
    Animal("Leão", felino=True, mamifero=True,
           terrestre=True, grande=True, pelos=True),
    Animal("Lobo", canino=True, mamifero=True,
           terrestre=True, medio=True, pelos=True),
    Animal("Tartaruga Marinha", reptil=True, terrestre=True,
           aquatico=True, medio=True, escama=True),
    Animal("Crocodilo", reptil=True, terrestre=True,
           aquatico=True, grande=True, escama=True),
    Animal("Sapo", anfibio=True, terrestre=True,
           aquatico=True, pequeno=True, escama=False)
]

print("Escolha um dos animais abaixo: ")
for i in animais:
    print(i.nome)
    
animal_selecionado = []

while 