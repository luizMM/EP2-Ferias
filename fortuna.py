import random
from random import randint
from colorama import Fore,Style,init

init()

lista = [ {'titulo':'Quem pintou a "Mona Lisa"?', 'nivel':'facil', 'opcoes':{'A':'Michelangelo', 'B':'Leonardo da Vinci', 'C':'Vincent van Gogh', 'D':'Pablo Picasso'}, 'correta':'B'},
          {'titulo':'Qual é a capital do Brasil?', 'nivel':'facil', 'opcoes':{'A':'São Paulo', 'B':'Rio de Janeiro', 'C':'Brasília', 'D':'Salvador'}, 'correta':'C'}, 
          {'titulo':'Quais são os cinco sentidos humanos?', 'nivel':'medio', 'opcoes':{'A':'Tato, visão, olfato, paladar e audição', 'B':'Tato, visão, olfato, equilíbrio e audição', 'C':'Tato, visão, olfato, paladar e linguagem', 'D':'Tato, visão, olfato, paladar e comunicação'}, 'correta':'A'}, 
          {'titulo':'Quem foi o primerio homem a pisar na Lua?', 'nivel':'medio', 'opcoes':{'A':'Buzz Aldrin', 'B':'Neil Armstrong', 'C':'Yuri Gagarin', 'D':'Alan Shepard'}, 'correta':'B'}, 
          {'titulo':'Qual é o elemento químico com símbolo "Fe"?', 'nivel':'medio', 'opcoes':{'A':'Ferro', 'B':'Fósforo', 'C':'Flúor', 'D':'Mercúrio'}, 'correta':'A'}, 
          {'titulo':'Quem escreveu a peça de teatro "Romeu e Julieta"?', 'nivel':'medio', 'opcoes':{'A':'William Shakespeare', 'B':'Charles Dickens', 'C':'Jane Austen', 'D':'Fyodor Dostoevsky'}, 'correta':'A'}, 
          {'titulo':'Em que ano a Primeira Guerra Mundial começou?', 'nivel':'dificil', 'opcoes':{'A':'1905', 'B':'1914', 'C':'1918', 'D':'1939'}, 'correta':'B'}, 
          {'titulo':'Qual é a montanha mais alta do mundo?', 'nivel':'dificil', 'opcoes':{'A':'K2', 'B':'Everest', 'C':'Monte McKinley (Denali)', 'D':'Monte Kilimanjaro'}, 'correta':'B'}, 
          {'titulo':'Quem foi o primeiro presidente dos Estados Unidos?', 'nivel':'dificil', 'opcoes':{'A':'Thomas Jefferson', 'B':'George Washington', 'C':'Abraham Lincoln', 'D':'John F. Kennedy'}, 'correta':'B'}, 
          {'titulo':'Quem é considerado o pai da psicanálise?', 'nivel':'dificil', 'opcoes':{'A':'Sigmund Freud', 'B':'Carl Jung', 'C':'Ivan Pavlov', 'D':'B.F. Skinner'}, 'correta':'A'}, 
          {'titulo':'Em qual continente está localizado o Deserto do Saara?', 'nivel':'dificl', 'opcoes':{'A':'África', 'B':'Ásia', 'C':'América do Sul', 'D':'Austrália'}, 'correta':'A'}, 
          {'titulo':'Quem foi o líder político sul-africano que lutou contra o apartheid?', 'nivel':'dificil', 'opcoes':{'A':'Nelson Mandela', 'B':'Robert Mugabe', 'C':'Julius Nyerere', 'D':'Haile Selassie'}, 'correta':'A'}, 
          {'titulo':'Qual é o processo pelo qual as plantas convertem luz solar em energia alimentar?', 'nivel':'dificil', 'opcoes':{'A':'Fotossíntese', 'B':'Respiração celular', 'C':'Fermentação', 'D':'Digestão'}, 'correta':'A'}, 
          {'titulo':'Em que país está localizada a cidade de Petra, famosa por suas construções esculpidas em rocha?', 'nivel':'dificil', 'opcoes':{'A':'Egito', 'B':'Grécia', 'C':'Jordânia', 'D':'Índia'}, 'correta':'C'}, 
          {'titulo':'Quem foi o cientista e matemático que formulou as leis do movimento e a lei da gravitação universal?', 'nivel':'dificil', 'opcoes':{'A':'Isaac Newton', 'B':'Albert Einstein', 'C':'Galileu Galilei', 'D':'Johannes Kepler'}, 'correta':'A'},]

def transforma_base(lista):
    dicionario = {}
    if len(lista) == 0:
        return dicionario
    for exr in lista:
        if exr['nivel'] not in dicionario:
            dicionario[exr['nivel']] = []
        dicionario[exr['nivel']].append(exr)
    return dicionario

def valida_questao(questao):
    erros = {}
    
    chaves = ['titulo','nivel','opcoes','correta']
    for c in chaves:
        if c not in questao:
            erros[c] = 'nao_encontrado'
    
    if len(questao) != 4:
        erros['outro'] = 'numero_chaves_invalido'
    
    if 'titulo' in questao.keys():
        if questao['titulo'].strip() == '':
            erros['titulo'] = 'vazio'

    if 'nivel' in questao.keys():
        niveis = ['facil','medio','dificil']
        if questao['nivel'] not in niveis:
            erros['nivel'] = 'valor_errado' 

    if 'opcoes' in questao.keys():
        if len(questao['opcoes']) != 4:
            erros['opcoes'] = 'tamanho_invalido'
        else:
    
            letras = ['A','B','C','D']
            for l in questao['opcoes'].keys():
                if l not in questao['opcoes']:
                    erros['opcoes'] = 'chave_invalida_ou_nao_encontrada'
                else:
                    if questao['opcoes'][l].strip() == '':
                        if 'opcoes' not in erros:
                            erros['opcoes'] = {}
                        erros['opcoes'][l] = 'vazia'
    
    if 'correta' in questao.keys():
        letras = ['A','B','C','D']
        if questao['correta'] not in letras:
            erros['correta'] = 'valor_errado'
    return erros 

