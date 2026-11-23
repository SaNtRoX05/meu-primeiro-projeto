
print("===== CALCULADORA =====")
print("1 - Soma")
print("2 - Subtraçao")
print("3 - Multiplicaçao")
print("4 - Divisao")

opcao = int(input("Escolha uma operação: "))

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

if opcao == 1:
    resultado = numero1 + numero2
    print("Resultado:", resultado)

elif opcao == 2:
    resultado = numero1 - numero2
    print("Resultado:", resultado)

elif opcao == 3:
    resultado = numero1 * numero2
    print("Resultado:", resultado)

elif opcao == 4:
    if numero2 != 0:
        resultado = numero1 / numero2
        print("Resultado:", resultado)
    else:
        print("Não é possível dividir por zero!")

else:
    print("Opção inválida!")
