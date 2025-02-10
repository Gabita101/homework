meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            'ROFL': 'una respuesta a una broma',
            'SHEESH': 'ligera desaprobación',
            'CREEPY': 'aterrador, siniestro',
            'QUE ONDA': 'expresión mexicana que se usa para saludar o preguntar cómo está alguien',
            'VIBES': 'Se usa para describir la atmósfera o sensación que algo transmite, tanto en personas como situaciones',
            'BTW': 'significa por cierto o a propósito',
            'F': 'Expresion de respeto o tristeza por algo que salio mal'
            }

while True:
    word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")
    
    if word in meme_dict.keys():
        print(meme_dict[word])
    else:
        print('Lo siento esta palabra no se encuentra en el diccionario')
