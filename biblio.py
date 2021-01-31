import json
import os
from datetime import date, timedelta
from reportlab.pdfgen import canvas

# variavel que recebe o livro cadastrado
livros = []

# inicializa o arquivo json com os dados salvos
if os.path.exists('biblio.json'):
    with open('biblio.json', encoding='utf8') as f:
        livros = json.load(f)


# salva os dados do livro no json
def salvar():
    with open('biblio.json', 'w', encoding='utf8') as f:
        json.dump(livros, f, ensure_ascii=False, indent=4, separators=(',', ':'))


def login():
    usuario = 'admin'
    senha = 'admin'
    c = 0
    while c < 5:
        user = str(input('DIGITE O USUÁRIO: '))
        password = str(input('DIGITE A SENHA: '))
        if user == usuario and password == senha:
            entrada = True
            limpar()
            return entrada
        else:
            print('TENTE NOVAMENTE!')
            c += 1
    exit()


def limpar():
    print()
    print('-' * 20)
    print()


def voltarMenu():
    voltar = ''
    while voltar != 'NÃO':
        voltar = str(input('DESEJA VOLTAR AO MENU?[SIM/NÃO] '))[:3].strip().upper()
        if voltar == 'SIM':
            limpar()
            menu()
        elif voltar != 'NÃO':
            print('ERRO, TENTE NOVAMENTE')


def cadastrarLivros():
    while True:
        print('CADASTRAR LIVROS')
        codigo = str(input('DIGITE O CÓDIGO DO LIVRO: '))
        for i in livros:
            if codigo == i['CÓDIGO']:
                resposta = str(input('ESSE LIVRO JÁ FOI CADASTRADO, DESEJA ATUALIZÁ-LO? [SIM/NÃO] '))[
                           :3].upper().strip()
                if resposta == 'SIM':
                    atualizarQuantLivros()
                else:
                    menu()
        titulo = str(input('TÍTULO: ')).upper()
        autor = str(input('AUTOR: ')).upper()
        ano = str(input('ANO: '))
        quantidade = int(input('DIGITE A QUANTIDADE QUE DESEJA CADASTRAR: '))
        reservado = str(input('O LIVRO É RESERVADO?[SIM/NÃO] '))[:3].upper().strip()
        categoria = str(input('CATEGORIA: ')).upper()
        tematica = str(input('TEMÁTICA: ')).upper()
        livro = {'CÓDIGO': codigo, 'TÍTULO': titulo, 'AUTOR': autor, 'ANO': ano, 'QUANTIDADE': quantidade,
                 'RESERVADO': reservado, 'CATEGORIA': categoria, 'TEMÁTICA': tematica}
        if livro['RESERVADO'] == 'NÃO':
            livro['ALUGADO'] = 'NÃO'
            livro['QUANTIDADE ALUGADOS'] = 0
        livros.append(livro)
        salvar()
        print('LIVRO CADASTRADO!')
        limpar()
        voltarMenu()


def atualizarQuantLivros():
    print('QUAL LIVRO VOCÊ DESEJA ATUALIZAR?')
    codigo = str(input('DIGITE O CÓDIGO DO LIVRO: ')).strip()

    for i in livros:
        if codigo == i['CÓDIGO']:
            quantidade = int(input('INFORME A QUANTIDADE QUE DESEJA ADICIONAR: '))
            i['QUANTIDADE'] += quantidade
            salvar()
            print('LIVRO ATUALIZADO')
            break
    else:
        print('LIVRO NÃO ENCONTRADO!')
        limpar()
    voltarMenu()


def removerLivros():
    while True:
        print('COMO VOCÊ DESEJA REMOVER?'
              '\n[1] TODOS OS LIVROS ANTES DO ANO 2000'
              '\n[2] PELO TÍTULO')
        opcao = str(input('QUAL SUA OPÇÃO: ')).strip()
        if opcao == '1':
            for i in livros:
                if i['ANO'] < '2000':
                    livros.remove(i)
                    salvar()
                    print('LIVROS REMOVIDOS COM SUCESSO!')
                    break
            else:
                print('LIVRO NÃO ENCONTRADO')
            voltarMenu()
        elif opcao == '2':
            titulo = str(input('DIGITE O TÍTULO DO LIVRO: ')).upper().strip()
            for i in livros:
                if titulo == i['TÍTULO']:
                    livros.remove(i)
                    salvar()
                    print('LIVROS REMOVIDOS COM SUCESSO!')
                    break
            else:
                print('LIVRO NÃO ENCONTRADO')
                limpar()
            voltarMenu()
        else:
            print('TENTE NOVAMENTE!')
            limpar()


