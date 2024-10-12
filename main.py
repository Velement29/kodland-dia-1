meme_dict = {
    "CRINGE": "algo raro o embarazoso",
    "LOL": "una respuesta a algo gracioso",
    "ROFL": "una respuesta a una broma",
    "SHEESH": "ligera desaprobación",
    "CREEPY": "aterrador, siniestro",
    "AGGRO": "ponerse agresivo/enojado"
}

word = input("Escribe una palabra que no entiendas (¡Tiene que ser en mayuscula!): ")

if word in meme_dict.keys():
    print("La palabra ", word, " tiene el significado: ", meme_dict[word])
else:
    print("La palabra ", word, " no esta en el diccionario.")
