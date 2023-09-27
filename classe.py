import abc
import random

# Classe pessoa abstrata
class Pessoa(abc.ABC):
    def __init__(self, nome, idade):
        self.__nome = nome
        self.__idade = idade

    @abc.abstractmethod
    def Consultar_pessoa(self):
        return f'Nome: {self.getNome()}, Idade: {self.getIdade()}'

    def getNome(self):
        return self.__nome

    def getIdade(self):
        return self.__idade

# Classe filha Aluno (Pessoa <- Pai)
class Aluno(Pessoa):
    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade)
        self.__matricula = matricula
        self.informacoes = []

    def Consultar_pessoa(self):
        return f'Nome: {self.getNome()}, Idade: {self.getIdade()}'

    def Consultar_aluno(self):
        return f'{super().Consultar_pessoa()}, Matrícula: {self.getMatricula()}'

    def getMatricula(self):
        return self.__matricula

    def inserir_info(self, info):
        self.informacoes.append(info)

    def imprimir_todas_informacoes(self):
        print("-----------------------------------------------")
        print(f"Nome : \t\t{self.getNome()} \nMatrícula: \t\t{self.getMatricula()} \nIdade: \t\t{self.getIdade()} ")
        print("-----------------------------------------------")
        for info in self.informacoes:
            print(info)


