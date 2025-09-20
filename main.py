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
    Animal("Golfinho", mamifero=True,
           aquatico=True, medio=True, terrestre=False, pelos=False),
    Animal("Tubarão", peixe=True,
           aquatico=True, grande=True, terrestre=False, escama=True),
    Animal("Polvo", molusco=True,
           aquatico=True, medio=True, terrestre=False, escama=False)
]

print("Escolha um dos animais abaixo: ")

for i in animais:
    print(i.nome)

filtro_animal = []

perguntas = {
    "terrestre": "Seu animal é terrestre?",
    "aquatico": "Seu animal é aquático?",
    "voador": "Seu animal voa?",
    "mamifero": "Seu animal é mamífero?",
    "ave": "Seu animal é uma ave?",
    "reptil": "Seu animal é um réptil?",
    "anfibio": "Seu animal é um anfíbio?",
    "pequeno": "Seu animal é pequeno?",
    "medio": "Seu animal é médio?",
    "grande": "Seu animal é grande?",
    "pelos": "Seu animal tem pelos?",
    "escama": "Seu animal tem escamas?",
    "penas": "Seu animal tem penas?"
}

filtro = animais[:]


ordem_perguntas = [
    "terrestre", "aquatico", "voador",     
    "mamifero", "ave", "reptil", "anfibio", 
    "pequeno", "medio", "grande",           
    "pelos", "escama", "penas"              
]


for chave in ordem_perguntas:
       if len(filtro) <= 1:
              break
       print(perguntas[chave])
       reposta = bool(int(input("0 - Não | 1- Sim")))