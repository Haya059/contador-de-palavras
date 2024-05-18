def contador_palavras(frase):
    palavras = frase.split()
    return len(palavras)

print(contador_palavras('O rato roeu a roupa do rei de roma'))