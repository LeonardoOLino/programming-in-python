import statistics
def calcular_media(notas):
    return statistics.mean(notas)

def calcular_modas(notas):
    try:
        return statistics.mode(notas)
    except:
        return 'Nãp ha modas (Valores unicos)'

def calcular_desvio_padrao(notas):
    if len(notas) > 1:
        return statistics.stdev(notas)
    else:
        return 0
    
def maior_nota(notas):
    return max(notas)

def menor_nota(notas):
    return min(notas)