def valida_questoes(lista_questoes):
    lista_de_erros = []
    for questao in lista_questoes:
        erros = valida_questao(questao)
        lista_de_erros.append(erros)
    return lista_de_erros

def sorteia_questao(questoes_por_nivel,nivel):
    indice_sorteado = random.randint(0, len(questoes_por_nivel[nivel])-1)
    return questoes_por_nivel[nivel][indice_sorteado]

def sorteia_questao_inedita(questoes_por_nivel,nivel,questoes_sorteadas):
    questao_inedita = sorteia_questao(questoes_por_nivel,nivel)
    while questao_inedita in questoes_sorteadas:
        questao_inedita = sorteia_questao(questoes_por_nivel,nivel)
    questoes_sorteadas.append(questao_inedita)
    return questao_inedita



def questao_para_texto(questao, id):
    return f"----------------------------------------\nQUESTAO {id}\n\n{questao['titulo']}\n\nRESPOSTAS:\nA: {questao['opcoes']['A']}\nB: {questao['opcoes']['B']}\nC: {questao['opcoes']['C']}\nD: {questao['opcoes']['D']}"

def gera_ajuda(questao):
    opc = ['A', 'B', 'C', 'D']
    dicas_sorts = []
    num_dicas = randint(1, 2)
    while num_dicas != 0:
        opc_sorteada =  opc[randint(0, len( opc)-1)]
        if opc_sorteada != questao['correta'] and opc_sorteada not in dicas_sorts:
            dicas_sorts.append(questao['opcoes'][opc_sorteada])
            num_dicas -= 1
    
    if len(dicas_sorts) == 1:
        return f"DICA: Opções certamente erradas: {dicas_sorts[0]}"
    elif len(dicas_sorts) == 2:
        return f"DICA: Opções certamente erradas: {dicas_sorts[0]} | {dicas_sorts[1]}"



niveis = ['facil','medio','dificil']
premios = [1000, 5000, 10000, 50000, 100000, 500000, 1000000]

print(Fore.MAGENTA + '\nOlá! Você está na Fortuna DesSoft e terá a oportunidade de enriquecer!\n' + Style.RESET_ALL)

nome = input('Digite seu nome: ')

print(f'\nOk {nome}, você tem direito a pular 3 vezes e 2 ajudas!')
print(Fore.LIGHTBLUE_EX + 'As opções de resposta são "A", "B", "C", "D", "ajuda", "pula" e "parar"!\n' + Style.RESET_ALL)
input('Aperte ENTER para continuar...')

print('\nO jogo já vai começar! Lá vem a primeira questão!')
input('Aperte ENTER para continuar...')

parar = True
while parar == True:
    questoes_por_nivel = transforma_base(lista)
    questoes_sorteadas = []
    pulos = 3
    ajudas = 2
    premio_atual = 0
    for i,premio in enumerate(premios):
        if i < len(premios)//3:
            nivel = niveis[0]
        elif i < 2*len(premios)//3:
            nivel = niveis[1]
        else:
            nivel = niveis[2]

        questao = sorteia_questao_inedita(questoes_por_nivel, nivel, questoes_sorteadas)
        id_questao = questoes_sorteadas.index(questao) + 1
        print(questao_para_texto(questao, id_questao))

        resposta = input('\nQual sua resposta? ')

        if resposta == 'pula':
            pulos -= 1
            print(Fore.YELLOW + f'Você pulou a questao e tem mais {pulos} pulos.' + Style.RESET_ALL)
            if pulos == 0:
                while resposta == 'pula':
                    print(Fore.RED + 'Você não tem mais pulos.'+ Style.RESET_ALL)
                    resposta = input('\nQual sua resposta? ')
            else:
                continue

        if resposta == 'parar':
            parar = False
            break

        if resposta == 'ajuda':
            while resposta == 'ajuda':
                ajudas -= 1
                if ajudas < 0:
                    print(Fore.RED + 'Você não tem mais ajuda.' + Style.RESET_ALL)
                    resposta = input('\nQual sua resposta? ')
                else:
                    print(Fore.YELLOW + f'{gera_ajuda(questao)}\nVoccê tem mais {ajudas} ajuda' + Style.RESET_ALL)
                    resposta = input('\nQual sua resposta? ')


        if resposta.upper() == questao['correta']:
            premio_atual = premio
            print(Fore.GREEN + '\nResposta correta!' + Style.RESET_ALL)
            print(f'Você agora tem R${premio_atual}')
            if premio_atual == 1000000:
                print(Fore.LIGHTGREEN_EX + '\nParabens! Você é um novo milionario!!' + Style.RESET_ALL)
                break
            input('Aperte ENTER para continuar...')

        else:
            print(Fore.RED + 'Resposta errada! Você perdeu tudo!' + Style.RESET_ALL)
            premio_atual = 0
            break

    print(Fore.BLUE + f'Obrigado por jogar o Fortuna DesSoft {nome}! Você saiu com R${premio_atual}.' + Style.RESET_ALL)
    if resposta != 'parar':
        continuar = input('Deseja continuar jogando? (S/N): ')
        if continuar.upper() == 'N':
            break