class Gerenciadora:
    def __init__(self, alunos):
        self.alunos = alunos

    @staticmethod
    def Listar_alunos(alunos):
        for aluno in alunos:
            print(aluno.Consultar_aluno())

    @staticmethod
    def Criar_aluno(alunos):
        try:
            while True:
                temp_aluno_nome = input("Digite o nome do aluno: ")
                if not any(aluno.getNome() == temp_aluno_nome for aluno in alunos):
                    break
                else:
                    print("Nome já existe na lista. Por favor, escolha outro nome.")

            while True:
                temp_aluno_idade = int(input("Digite a idade do aluno: "))
                if temp_aluno_idade < 0 or temp_aluno_idade > 121:
                    raise ValueError("Idade inválida. A idade deve estar entre 0 e 120 anos.")
                break  # Saia do loop se a entrada for válida

            while True:
                temp_aluno_matricula = "2023" + str(random.randint(1, 9)) + str(random.randint(1, 9)) + str(
                    random.randint(1, 9)) + str(random.randint(1, 9)) + str(random.randint(1, 9)) + str(
                    random.randint(1, 9)) + str(random.randint(1, 9)) + str(random.randint(1, 9))

                if not any(aluno.getMatricula() == temp_aluno_matricula for aluno in alunos):
                    print(f"Matrícula gerada: {temp_aluno_matricula}")
                    break

            novo_aluno = Aluno(temp_aluno_nome, temp_aluno_idade, temp_aluno_matricula)
            alunos.append(novo_aluno)
            print("Aluno cadastrado com sucesso!")
        except Exception as error:
            print(f"Erro ao cadastrar aluno: {str(error)}")

    @staticmethod
    def Consultar_aluno(matricula, alunos):
        try:
            encontrado = False
            for aluno in alunos:
                if aluno.getMatricula() == matricula:
                    aluno.imprimir_todas_informacoes()
                    encontrado = True
                    break  # Saia do loop após encontrar o aluno
            if not encontrado:
                print("Não existe nenhum aluno com este número de matrícula.")
                return False  # Nenhum aluno encontrado
            return True  # Aluno encontrado
        except Exception as error:
            print(f"Erro ao consultar aluno: {str(error)}")
            return False  # Ocorreu um erro durante a consulta

    @staticmethod
    def Atualizar_aluno(matricula, alunos):
        try:
            encontrado = False
            for aluno in alunos:
                if aluno.getMatricula() == matricula:
                    temp_aluno_matricula = aluno.getMatricula()
                    while True:
                        temp_aluno_nome = input("Digite o nome atualizado do aluno: ")
                        if not any(aluno.getNome() == temp_aluno_nome for aluno in alunos):
                            break
                        else:
                            print("Nome já existe na lista. Por favor, escolha outro nome.")
                    while True:
                        temp_aluno_idade = int(input("Digite a idade atualizada do aluno: "))
                        if temp_aluno_idade < 0 or temp_aluno_idade > 121:
                            raise ValueError("Idade inválida. A idade deve estar entre 0 e 120 anos.")
                        break  # Saia do loop se a entrada for válida
                    aluno_atualizado = Aluno(temp_aluno_nome, temp_aluno_idade, temp_aluno_matricula)
                    alunos.remove(aluno)
                    alunos.append(aluno_atualizado)
                    print("Aluno atualizado com sucesso!")
                    encontrado = True
                    break
            if not encontrado:
                print("Não existe nenhum aluno com este número de matrícula.")
                while True:
                    escolha = input("Deseja visualizar os alunos matriculados?\n\tSim\n\tNão: ").lower()
                    if escolha in ('sim', 's'):
                        Gerenciadora.Listar_alunos(alunos)
                    elif escolha in ('não', 'n'):
                        break
                    else:
                        print("Escolha inválida.")
        except Exception as error:
            print(f"Erro ao atualizar aluno: {str(error)}")

    @staticmethod
    def Excluir_aluno(matricula, alunos):
        try:
            encontrado = False
            for aluno in alunos:
                if aluno.getMatricula() == matricula:
                    alunos.remove(aluno)
                    encontrado = True
                    print("Aluno excluído com sucesso!")
                    break  # Saia do loop após encontrar e excluir o aluno

            if not encontrado:
                print("Não existe nenhum aluno com esta matrícula.")
                while True:
                    escolha = input("Deseja visualizar os alunos matriculados?\n\tSim (S)\n\tNão (N): ").lower()
                    if escolha in ('s', 'sim'):
                        Gerenciadora.Listar_alunos(alunos)
                    elif escolha in ('n', 'não'):
                        break  # Sair do loop e voltar ao menu principal
                    else:
                        print("Escolha inválida. Por favor, digite 'S' ou 'N'.")

        except Exception as error:
            print(f"Erro ao excluir aluno: {str(error)}")

    @staticmethod
    def Menu(alunos):
        while True:
            print("---------------------------------------------------------")
            print("\t\t MENU ")
            print("---------------------------------------------------------")
            print("1- Criar Aluno")
            print("2- Buscar Aluno")
            print("3- Atualizar Aluno")
            print("4- Excluir Aluno")
            print("5 - Inserir informações  ")
            print("6- Imprimir todos os alunos")
            print("7- Sair")

            try:
                escolha = int(input("Digite o número da opção desejada: "))
                if escolha not in (1, 2, 3, 4, 5,6,7):
                    raise ValueError("Opção inválida")
            except ValueError as e:
                print(f"Erro: {e}")
                continue  # Volte ao início do loop

            if escolha == 1:
                Gerenciadora.Criar_aluno(alunos)
            elif escolha == 2:
                while True:
                    temp_matricula = input("Digite a matrícula que deseja consultar: ")
                    aux = input(f"Você digitou {temp_matricula}. Está correto? (S/N) ").lower()
                    if aux in ('nao', 'n', 'não'):
                        continue  # Volte ao início do loop
                    elif aux in ('sim', 's'):
                        encontrado = Gerenciadora.Consultar_aluno(temp_matricula, alunos)
                        if encontrado:
                            break  # Saia do loop após consultar o aluno
                        else:
                            print("Aluno não encontrado.")
                            break  # Saia do loop também se o aluno não for encontrado
                    else:
                        print("Opção inválida. Por favor, digite 'S' ou 'N'.")
            elif escolha == 3:
                while True:
                    temp_matricula1 = input("Digite a matrícula que deseja atualizar: ")
                    aux = input(f"Você digitou {temp_matricula1}. Está correto? (S/N) ").lower()
                    if aux in ('nao', 'n', 'não'):
                        continue  # Volte ao início do loop
                    elif aux in ('sim', 's'):
                        Gerenciadora.Atualizar_aluno(temp_matricula1, alunos)
                        break  # Saia do loop após consultar o aluno
                    else:
                        print("Opção inválida. Por favor, digite 'S' ou 'N'.")
            elif escolha == 4:
                while True:
                    temp_matricula2 = input("Digite a matrícula que deseja excluir: ")
                    aux = input(f"Você digitou {temp_matricula2}. Está correto? (S/N) ").lower()
                    if aux in ('nao', 'n', 'não'):
                        continue  # Volte ao início do loop
                    elif aux in ('sim', 's'):
                        escolha_aux = input(f"Você está prestes a excluir o aluno de matrícula {temp_matricula2}. Tem certeza? (S/N)").lower()
                        if escolha_aux in ('nao', 'n', 'não'):
                            continue
                        elif escolha_aux in ('sim', 's'):
                            Gerenciadora.Excluir_aluno(temp_matricula2, alunos)
                            break  # Saia do loop após consultar o aluno
                        else:
                            print("Opção inválida. Por favor, digite 'S' ou 'N'.")
                    else:
                        print("Opção inválida. Por favor, digite 'S' ou 'N'.")
            elif escolha == 5:
                pass
            elif escolha == 6:
                pass
            elif escolha == 7:
                print("Saindo do programa...")
                break  # Saia do loop principal e encerre o programa

if __name__ == "__main__":
    alunos = []  # Lista para armazenar os objetos Aluno
    Gerenciadora.Menu(alunos)
