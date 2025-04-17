sair = ''
while sair != "s":
    print('Oque você deseja?\nVoce pode:')
    print("[1] Calcular o consume de um eletrodomestico")
    print("[2] Calcular o consumo de energia da sua residencia")
    answer = int(input())
    match answer:
        case 1:
            potencia = float(input("Digite a potencia em (w)"))
            horas_usadas = float(input("Digite quantas horas o aparelho foi usado"))
            days = int(input("Digite quantos dias ele foi usado"))
            resultado = potencia * horas_usadas * days
            resultado / 1000
            print(resultado)
        case 2:
            consumo = float(input("Digite o consumo em (kwh)" ))
            tariff = float(input("Digite o valor da tarifa R$ "))
            resultado = consumo * tariff
            print(f"O valor da conta de luz e de {resultado}")


    sair = input("Quer sair (S) ou (N) ?").lower()
    continue