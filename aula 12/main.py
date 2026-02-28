from entrada import receber_notas
from saida import mostrar_estatisticas

def main():
    print('==== Sistema de notas ===')
    notas_alunos = receber_notas()
    mostrar_estatisticas(notas_alunos)

if __name__ == '__main__':
    main()
    