def buscarLivros():
    while True:
        print('ESCOLHA UMA OPÇÃO ABAIXO'
              '\n[1] POR ANO'
              '\n[2] POR TÍTULO'
              '\n[3] POR AUTOR'
              '\n[4] POR TEMÁTICA')
        opcao = str(input('QUAL SUA OPÇÃO: ')).strip()
        c = 0
        if opcao == '1':
            ano = str(input('DIGITE O ANO: ')).upper().strip()
            for i in livros:
                c += 1
                if ano == i['ANO']:
                    limpar()
                    for k, v in i.items():
                        print(f'{k} : {v}')
                if c == len(livros):
                    break

            else:
                print('LIVRO NÃO ENCONTRADO')
            voltarMenu()
        elif opcao == '2':
            titulo = str(input('DIGITE O TÍTULO: ')).upper().strip()
            for i in livros:
                if titulo == i['TÍTULO']:
                    for k, v in i.items():
                        print(f'{k} : {v}')
                    break
            else:
                print('LIVRO NÃO ENCONTRADO')
            voltarMenu()
        elif opcao == '3':
            autor = str(input('DIGITE O NOME DO AUTOR: ')).upper().strip()
            for i in livros:
                c += 1
                if autor == i['AUTOR']:
                    for k, v in i.items():
                        print(f'{k} : {v}')
                if c == len(livros):
                    break
            else:
                print('LIVRO NÃO ENCONTRADO')
            voltarMenu()
        elif opcao == '4':
            tematica = str(input('DIGITE A TEMÁTICA: ')).upper()
            for i in livros:
                c += 1
                if tematica == i['TEMÁTICA']:
                    for k, v in i.items():
                        print(f'{k} : {v}')
                if c == len(livros):
                    break
            else:
                print('LIVRO NÃO ENCONTRADO')
            voltarMenu()
        else:
            print('TENTE NOVAMENTE!')


def reservarLivro():
    codigo = str(input('DIGITE O CÓDIGO DO LIVRO: ')).strip()
    for i in livros:
        if codigo == i['CÓDIGO'] and i['RESERVADO'] == 'NÃO':
            i['RESERVADO'] = 'SIM'
            salvar()
            print('LIVRO RESERVADO!')
            break
    else:
        print('CÓDIGO NÃO ENCONTRADO OU LIVRO RESERVADO!')
    voltarMenu()


# data de devolução do aluguel de livros
def devolucao():
    duracaoAluguel = (date.today() + timedelta(days=15))
    return duracaoAluguel.strftime('%d/%m/%Y')


# data atual
def data():
    dataAtual = date.today()
    dataFormat = dataAtual.strftime('%d/%m/%Y')
    return dataFormat


def alugarLivro():
    codigo = str(input('DIGITE O CÓDIGO DO LIVRO QUE DESEJA ALUGAR: ')).strip()
    for i in livros:
        if codigo == i['CÓDIGO']:
            if i['RESERVADO'] == 'NÃO' and i['QUANTIDADE'] >= 1:
                i['QUANTIDADE'] -= 1
                i['ALUGADO'] = 'SIM'
                i['QUANTIDADE ALUGADOS'] += 1
                print('VOCÊ TEM 15 DIAS PARA DEVOLUÇÃO')
                print(f'DATA DO ALUGUEL: {data()}')
                print(f'DATA DA DEVOLUÇÃO: {devolucao()}')
                salvar()
                break
            elif i['QUANTIDADE'] == 0:
                print('QUANTIDADE INSUFICIENTE PARA ALUGAR')
                break
            elif i['RESERVADO'] == 'SIM':
                print('ESTE LIVRO ESTÁ RESERVADO, NÃO PODE SER ALUGADO.')
                break
    else:
        print('LIVRO NÃO ENCONTRADO')
    voltarMenu()


def statusLivro():
    codigo = str(input('DIGITE O CÓDIGO DO LIVRO PARA SABER O STATUS: ')).strip()
    for i in livros:
        if codigo == i['CÓDIGO'] and i['RESERVADO'] == 'NÃO':
            print('QUANTIDADE DESSE LIVRO NO ACERVO: {}'.format(i['QUANTIDADE']))
            print('ALUGADO? {}'.format(i['ALUGADO']))
            if i['ALUGADO'] == 'SIM':
                print(f'DATA DE DEVOLUÇÃO: {devolucao()}')
            print('UNIDADES DISPONÍVEIS PARA ALUGUEL: {}'.format(i['QUANTIDADE']))
            print('LOCALIZAÇÃO: NA CATEGORIA "{}" E TEMÁTICA "{}"'.format(i['CATEGORIA'], i['TEMÁTICA']))
            salvar()
            break
        elif codigo == i['CÓDIGO'] and i['RESERVADO'] == 'SIM':
            print('QUANTIDADE DESSE LIVRO NO ACERVO: {}'.format(i['QUANTIDADE']))
            print('LOCALIZAÇÃO: NA CATEGORIA "{}" E TEMÁTICA "{}"'.format(i['CATEGORIA'], i['TEMÁTICA']))
            break
    else:
        print('LIVRO NÃO ENCONTRADO')
    voltarMenu()


def importarDados():
    if os.path.exists('biblio.json'):
        with open('biblio.json', encoding='utf8') as f:
            livros = json.load(f)
            for i in livros:
                limpar()
                for k, v in i.items():
                    print(f'{k} : {v}')

    voltarMenu()


