import datetime

registros = []
proximoID = 1
    
def voltarMenu(pergunta):
    while True:
        resposta = input(pergunta).lower()
        if resposta == 's':
            return True
        elif resposta == 'n':
            return False
        else:
            print('\033[091mEscolha uma das opções (S/N)! Tente novamente.\033[m')

def listarRegistros():
    if not registros:
        print("\033[93mNenhum registro encontrado.\033[m")
        return
    
    VERDE = '\033[92m'
    AMARELO = '\033[93m'
    VERMELHO = '\033[91m'
    RESET = '\033[0m'

    print('\n\033[093mLista de registros cadastrados:\033[m\n')
    print(f"{'ID':<4} {'Data':<15} {'Água (L)':<10} {'Energia (kWh)':<14} {'Resíduos (Kg)':<17} {'Reciclado':<12} {'Transporte'}")

    for reg in registros:
        if reg['Agua'] < 150:
            corAgua = VERDE
        elif reg['Agua'] >= 150 and reg['Agua'] < 200:
            corAgua = AMARELO
        else:
            corAgua = VERMELHO

        if reg['Energia'] < 5:
            corEnergia = VERDE
        elif reg['Energia'] >= 5 and reg['Energia'] < 10:
            corEnergia = AMARELO
        else:
            corEnergia = VERMELHO

        if reg['Porcentagem Residuos'] > 50:
            corReciclado = VERDE
        elif reg['Porcentagem Residuos'] >= 20 and reg['Porcentagem Residuos'] < 50:
            corReciclado = AMARELO
        else:
            corReciclado = VERMELHO

        if reg['Transporte'] in [2, 3, 5]:
            corTransporte = VERDE
        elif reg['Transporte'] in [1, 6]:
            corTransporte = AMARELO
        else:
            corTransporte = VERMELHO

        aguaSTR = f"{corAgua}{reg['Agua']:<10.2f}{RESET}"
        energiaSTR = f"{corEnergia}{reg['Energia']:<14.2f}{RESET}"
        recicladoSTR = f"{corReciclado}{reg['Porcentagem Residuos']:<12}{RESET}"
        transporteSTR = f"{corTransporte}{reg['Transporte']:<10}{RESET}"
        
        print(f"{f'[{reg['id']}]':<4} {reg['Data']:<15} {aguaSTR} {energiaSTR} "
              f"{reg['Residuos']:<17.2f} {recicladoSTR} {transporteSTR}")
        
def seFloat(mensagem, minimo=None, maximo=None, permitirZero=False,
            msgErroMin = 'O valor nao atinge o minimo necessario!',
            msgErroMax = 'O valor excede o maximo permitido!'):
    while True:
        try:
            num = float(input(mensagem))
            if (minimo is not None and (num < minimo or (num ==0 and not permitirZero))):
                print(f'\033[91m{msgErroMin}\033[m')
            elif maximo is not None and num > maximo:
                print(f'\033[91m{msgErroMax}\033[m')
            else:
                return num
        except ValueError:
            print(f'\033[91mValor invalido, Tente novamente!\033[m')

def seInt(mensagem, minimo=None, maximo=None,
          msgErro = 'O valor esta fora do intervalo permitido!'):
    while True:
        try:
            valor = int(input(mensagem))
            if (minimo is not None and valor < minimo) or (maximo is not None and valor > maximo):
                print(f"\033[91m{msgErro}\033[m")
            else:
                return valor
        except ValueError:
            print("\033[91mValor inválido, tente novamente!\033[m")

def registrarConsumo():
    global proximoID

    hoje = datetime.datetime.today()

    print('\033[093mComeçando o registro do dia.\033[m')
    litrosAgua = seFloat('Quantos litros de agua você consumiu hoje? (aproximadamente): ',
                        minimo = 0.01,
                        msgErroMin ='\033[091mA quantidade de água não pode ser negativa! Tente novamente.\033[m')
    energia = seFloat('Quantos kWh de energia elétrica você consumiu hoje?: ',
                        minimo = 0.01,
                        msgErroMin ="\033[091mA quantidade de energia não pode ser negativa! Tente novamente.\033[m")
    residuo = seFloat('Quantos kg de resíduos você gerou hoje?: ',
                        minimo = 0.01,
                        msgErroMin = "\033[091mA quantidade de resíduo não pode ser negativa! Tente novamente.\033[m")
    residuoPorcentagem = seInt('Dos resíduos gerados, quantos foram reciclados? (em %): ',
                        minimo = 1,
                        maximo = 100,
                        msgErro = "\033[091mA porcentagem de resíduo deve ser um numero entre 0 e 100! Tente novamente.\033[m")
    print('1. Transporte público (Ônibus, metrô, trem).\n'
                                '2. Bicicleta.\n'
                                '3. Caminhada.\n'
                                '4. Carro (Combustível fósseis).\n'
                                '5. Carro elétrico.\n'
                                '6. Carona compartilhada.')
    meioTransporte = seInt('Qual meio de transporte você utilizou hoje?: ',
                        minimo = 1,
                        maximo = 6,
                        msgErro = "\033[091mEscolha uma das opçôes! Tente novamente.\033[m")
    dadosDia = {
        'id': proximoID,
        'Data': hoje.strftime('%d/%m/%Y'),
        'Agua': litrosAgua,
        'Energia': energia,
        'Residuos': residuo,
        'Porcentagem Residuos': residuoPorcentagem,
        'Transporte': meioTransporte
    }
    registros.append(dadosDia)
    proximoID += 1

    print('\033[093mRegisto diario finalizado.\033[m')
    if voltarMenu('Gostaria de vizualizar os seus dados registrados de hoje? (s/n): '):
        listarRegistros()

    if not voltarMenu('Gostaria de voltar ao menu principal (s/n): '):
        print('Obrigado, até a proxima vez.')
        exit()

