import random
def gerar_referencias_de_pagina(num_paginas, tamanho_sequencia):
    return [random.randint(0, num_paginas - 1) for _ in range(tamanho_sequencia)]

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
def main():
    lista_num_molduras = list(range(1, 21))

    print(lista_num_molduras)

    num_paginas = 200
    tamanho_sequencia = 1000
    referencia_de_paginas = gerar_referencias_de_pagina(num_paginas, tamanho_sequencia)

    with open("referencias_paginas.txt", "w") as f:
        f.write('|'.join(map(str, referencia_de_paginas)))

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

if __name__ == "__main__":
    main()
