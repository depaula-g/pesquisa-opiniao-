# Pesquisa de Opinião - TudoWeb

excelentes = 0
ruins = 0

# Pesquisa com 50 entrevistados
for i in range(50):
    print(f"\n--- Entrevistado {i + 1} ---")

    nome = input("Nome: ")
    idade = int(input("Idade: "))

    print("\nOpinião sobre o atendimento:")
    print("1 - EXCELENTE")
    print("2 - BOM")
    print("3 - RUIM")

    opiniao = int(input("Digite sua opinião: "))

    # Verificação da opinião
    if opiniao == 1:
        excelentes += 1
    elif opiniao == 3:
        ruins += 1

# Exibição dos resultados
print("\n--- RESULTADO DA PESQUISA ---")
print("Quantidade de respostas EXCELENTE:", excelentes)
print("Quantidade de respostas RUIM:", ruins)