def alterarRegistro():
    print("\n\033[093mAlteração de registro.\033[m\n")
    if not registros:
        print("\033[91mNenhum registro encontrado.\033[m\n")
        return
    
    listarRegistros()

    idsValidos = [reg['id'] for reg in registros]
    idAlterar = seInt(f"Digite o ID do registro que deseja alterar: ",
                        minimo = min(idsValidos), maximo = max(idsValidos), msgErro = '\033[91mEscolha um ID existente\033[m')
    registroEncontrado = None
    for reg in registros:
        if reg['id'] == idAlterar:
            registroEncontrado = reg
            break
    if registroEncontrado:
        while True:
            print(f"\nAlterando registro do ID: {idAlterar}. O que deseja modificar?")
            print("1. Água")
            print("2. Energia")
            print("3. Resíduos (Kg)")
            print("4. Porcentagem Reciclada")
            print("5. Meio de Transporte")
            print("6. Voltar ao menu principal")

            escolha = seInt("Escolha o campo para alterar: ", minimo=1, maximo=6, msgErro = '\033[91mEscolha uma opção existente\033[m' )
            
            if escolha == 1:
                novoValor = seFloat(f"Valor atual da Água: {registroEncontrado['Agua']}. Novo valor: ", minimo=0.01)
                registroEncontrado['Agua'] = novoValor
                print(f"\033[92mValor da Água alterado com sucesso!\033[m")
            
            elif escolha == 2:
                novoValor = seFloat(f"Valor atual de Energia: {registroEncontrado['Energia']}. Novo valor: ", minimo=0.01)
                registroEncontrado['Energia'] = novoValor
                print(f"\033[92mValor de Energia alterado com sucesso!\033[m")

            elif escolha == 3:
                novo_valor = seFloat(f"Valor atual de Resíduos: {registroEncontrado['Residuos']}. Novo valor: ", minimo=0.01)
                registroEncontrado['Residuos'] = novoValor
                print(f"\033[92mValor de Resíduos alterado com sucesso!\033[m")

            elif escolha == 4:
                novoValor = seInt(f"Valor atual de % Reciclado: {registroEncontrado['Porcentagem Residuos']}. Novo valor: ", minimo=0, maximo=100)
                registroEncontrado['Porcentagem Residuos'] = novoValor
                print(f"\033[92mPorcentagem de reciclados alterada com sucesso!\033[m")

            elif escolha == 5:
                novoValor = seInt(f"Valor atual do Transporte: {registroEncontrado['Transporte']}. Novo valor (1-6): ", minimo=1, maximo=6)
                registroEncontrado['Transporte'] = novoValor
                print(f"\033[92mMeio de transporte alterado com sucesso!\033[m")
            
            elif escolha == 6:
                print("\033[093mVoltando ao menu principal...\033[m")
                break
    else:
        print(f"\033[91mRegistro com ID {idAlterar} não encontrado!\033[m")

def excluirRegistro():
    print("\n\033[093mExclusão de registro.\033[m\n")
    if not registros:
        print("\033[91mNenhum registro encontrado.\033[m\n")
        return

    listarRegistros()

    idsValidos = [reg['id'] for reg in registros]
    idExcluir = seInt(f"Digite o ID do registro que deseja exlcuir: ",
                        minimo = min(idsValidos), maximo = max(idsValidos), msgErro = '\033[91mEscolha um ID existente\033[m')
    registroEncontrado = None
    for reg in registros:
        if reg['id'] == idExcluir:
            registroEncontrado = reg
            break
    if registroEncontrado:
        print(f"\nRegistro encontrado:")
        for chave, valor in registroEncontrado.items():
            print(f"  {chave.capitalize()}: {valor}")
        confirmacao = input("\nTem certeza que deseja excluir este registro? (s/n): ").lower().strip()
        
        if confirmacao == 's':
            registros.remove(registroEncontrado)
            print("\n\033[92mRegistro excluído com sucesso!\033[m")
        else:
            print("\n\033[93mOperação de exclusão cancelada.\033[m")
    else:
        print("\n\033[91mErro: Registro não encontrado.\033[m")



def menu():
    while True:
        print("\033[095mBem-vindo ao Sistema de Monitoramento de Sustentabilidade Pessoal!\033[m\n"
        "[1] Registrar consumo diário.\n"
        "[2] Alterar registro diário.\n"
        "[3] Excluir registro diário.\n"
        "[4] Sair do programa.")
        escolha = input('Escolha uma opção: ')

        if escolha == '1':
            registrarConsumo()
        elif escolha == '2':
            alterarRegistro()
        elif escolha == '3':
            excluirRegistro()
        elif escolha == '4':
            print('Saindo do programa.')
            break
        else:
            print("\033[91mOpção inválida. Tente novamente.\033[m")

menu()
