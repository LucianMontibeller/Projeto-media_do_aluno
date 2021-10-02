import os
import sqlite3
import time


class App():
    def __init__(self):
        self.aluno = {'Nome': '',
                      'Nota1': 0,
                      'Nota2': 0,
                      'Nota3': 0,
                      'Nota4': 0,
                      'Media': 0,
                      'Resultado': '',
                      'Observacao': ''}
        self.cores = {'limpa': '\033[m',
                      'azul': '\033[34m',
                      'amarelo': '\033[33m',
                      'vermelho': '\033[31m',
                      'verde': '\033[32m',
                      'azul_claro': '\033[36m'}

    def cabecalho(self):
        os.system('clear')
        time.sleep(0.05)
        print('#'*40)
        time.sleep(0.05)
        print('{:#^48}'.format(' \033[32mESCOLA INTER_CONTINENTAL\033[m '))
        time.sleep(0.05)
        print('{:#^48}'.format(' \033[32mDO\033[m '))
        time.sleep(0.05)
        print('{:#^48}'.format(' \033[32mDEDINHO\033[m '))
        time.sleep(0.05)
        print('#'*40)

    def menu(self):
        os.system('clear')
        self.cabecalho()
        time.sleep(0.05)
        print('{}O que deseja fazer?{}'.format(self.cores['azul_claro'],
                                               self.cores['limpa']))

        time.sleep(0.05)
        print('{}[1]Cadastrar Aluno novo{}'.format(self.cores['verde'],
                                                   self.cores['limpa']))
        time.sleep(0.05)
        print('{}[2]Lista de alunos{}'.format(self.cores['vermelho'],
                                              self.cores['limpa']))
        time.sleep(0.05)
        print('{}[3]Atualizar Cadastro do aluno{}'
              .format(self.cores['amarelo'], self.cores['limpa']))
        time.sleep(0.05)
        print('{}[4]Excluir Cadastro{}'
              .format(self.cores['verde'], self.cores['limpa']))
        time.sleep(0.05)
        print('{}[5]Sair{}'.format(self.cores['azul'], self.cores['limpa']))

        opcao = ''
        while opcao != '1' or opcao != '2' or opcao != '3'or opcao != '4' or opcao != '5' or opcao != '': 
            opcao = input('Selecione uma opcao:')
            print('opcao invalida!')
            if opcao == '1':
                self.add_aluno()
            elif opcao == '2':
                self.lista_aluno()
            elif opcao == '3':
                self.atualizar()
            elif opcao == '4':
                self.deletar()
            elif opcao == '5':
                self.sair()

    def add_aluno(self):
        while True:
            os.system('clear')
            self.cabecalho()
            print('{:#^48}'.format(' \033[32mCADASTRO\033[m '))
            print('{:#^48}'.format(' \033[32mDO\033[m '))
            print('{:#^48}'.format(' \033[32mALUNO(A)\033[m '))
            print('#'*40)
            print()
            opcao = input('\033[31mDesejar cadastrar Novo Aluno? [S/N]:\033[m').lower().strip()
            while opcao != 'n' and opcao != 's':
                print('{}Opção invalida: tente S ou N{}'.format(self.cores['amarelo'],self.cores['limpa']))
                opcao = input('\033[32mDesejar cadastrar Novo Aluno? [S/N]:\033[m').lower().strip()

            if opcao == 's':
                print()

                print('{}CADASTRO EM ANDAMENTO{}'.format(self.cores['azul_claro'],self.cores['limpa']))
                print()
                self.aluno['Nome'] = input('{}Nome:{}'.format(self.cores['verde'],self.cores['limpa'])).lower()
                db = sqlite3.connect('connection')
                cursor = db.cursor()
                cursor.execute('SELECT * FROM contacts')
                results = cursor.fetchall()

                for row in results:
                    if self.aluno['Nome'] in row:
                        print('{}Este usuário já existe!{}'.format(self.cores['vermelho'],self.cores['limpa']))
                        time.sleep(2)
                        self.add_aluno()

                self.aluno['Nota1'] = float(input('{}1°Nota:{} '.format(self.cores['azul_claro'],self.cores['limpa'])))
                self.aluno['Nota2'] = float(input('{}2°Nota:{} '.format(self.cores['amarelo'],self.cores['limpa'])))
                self.aluno['Nota3'] = float(input('3°Nota:'.format(self.cores['azul'],self.cores['limpa'])))
                self.aluno['Nota4'] = float(input('{}4°Nota: {}'.format(self.cores['verde'],self.cores['limpa'])))
                self.aluno['Media'] = (self.aluno['Nota1'] + self.aluno['Nota2']+self.aluno['Nota3']+self.aluno['Nota4'])/4

                if self.aluno['Media'] >= 7.0:
                    self.aluno['Resultado'] = '{}APROVADO{}'.format(self.cores['verde'],self.cores['limpa'])
                    self.aluno['Observacao']= '{}Este ser tem algum futuro!{}'.format(self.cores['azul_claro'],self.cores['limpa'])
                else:
                    self.aluno['Resultado'] = '{}REPROVADO{}'.format(self.cores['amarelo'],self.cores['limpa'])
                    self.aluno['Observacao'] = '{}Pessoa BURRA nem sei por que veio ao Mundo{}'.format(self.cores['vermelho'],self.cores['limpa'])
                print('Média:{}{}{}'.format(self.cores['verde'],self.aluno['Media'],self.cores['limpa']))
                print('Resultado:{}{}{} '.format(self.cores['azul_claro'],self.aluno['Resultado'],self.cores['limpa']))
                print('Observação:{}{}{} '.format(self.cores['vermelho'],self.aluno['Observacao'],self.cores['limpa']))
                cursor.execute(""" INSERT INTO contacts
                                (Nome,Nota1,Nota2,Nota3,Nota4,
                                Media,Resultado,Observacao)
                                VALUES(?,?,?,?,?,?,?,?)""",
                                (self.aluno['Nome'],self.aluno['Nota1'],self.aluno['Nota2'],
                                self.aluno['Nota3'],self.aluno['Nota4'],self.aluno['Media'],
                                self.aluno['Resultado'],self.aluno['Observacao']))
                db.commit()
                opcao = input('{}Deseja continuar cadastrando? [s/n]:{}'.format(self.cores['verde'],self.cores['limpa'])).lower() 
                if opcao == 's':
                    continue
                else:
                    db.close()
                    os.system('clear')
                    self.menu()
                    break
            elif opcao == 'n':
                self.menu()

            
    def lista_aluno(self):
        count_1 = 0
        count_2 = 0
        db = sqlite3.connect('connection')
        cursor = db.cursor()
        os.system('clear')
        print('#'*40)
        time.sleep(0.05)
        print('{:#^48}'.format(' \033[32mESCOLA INTER_CONTINENTAL\033[m '))
        time.sleep(0.05)
        print('{:#^48}'.format(' \033[32mDO\033[m '))
        time.sleep(0.05)
        print('{:#^48}'.format(' \033[32mDEDINHO\033[m '))
        time.sleep(0.05)
        print('#'*40)
        time.sleep(0.05)
        print('#'*40)
        time.sleep(0.05)
        print('{:#^48}'.format(' \033[36mLISTA\033[m '))
        print('{:#^48}'.format(' \033[36mDOS\033[m '))
        time.sleep(0.05)
        print('{:#^48}'.format(' \033[36mALUNOS CADASTRADOS\033[m '))
        time.sleep(0.05)
        print('#'*40)
        time.sleep(0.05)
        cursor.execute('SELECT * FROM contacts')
        results = cursor.fetchall()
        print()
        for row in results:
            print('#'*50)
            time.sleep(0.02)
            print('Nome:',row[0])
            time.sleep(0.02)
            print('1°Nota:',row[1])
            time.sleep(0.02)
            print('2°Nota:',row[2])
            time.sleep(0.02)
            print('3°Nota:',row[3])
            time.sleep(0.02)
            print('4°Nota:',row[4])
            time.sleep(0.02)
            print('Média:',row[5])
            time.sleep(0.02)
            print('Resultado:',row[6])
            time.sleep(0.02)
            print('Observação:',row[7])
            time.sleep(0.02)
            print('#'*50)


            count_1 += 1
            if count_1 == 2:
                input('Precione Qualquer tecla para listar mais alunos!')

                count_1 = 0
                os.system('clear')
                print()
        print('Final dos Resultados')
        print()
        option = input('Aperte [A] Para Atualizar,[D]para deletar,[M]voltar ao Menu ').lower()
        while option != 'a' or option != 'd' or option != 'm' and option == '':
            print('Opcao invalida!')
            option = input('Aperte [A] Para Atualizar,[D]para deletar,[M]voltar ao Menu ').lower()
            if option == 'a':
                self.atualizar()
            elif option == 'd':
                self.deletar()
            elif option == 'm':
                self.menu()    
            print()

    def atualizar(self):
        print('ATUALIZAR CADASTROS')
        print()
        self.aluno['Nome'] = input('Busque um Nome cadastrado:')
        confirm = input('Tem certeza? [S/N]:').lower()
        if confirm == 's':
            db = sqlite3.connect('connection')
            cursor = db.cursor()
            cursor.execute('SELECT * FROM contacts')
            results = cursor.fetchall()
            print()
            for row in results:
                if self.aluno['Nome'] in row[0]:
                    print('#'*50)
                    time.sleep(0.02)
                    print('Nome:',row[0])
                    time.sleep(0.02)
                    print('1°Nota:',row[1])
                    time.sleep(0.02)
                    print('2°Nota:',row[2])
                    time.sleep(0.02)
                    print('3°Nota:',row[3])
                    time.sleep(0.02)
                    print('4°Nota:',row[4])
                    time.sleep(0.02)
                    print('Média:',row[5])
                    time.sleep(0.02)
                    print('Resultado:',row[6])
                    time.sleep(0.02)
                    print('Observação:',row[7])
                    time.sleep(0.02)
                    print('#'*50)


            self.aluno['Nome'] = input('digite o nome para atualizar:')
            atualizar_nota = input('Atualizar nota do aluno?[S/N]:').lower()
            if atualizar_nota == 's':
                self.aluno['Nota1'] = input('1°Nota: ')
                self.aluno['Nota2'] = input('2°Nota: ')
                self.aluno['Nota3'] = input('3°Nota: ')
                self.aluno['Nota4'] = input('4°Nota: ')
                cursor.execute('UPDATE contacts SET Nota1 = ? WHERE Nome = ?', (self.aluno['Nota1'], self.aluno['Nome']))
                cursor.execute('UPDATE contacts SET Nota2 = ? WHERE Nome = ?', (self.aluno['Nota2'], self.aluno['Nome']))
                cursor.execute('UPDATE contacts SET Nota3 = ? WHERE Nome = ?', (self.aluno['Nota3'], self.aluno['Nome']))
                cursor.execute('UPDATE contacts SET Nota4 = ? WHERE Nome = ?', (self.aluno['Nota4'], self.aluno['Nome']))
                db.commit()
                print('Cadastro atualizado com sucesso.')
                time.sleep(2)
                self.menu()
            else:
                print('SAINDO...')
                time.sleep(3)
                self.menu()



    def deletar(self):
        print('DELETAR CADASTROS')
        print()
        name = input('Digite o Nome do aluno para deletar: ')
        confirm = input('Tem certeza? [S/N]:').lower()
        if confirm == 's':
            db = sqlite3.connect('connection')
            cursor =db.cursor()
            cursor.execute('DELETE FROM contacts where Nome = ?',(name,))
            db.commit()
            print('Cadastro deletado com sucesso.')
            time.sleep(2)
            self.menu()
        else:
            print('SAINDO...')
            time.sleep(3)
            self.menu()

    def sair(self):
        confirm = input('Deseja sair do sistema? [S/N:').lower()
        if confirm == 's':
            print('SAINDO DO SISTEMA...')
            time.sleep(2)
            print('..........')
            time.sleep(0.05)
            print('......')
            time.sleep(0.05)
            print('...')
            time.sleep(0.05)
            print('.')
            exit()
        else:
            print('Voltando pro Menu.')
            time.sleep(2)
            self.menu()

    def main(self):
        os.system('clear')
        if os.path.isfile('connection'):
            db = sqlite3.connect('connection')
            time.sleep(1)
            print()
            print('CONECTADO AO BANCO DE DADOS')
            time.sleep(1.5)
            self.menu()
        else:
            print('ESTA CONEXÃO NÃO EXISTE')
            print()
            time.sleep(1)
            print()
            print('CRIANDO NOVA CONEXÃO')
            time.sleep(1)
            db = sqlite3.connect('connection')

            cursor = db.cursor()
            cursor.execute("""CREATE TABLE contacts
                           (Nome TEXT,Nota1 REAL,Nota2 REAL,
                           Nota3 REAL,Nota4 REAL,Media REAL,
                           Resultado TEXT,Observacao TEXT);""")


contato_aluno = App()
contato_aluno.main()







