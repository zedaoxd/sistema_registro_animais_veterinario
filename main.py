from colorama import Fore, Style
import time


class Animal:
    def __init__(self, nome_animal, nome_dono, especie, raca, descricao):
        self.__nome_animal = nome_animal
        self.__nome_dono = nome_dono
        self.__especie = especie
        self.__raca = raca
        self.__descricao = descricao
        self.__status = 'Internado'

    @property
    def status(self):
        time.sleep(0.5)
        return f'\n{self.__nome_animal} está \033[31m{self.__status}\033[m'

    @property
    def nome_animal(self):
        return self.__nome_animal

    @status.setter
    def status(self, novo_status):
        self.__status = novo_status

    def mostra_tudo(self):
        return f'Nome do animal: \033[36m{self.__nome_animal}\033[m Especie: \033[36m{self.__especie}\033[m ' \
               f'Raça: \033[36m{self.__raca}\033[m Descrição: \033[36m{self.__descricao}\033[m Status: ' \
               f'\033[31m{self.__status}\033[m'


def indic():
    contador = 0
    for animais in registro:
        contador += 1
        print(Fore.LIGHTYELLOW_EX + '=-' * 30, Style.RESET_ALL)
        print(Fore.BLUE + f'[{contador}]', Style.RESET_ALL + f'{animais.nome_animal}')
    return contador


def menu():
    print(Fore.LIGHTYELLOW_EX + '=-' * 30)
    print(Fore.BLUE + 'ESCOLHA:'.center(50))
    print(Fore.BLUE + '[1]', Style.RESET_ALL + 'Registrar animal')
    print(Fore.BLUE + '[2]', Style.RESET_ALL + 'Listar todos os animais')
    print(Fore.BLUE + '[3]', Style.RESET_ALL + 'Verificar status do animal')
    print(Fore.BLUE + '[4]', Style.RESET_ALL + 'Remover animal')
    print(Fore.BLUE + '[5]', Style.RESET_ALL + 'Mudar status do animal')
    print(Fore.RED + '[0]', Style.RESET_ALL + 'Para sair')
    print(Fore.LIGHTYELLOW_EX + '=-' * 30, Style.RESET_ALL)
    escolha = int(input())
    return escolha


registro = []
fazer = menu()
while fazer:
    if 0 < fazer > 5:
        exit()
    elif fazer == 1:
        nome_dono_ = input('Digite o nome do dono: ')
        nome_animal_ = input('Digite o nome do animal: ')
        especie_ = input('Qual especie é: ')
        raca_ = input('Qual a raça do animal: ')
        descricao_ = input('Descreva brevemente o problema dele: ')
        registro.append(Animal(nome_animal_, nome_dono_, especie_, raca_, descricao_))
        time.sleep(0.5)
        print(Fore.GREEN + '\nAnimal registrado com sucesso!!', Style.RESET_ALL)
        time.sleep(0.5)
    if len(registro) >= 1:
        if fazer == 2:
            for animais in registro:
                print(Fore.LIGHTYELLOW_EX + '=-' * 30, Style.RESET_ALL)
                time.sleep(0.5)
                print(animais.mostra_tudo())
                time.sleep(0.5)
                print(Fore.LIGHTYELLOW_EX + '=-' * 30, Style.RESET_ALL)
        elif fazer == 3:
            time.sleep(0.5)
            indic()
            indice_status = int(input('\nDigite o número do animal que deseja ver o status: '))
            print(registro[indice_status - 1].status)
            time.sleep(0.5)
        elif fazer == 4:
            indic()
            indice_delete = int(input('Digite o número do animal que você deseja deletar: '))
            registro.pop(indice_delete - 1)
            time.sleep(0.5)
            print(Fore.RED + 'Animal deletado com sucesso!', Style.RESET_ALL)
            time.sleep(0.5)
        elif fazer == 5:
            indic()
            indice_muda_status = int(input('Digite o número do animal que deseja ver o status: '))
            registro[indice_muda_status - 1].status = input('Digite o novo status para o animal: ')
            time.sleep(0.5)
            print(Fore.RED + 'Status modificado', Style.RESET_ALL)
    else:
        time.sleep(0.5)
        print('Nenhum animal registrado')
        time.sleep(0.3)
    fazer = menu()
