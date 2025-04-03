import datetime

hoje = datetime.datetime.today()

print("Bem-vindo ao Sistema de Monitoramento de Sustentabilidade Pessoal!\n"
    "1. Registrar consumo diário.\n"
    "2. Verificar nível de sustentabilidade.")

while True:

    try:
        escolha = int(input("Escolha uma opção: "))

        if escolha == 1:
                print("Começando o registro do dia")

                while True:
                    try:
                        litros_agua = float(input('Quantos litros de agua você consumiu hoje? (aproximadamente): '))
                        if litros_agua < 0:
                            print("\033[091mA quantidade de água não pode ser negativa! Tente novamente.\033[m")
                        else:
                            break
                    except ValueError:
                        print('\033[091mA quantidade de agua deve ser um valor numérico; tente novamente!\033[m')

                while True:
                    try:
                        energia = int(input('Quantos kWh de energia elétrica você consumiu hoje?: '))
                        if energia < 0:
                            print("\033[091mA quantidade de energia não pode ser negativa! Tente novamente.\033[m")
                        else:
                            break
                    except ValueError:
                        print('\033[091mA quantidade de energia deve ser um valor numérico válido! Tente novamente.\033[m')

                while True:
                    try:
                        residuo = float(input('Quantos kg de resíduos você gerou hoje?: '))
                        if residuo < 0:
                            print("\033[091mA quantidade de residuo não pode ser negativa! Tente novamente.\033[m")
                        else:
                            break
                    except ValueError:
                        print('\033[091mA quantidade de residuo deve ser um valor numérico; tente novamente!\033[m')

                while True:
                    try:
                        residuo_porcentagem = int(input('Dos residuos gerados, quantos foram reciclados? (em %): '))
                        if residuo_porcentagem < 0:
                            print("\033[091mA porcentagem de residuo não pode ser negativa! Tente novamente.\033[m")
                        else:
                            break
                    except ValueError:
                        print('\033[091mA porcentagem de residuo deve ser um valor numérico válido! Tente novamente.\033[m')

                while True:
                    try:
                        print('1. Transporte público (ônibus, metrô, trem).\n'
                                '2. Bicicleta.\n'
                                '3. Caminhada.\n'
                                '4. Carro (combustível fósseis).\n'
                                '5. Carro elétrico.\n'
                                '6. Carona compartilhada.')
                        meio_transporte = int(input('Qual o meio de transporte você usou hoje?: '))
                        if meio_transporte <1 or meio_transporte > 6:
                            print("\033[091mEscolha uma das opçôes! Tente novamente.\033[m")
                        else:
                            break
                    except ValueError:
                        print('\033[091mA escolha do meio de transporte deve ser um valor numérico válido! Tente novamente.\033[m')

                print('\033[093mRegisto diario finalizado.\033[m]')

                vizualizar = input('Gostaria de vizualizar os seus dados registrados de hoje? (s/n): ')
                if vizualizar.lower() != 's':
                    print('Obrigado, até a proxima vez.')
                    break

                else:
                    print (f'Registro do dia: {hoje.strftime("%d/%m/%Y")}\n'
                    f'Quantos litros de agua você consumiu hoje? (aproximadamente): {litros_agua}\n'
                    f'Quantos kWh de energia elétrica você consumiu hoje?: {energia}\n'
                    f'Quantos kg de resíduos você gerou hoje?: {residuo}\n'
                    f'Dos residuos gerados, quantos foram reciclados? (em %): {residuo_porcentagem}\n'
                    f'Qual o meio de transporte você usou hoje?: {meio_transporte}')
                    if meio_transporte == 1:
                        print('Transporte público (ônibus, metrô, trem).')
                    elif meio_transporte == 2:
                        print ('Bicicleta.')
                    elif meio_transporte == 3:
                        print('Caminhada.')
                    elif meio_transporte == 4:
                        print('Carro (combustível fósseis).')
                    elif meio_transporte == 5:
                        print('Carro elétrico.')
                    elif meio_transporte == 6:
                        print('Carona compartilhada.')

                voltar = input('Gostaria de voltar ao menu principal (s/n): ')
                if vizualizar.lower() != 's':
                    print('Obrigado, até a proxima vez.')
                    break
                



    except ValueError:
        print()