while True:
    operacao = input('A operação é uma operação de compra ou de venda?').title().strip()
    if operacao == 'Compra':
        while True:
            tipo_operacao = input('Qual o tipo de operação (Day trade/Normal)?').title().strip()
            if tipo_operacao == 'Day Trade':
                while True:
                    try:
                        preco_compra = float(input('Qual o preço da compra?'))
                        break
                    except:
                        print('Valor inválido. Digite um número.')
                while True:
                    try:
                        preco_venda = float(input('Qual o preço da venda?'))
                        break
                    except:
                        print('Valor inválido. Digite um número.')
                while True:
                    try:
                        quantidade = int(input('Qual a quantidade?'))
                        break
                    except:
                        print('Valor inválido. Digite um número.')
                resultado = ((preco_venda - preco_compra) * quantidade)
                if resultado * 0.2 > 10:
                    while True:
                        try:
                            credito_tributario = float(input('Se você possui créditos tributários provenientes de '
                                                     'operações do tipo Day Trade e ainda não os utilizou '
                                                     'para abatimento, por favor, informe o valor aqui. '
                                                     '(Caso não possua créditos tributários, digite o valor '
                                                     '0.00).'))
                            break
                        except:
                            print('Valor inválido. Digite um número.')
                    print(f'O imposto de renda a recolher é de R$ {(resultado - credito_tributario) * 0.2}')
                    break
                elif resultado < 0:
                    print(f'Isento. Essa operação gerou um crédito tributário de R$ {abs(resultado)}.')
                    break
                else:
                    print(f'O valor de R$ {round(resultado * 0.2, 2)} é inferior a R$ 10,00, portanto, o DARF '
                          f'não precisa ser recolhido neste momento.Esse valor deverá ser recolhido no '
                          f'futuro apenas quando a soma do Imposto de Renda (IR) for superior a R$ 10,00.')
                    break
            elif tipo_operacao == 'Normal':
                while True:
                    try:
                        preco_compra = float(input('Qual o preço da compra?'))
                        break
                    except:
                        print('Valor inválido. Digite um número.')
                while True:
                    try:
                        preco_venda = float(input('Qual o preço da venda?'))
                        break
                    except:
                        print('Valor inválido. Digite um número.')
                while True:
                    try:
                        quantidade = int(input('Qual a quantidade da venda?'))
                        break
                    except:
                        print('Valor inválido. Digite um número.')
                total_venda = quantidade * preco_venda
                resultado = ((preco_venda - preco_compra) * quantidade)
                if total_venda > 20000 and resultado * 0.15 > 10.0:
                    while True:
                        try:
                            credito_tributario = float(input('Se você possui créditos tributários provenientes de operações'
                                                     ' do tipo Day Trade e ainda não os utilizou para abatimento, '
                                                     'por favor, informe o valor aqui. (Caso não possua créditos '
                                                     'tributários, digite o valor 0.00).'))
                            break
                        except:
                            print('Valor inválido. Digite um número.')
                    print(f'O imposto de renda a recolher é de R$ {(resultado - credito_tributario) * 0.15}')
                    break
                elif resultado < 0:
                    print(f'Isento. Essa operação gerou um crédito tributário de R$ {abs(resultado)}.')
                    break
                elif total_venda < 20000:
                    print('Isento')
                    break
                else:
                    print(f'O valor de R$ {round(resultado * 0.15, 2)} é inferior a R$ 10,00, portanto, o DARF não '
                          f' precisa ser recolhido neste momento. Esse valor deverá ser recolhido no futuro apenas '
                          f' quando a soma do Imposto de Renda (IR) for superior a R$ 10,00.')
                    break
            else:
                print('Informe um tipo de operação válida.')
        break
    elif operacao == 'Venda':
        while True:
            tipo_operacao = input('Qual o tipo de operação (Day trade/Normal)?').title().strip()
            if tipo_operacao == 'Day Trade':
                while True:
                    try:
                        preco_venda = float(input('Qual o preço da venda?'))
                        break
                    except:
                        print('Valor inválido. Digite um número.')
                while True:
                    try:
                        preco_compra = float(input('Qual o preço da compra?'))
                        break
                    except:
                        print('Valor inválido. Digite um número.')
                while True:
                    try:
                        quantidade = int(input('Qual a quantidade da venda?'))
                        break
                    except:
                        print('Valor inválido. Digite um número.')
                resultado = ((preco_venda - preco_compra) * quantidade)
                if resultado * 0.2 > 10:
                    while True:
                        try:
                            credito_tributario = float(input('Se você possui créditos tributários provenientes de '
                                                             'operações do tipo Day Trade e ainda não os utilizou '
                                                             'para abatimento, por favor, informe o valor aqui. '
                                                             '(Caso não possua créditos tributários, digite o valor '
                                                             '0.00).'))
                            break
                        except:
                            print('Valor inválido. Digite um número.')
                    print(f'O imposto de renda a recolher é de R$ {(resultado - credito_tributario) * 0.2}')
                    break
                elif resultado < 0:
                    print(f'Isento. Essa operação gerou um crédito tributário de R$ {abs(resultado)}.')
                    break
                else:
                    print(f'O valor de R$ {round(resultado * 0.2, 2)} é inferior a R$ 10,00, portanto, o DARF '
                          f'não precisa ser recolhido neste momento.Esse valor deverá ser recolhido no '
                          f'futuro apenas quando a soma do Imposto de Renda (IR) for superior a R$ 10,00.')
                    break
            elif tipo_operacao == 'Normal':
                while True:
                    try:
                        preco_venda = float(input('Qual o preço da venda?'))
                        break
                    except:
                        print('Valor inválido. Digite um número.')
                while True:
                    try:
                        preco_compra = float(input('Qual o preço da compra?'))
                        break
                    except:
                        print('Valor inválido. Digite um número.')
                while True:
                    try:
                        quantidade = int(input('Qual a quantidade da venda?'))
                        break
                    except:
                        print('Valor inválido. Digite um número.')
                total_venda = quantidade * preco_venda
                resultado = ((preco_venda - preco_compra) * quantidade)
                if total_venda > 20000 and resultado * 0.15 > 10.0:
                    while True:
                        try:
                            credito_tributario = float(input('Se você possui créditos tributários provenientes de '
                                                             'operações do tipo Day Trade e ainda não os utilizou '
                                                             'para abatimento, por favor, informe o valor aqui. '
                                                             '(Caso não possua créditos tributários, digite o valor '
                                                             '0.00).'))
                            break
                        except:
                            print('Valor inválido. Digite um número.')
                elif resultado < 0:
                    print(f'Isento. Essa operação gerou um crédito tributário de R$ {abs(resultado)}.')
                    break
                elif total_venda < 20000:
                    print('Isento')
                    break
                else:
                    print(f'O valor de R$ {round(resultado * 0.15, 2)} é inferior a R$ 10,00, portanto, o DARF não '
                          f' precisa ser recolhido neste momento. Esse valor deverá ser recolhido no futuro apenas '
                          f' quando a soma do Imposto de Renda (IR) for superior a R$ 10,00.')
                    break
            else:
                print('Informe um tipo de operação válida.')
        break
    else:
        print('Informe se a operação foi de compra ou de venda.')
