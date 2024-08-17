import random
import matplotlib.pyplot as plt

def fifo(referencia_de_paginas, num_molduras):
    molduras = []
    faltas_de_pagina = 0

    for pagina in referencia_de_paginas:
        if pagina not in molduras:
            faltas_de_pagina += 1
            if len(molduras) < num_molduras:
                molduras.append(pagina)
            else:
                molduras.pop(0)
                molduras.append(pagina)
    
    return faltas_de_pagina

def aging(referencia_de_paginas, num_molduras, bits=8):
    faltas_de_pagina = 0
    molduras = []
    contador = {}
    
    for pagina in referencia_de_paginas:

        if pagina in molduras:
            contador[pagina] = contador[pagina] | (1 << (bits - 1)) 
        else:
            faltas_de_pagina += 1
            if len(molduras) < num_molduras:
                molduras.append(pagina)
            else:
                oldest_pagina = min(molduras, key=lambda p: contador[p])
                molduras.remove(oldest_pagina)
                del contador[oldest_pagina]
                molduras.append(pagina)
            contador[pagina] = 1 << (bits - 1) 

        for p in molduras:
            contador[p] = contador[p] >> 1  
    
    return faltas_de_pagina

def ler_referencias(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        conteudo = arquivo.read()
    referencias = [int(x.strip()) for x in conteudo.split(',')]
    return referencias

def main():
    lista_num_molduras = list(range(1, 21))

    print(lista_num_molduras)

    num_paginas = 200
    tamanho_sequencia = 1000

    referencia_de_paginas = ler_referencias('referencias_paginas.txt')

    resultados = []

    for num_molduras in lista_num_molduras:
        falta_de_paginas_fifo = fifo(referencia_de_paginas, num_molduras)
        falta_de_paginas_aging = aging(referencia_de_paginas, num_molduras)

        resultados.append({
            'molduras': num_molduras,
            'falta_de_paginas_fifo': falta_de_paginas_fifo,
            'falta_de_paginas_aging': falta_de_paginas_aging
        })

    for resultado in resultados:
        print(f"molduras: {resultado['molduras']}, Falta de páginas FIFO: {resultado['falta_de_paginas_fifo']}, Falta de páginas AGING: {resultado['falta_de_paginas_aging']}")

    molduras = [resultado['molduras'] for resultado in resultados]
    faltas_fifo = [resultado['falta_de_paginas_fifo'] for resultado in resultados]
    faltas_aging = [resultado['falta_de_paginas_aging'] for resultado in resultados]

    plt.figure(figsize=(12, 6))
    
    plt.plot(molduras, faltas_fifo, marker='o', label='FIFO', color='b')
    plt.plot(molduras, faltas_aging, marker='x', label='AGING', color='r')
    
    plt.xlabel('Número de Molduras')
    plt.ylabel('Número de Faltas de Página')
    plt.title('Comparação de Faltas de Página entre FIFO e AGING')
    plt.legend()
    plt.grid(True)
    
    plt.savefig('comparacao_algoritmos.png')
    plt.show()
    
if __name__ == "__main__":
    main()
