import random

def fifo(referencia_de_paginas, num_molduras):
    print("-----------FIFO----------")
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

def lru(referencia_de_paginas, num_molduras):
    print("-----------LRU----------")
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
        else:
            molduras.remove(pagina)
            molduras.append(pagina)
    return faltas_de_pagina

def main():
    lista_num_molduras = list(range(1,5))
    print(lista_num_molduras)

    referencia_de_paginas = [8,1,1,4,5,7,9,6,5,3]
    resultados = []

    for num_molduras in lista_num_molduras:
        falta_de_paginas_fifo = fifo(referencia_de_paginas, num_molduras)
        falta_de_paginas_lru = lru(referencia_de_paginas, num_molduras)

        resultados.append({
            'molduras': num_molduras,
            'falta_de_paginas_fifo': falta_de_paginas_fifo,
            'falta_de_paginas_lru': falta_de_paginas_lru
        })

    for resultado in resultados:
        print(f"molduras: {resultado['molduras']}, Falta de páginas FIFO: {resultado['falta_de_paginas_fifo']}, Falta de páginas LRU: {resultado['falta_de_paginas_lru']}")

if __name__ == "__main__":
    main()
