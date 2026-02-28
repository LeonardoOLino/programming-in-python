from estastisca import calcular_media, calcular_modas, calcular_desvio_padrao, maior_nota, menor_nota

def mostrar_estatisticas(notas):
    print("\n===== ESTATÍSTICAS =====")
    print(f"Média: {calcular_media(notas):.2f}")
    print(f"Moda: {calcular_modas(notas)}")
    print(f"Desvio Padrão: {calcular_desvio_padrao(notas):.2f}")
    print(f"Maior nota: {maior_nota(notas)}")
    print(f"Menor nota: {menor_nota(notas)}")
    print("========================")