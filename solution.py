from unicodedata import normalize


# NORMALIZE TEXT // NORMALIZAR TEXTO
# CREATE HASHMAP WITH EACH CHARACTER // CREAR UN DICCIONARIO CON CADA CARACTER
# GET EACH STRING IN THE TEXT // OBTENER CADA CADENA DEL TEXTO
# FOR EACH CHARACTER CHECK EACH STRING // POR CADA CARACTER REVISAR CADA CADENA
# COMPARE AND REPLACE FOR THE MORE LONG // COMPARAR Y GUARDAR LA MAS LARGA

def ex953(text):
    trans_tab = dict.fromkeys(map(ord, u'\u0301\u0308'), None)
    text = normalize('NFKC', normalize('NFKD', text).translate(trans_tab))
    text = text.lower()
    all_characters = {}
    for character in text:
        if character not in all_characters and character != " ":
            all_characters[character] = ""
    list_string = text.split()
    for character in all_characters:
        for string in list_string:
            if character in string:
                size_string = len(string)
                if size_string >= len(all_characters[character]):
                    all_characters[character] = string

    return all_characters
