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
    Animal("Peixe-Palhaço", peixe=True,
           aquatico=True, pequeno=True, terrestre=False, pelos=False),
    Animal("Tubarão", peixe=True,
           aquatico=True, grande=True, terrestre=False, escama=True),
    Animal("Salmão", peixe=True, aquatico=True,
           medio=True, escama=True),
    
    Animal("Pinguim", ave=True, terrestre=True,
           aquatico=True, medio=True, penas=True, voador=False),
    Animal("Tartaruga", reptil=True, terrestre=True,
           aquatico=True, medio=True, escama=True),
    Animal("Sapo", anfibio=True, terrestre=True,
           aquatico=True, pequeno=True, escama=False),
    Animal("Elefante", mamifero=True, terrestre=True,
           grande=True, pelos=False),
    Animal("Morcego", mamifero=True, terrestre=True,
           voador=True, pequeno=True, pelos=True)
]

print("Escolha um dos animais abaixo: ")

for i in animais:
    print(i.nome)


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


ordem_perguntas = [
    "terrestre", "aquatico", "voador",     
    "mamifero", "ave", "reptil", "anfibio", 
    "pequeno", "medio", "grande",           
    "pelos", "escama", "penas"              
]

filtro = animais[:] # começa com tds os animais

contador = 0
for chave in ordem_perguntas:
    contador += 1
    print(f"\n{contador}: {perguntas[chave]}")
    resposta = bool(int(input("0 - Não | 1 - Sim\n")))

    # filtro atualizado usando list comprehension
    filtro = [animal for animal in filtro if getattr(animal, chave) == resposta]

    if len(filtro) <= 1:  # se sobrou 1, pode parar
        break

print("\n=== Resultado final ===")
for animal in filtro:
    print("-", animal.nome)
