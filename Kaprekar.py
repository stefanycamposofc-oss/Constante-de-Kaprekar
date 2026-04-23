numero = int(input("Digite um número de 4 dígitos: "))

# VALIDAÇÃO 1: não pode ser negativo
if numero < 0:
    print("Erro: o número deve ser inteiro e positivo.")

else:

    # VALIDAÇÃO 2: não pode ter mais de 4 dígitos
    if numero > 9999:
        print("Erro: número fora do intervalo permitido (0000 a 9999).")

    else:

        # Separa cada dígito usando divisão inteira (//) e resto (%)
        # Ex: 3524 → d1=3, d2=5, d3=2, d4=4
        d1 = numero // 1000
        d2 = (numero // 100) % 10
        d3 = (numero // 10) % 10
        d4 = numero % 10

        # VALIDAÇÃO 3: conta pares de dígitos iguais
        # Se iguais >= 3, há dígitos repetidos demais (ex: 1112, 1111)
        iguais = 0

        if d1 == d2:
            iguais = iguais + 1
        if d1 == d3:
            iguais = iguais + 1
        if d1 == d4:
            iguais = iguais + 1
        if d2 == d3:
            iguais = iguais + 1
        if d2 == d4:
            iguais = iguais + 1
        if d3 == d4:
            iguais = iguais + 1

        if iguais >= 3:
            print("Erro: o número possui muitos dígitos repetidos.")

        else:

            print("Número informado:", numero)
            print()

            resultado = numero
            iteracao = 0

            # Repete até atingir a constante 6174
            while resultado != 6174:

                # Separa os dígitos do resultado atual
                d1 = resultado // 1000
                d2 = (resultado // 100) % 10
                d3 = (resultado // 10) % 10
                d4 = resultado % 10

                a = d1
                b = d2
                c = d3
                d = d4

                # Ordena os dígitos do menor pro maior usando trocas com temp
                if a > b: temp = a; a = b; b = temp
                if a > c: temp = a; a = c; c = temp
                if a > d: temp = a; a = d; d = temp
                if b > c: temp = b; b = c; c = temp
                if b > d: temp = b; b = d; d = temp
                if c > d: temp = c; c = d; d = temp

                # Monta NDC (crescente) e NDD (decrescente)
                # Ex: dígitos 2,3,4,5 → NDC=2345, NDD=5432
                NDC = a * 1000 + b * 100 + c * 10 + d
                NDD = d * 1000 + c * 100 + b * 10 + a

                resultado = NDD - NDC
                iteracao = iteracao + 1

                print("Iteração", iteracao, ":", NDD, "-", NDC, "=", resultado)

            print()
            print("Constante de Kaprekar (6174) atingida em", iteracao, "iterações.")