def relatorioAcervo():
    nome_pdf = input('INFORME O NOME DO PDF: ').lower().strip()
    pdf = canvas.Canvas(f'{nome_pdf}.pdf')
    pdf.setTitle(nome_pdf)
    pdf.setFont("Helvetica-Oblique", 14)
    pdf.drawString(500, 800, data())
    pdf.drawString(250, 750, 'ACERVO')
    x = 720
    quantLivros = 0
    quantAlugados = 0
    for i in livros:
        quantLivros += i['QUANTIDADE']
        if i['RESERVADO'] == 'NÃO':
            quantAlugados += i['QUANTIDADE ALUGADOS']
    pdf.drawString(100, 700, f'TOTAL DE LIVROS: {quantLivros}')
    pdf.drawString(100, 680, 'LIVROS ALUGADOS: {}'.format(quantAlugados))
    pdf.save()
    print(f'{nome_pdf}.pdf CRIADO COM SUCESSO!')
    voltarMenu()


def relatorioCategoria():
    nome_pdf = input('INFORME O NOME DO PDF: ').lower().strip()
    categoria = str(input('INFORME A CATEGORIA: ')).upper()
    pdf = canvas.Canvas(f'{nome_pdf}.pdf')
    pdf.setTitle(nome_pdf)
    pdf.setFont("Helvetica-Oblique", 14)
    pdf.drawString(500, 800, data())
    pdf.drawString(250, 750, 'CATEGORIA')
    quantCategoria = 0
    total = 0
    c = 0
    for i in livros:
        c += 1
        if categoria == i['CATEGORIA']:
            quantCategoria += 1
            total += quantCategoria
        if c == len(livros) and categoria != i['CATEGORIA']:
            print('CATEGORIA NÃO ENCONTRADA')
            limpar()
            menu()
    pdf.drawString(100, 700, f'TOTAL DE LIVROS DA CATEGORIA "{categoria}": {total}')
    print(f'{nome_pdf}.pdf CRIADO COM SUCESSO!')
    pdf.save()
    voltarMenu()


def relatorioTematica():
    nome_pdf = input('INFORME O NOME DO PDF: ').lower().strip()
    tematica = str(input('INFORME A TEMÁTICA: ')).upper()
    pdf = canvas.Canvas(f'{nome_pdf}.pdf')
    pdf.setTitle(nome_pdf)
    pdf.setFont("Helvetica-Oblique", 14)
    pdf.drawString(500, 800, data())
    pdf.drawString(250, 750, 'TEMÁTICA')
    quantTematica = 0
    total = 0
    c = 0
    for i in livros:
        c += 1
        if tematica == i['TEMÁTICA']:
            quantTematica += 1
            total += quantTematica
        if c == len(livros) and tematica != i['TEMÁTICA']:
            print('TEMÁTICA NÃO ENCONTRADA')
            limpar()
            menu()
    pdf.drawString(100, 700, f'TOTAL DE LIVROS COM A TEMÁTICA "{tematica}": {quantTematica}')
    pdf.save()
    print(f'{nome_pdf}.pdf CRIADO COM SUCESSO!')
    voltarMenu()


login()


def menu():
    print('=====MORAIS LIBRARY====='
          '\nESCOLHA UMA OPÇÃO ABAIXO'
          '\n[1] PARA CADASTRAR LIVROS '
          '\n[2] PARA ATUALIZAR LIVROS'
          '\n[3] PARA REMOVER LIVROS'
          '\n[4] PARA BUSCAR LIVROS'
          '\n[5] PARA RESERVAR LIVRO'
          '\n[6] PARA ALUGAR LIVROS'
          '\n[7] PARA STATUS DO LIVRO'
          '\n[8] PARA IMPORTAR DADOS'
          '\n[9] GERAR RELATÓRIO DE ACERVO'
          '\n[10] GERAR RELATÓRIO POR CATEGORIA'
          '\n[11] GERAR RELATÓRIO POR TEMÁTICA'
          '\n[0] PARA SAIR')
    opcao = str(input('QUAL SUA OPÇÃO: ')).strip()
    while True:
        if opcao == '1':
            limpar()
            cadastrarLivros()
        elif opcao == '2':
            limpar()
            atualizarQuantLivros()
        elif opcao == '3':
            limpar()
            removerLivros()
        elif opcao == '4':
            limpar()
            buscarLivros()
        elif opcao == '5':
            limpar()
            reservarLivro()
        elif opcao == '6':
            limpar()
            alugarLivro()
        elif opcao == '7':
            limpar()
            statusLivro()
        elif opcao == '8':
            limpar()
            importarDados()
        elif opcao == '9':
            limpar()
            relatorioAcervo()
        elif opcao == '10':
            limpar()
            relatorioCategoria()
        elif opcao == '11':
            limpar()
            relatorioTematica()
        elif opcao == '0':
            print('ATÉ MAIS!')
            exit()
        else:
            limpar()
            print('NÚMERO ERRADO, TENTE NOVAMENTE!'.format(livros))
            limpar()
            menu()

menu()
