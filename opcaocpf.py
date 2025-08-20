import os
import random
import re

while True:
    opcao = int(input("\n(1) Verificar se CPF é valido\n(2) Gerar CPF valido\n(3) Encerrar sessão\n"))

    if opcao == 1:
        cpf = str(input("Digite seu CPF: "))
        cpf = re.sub(r'[^0-9]','',cpf)
        nove_digitos = str(cpf[0:9])
        contador_regressivo_1 = 10
        resultado_1 = 0

        for numero in nove_digitos:
            resultado_1 += int(numero) * contador_regressivo_1
            contador_regressivo_1 -= 1

        digito_1 = (resultado_1 * 10) % 11

        digito_1 = digito_1 if digito_1 <= 9 else 0

        dez_digitos = nove_digitos + str(digito_1)
        contador_regressivo_2 = 11

        resultado_2 = 0

        for numero in dez_digitos:
            resultado_2 += int(numero) * contador_regressivo_2
            contador_regressivo_2 -= 1

        digito_2 = (resultado_2 * 10) % 11

        digito_2 = digito_2 if digito_2 <= 9 else 0

        validacao_cpf = f'{nove_digitos}{digito_1}{digito_2}'

        os.system('cls')

        if cpf == validacao_cpf:
            print(f"{cpf} é um CPF valido")
        else:
            print("CPF invalido")
 
    elif opcao == 2:
        nove_digitos = ''

        for i in range (9):
            nove_digitos += str(random.randint(0, 9))

        print(nove_digitos)
        contador_regressivo_1 = 10
        resultado_1 = 0
        nove_digitos

        for numero in nove_digitos:
            resultado_1 += int(numero) * contador_regressivo_1
            contador_regressivo_1 -= 1

        digito_1 = (resultado_1 * 10) % 11

        digito_1 = digito_1 if digito_1 <= 9 else 0
  
        dez_digitos = nove_digitos + str(digito_1)
        contador_regressivo_2 = 11

        resultado_2 = 0

        for numero in dez_digitos:
            resultado_2 += int(numero) * contador_regressivo_2
            contador_regressivo_2 -= 1

        digito_2 = (resultado_2 * 10) % 11

        digito_2 = digito_2 if digito_2 <= 9 else 0

        os.system('cls')

        cpf = f'{nove_digitos}{digito_1}{digito_2}'

        if cpf:
            print(f"{cpf} gerado com sucesso")
        else:
            print("Erro")

    elif opcao == 3:
        os.system('cls')
        print("Sessão encerrada")
        
        break
    else:
        print("\nopcao invalida")