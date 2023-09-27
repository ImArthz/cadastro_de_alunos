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

    def Consultar_aluno(self):
        return f'{super().Consultar_pessoa()}, Matrícula: {self.getMatricula()}'

    def getMatricula(self):
        return self.__matricula

    def inserir_info(self, info):
        self.informacoes.append(info)

    def imprimir_todas_informacoes(self):
        print("-----------------------------------------------")
        print(f"Informações de {self.getNome()}:")
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
                    print(f"matricula gerada : {temp_aluno_matricula}")
                    break

            novo_aluno = Aluno(temp_aluno_nome, temp_aluno_idade, temp_aluno_matricula)
            alunos.append(novo_aluno)
            return "Aluno cadastrado com sucesso!"
        except Exception as error:
            return f"Erro ao cadastrar aluno: {str(error)}"

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
                while True:
                    escolha = input("Deseja visualizar os alunos matriculados?\n\tSim\n\tNão: ").lower()
                    Gerenciadora.Listar_alunos(alunos) if escolha in ('sim', 's') else (
                        print("Voltando ao menu...") if escolha in ('não', 'n') else print("Escolha inválida."))
                    if escolha in ('sim', 's', 'não', 'n'):
                        break
        except Exception as error:
            return f"Erro ao consultar aluno : {str(error)}"

    @staticmethod
    def Atualizar_aluno(matricula, alunos):
        try:
            encontrado = False
            for aluno in alunos:
                if aluno.getMatricula() == matricula:
                    temp_aluno_matricula = aluno.getMatricula()
                    # Delete aluno criar metodo
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
                    return "Aluno atualizado com sucesso!"
                    encontrado = True
                    break
            if not encontrado:
                print("Não existe nenhum aluno com este número de matrícula.")
                while True:
                    escolha = input("Deseja visualizar os alunos matriculados?\n\tSim\n\tNão: ").lower()
                    Gerenciadora.Listar_alunos(alunos) if escolha in ('sim', 's') else (
                        print("Voltando ao menu...") if escolha in ('não', 'n') else print("Escolha inválida."))
                    if escolha in ('sim', 's', 'não', 'n'):
                        break

        except Exception as error:
            return f"Erro ao atualizar aluno : {str(error)}"

    @staticmethod
    def Excluir_aluno(matricula, alunos):
        try:
            encontrado = False
            for aluno in alunos:
                if aluno.getMatricula() == matricula:
                    alunos.remove(aluno)
                    encontrado = True
                    break  # Saia do loop após encontrar e excluir o aluno

            if encontrado:
                return "Aluno excluído com sucesso!"
            else:
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
            return f"Erro ao excluir aluno: {str(error)}"

    @staticmethod
    def Menu(alunos):
        while True:
            if __name__ == "__main__":
                alunos = []  # Lista para armazenar os objetos Aluno

                while True:
                    print("---------------------------------------------------------")
                    print("\t\t MENU ")
                    print("---------------------------------------------------------")
                    print("1- Criar Aluno")
                    print("2- Buscar Aluno")
                    print("3- Atualizar Aluno")
                    print("4- Excluir Aluno")
                    print("5- Sair")

                    try:
                        escolha = int(input("Digite o número da opção desejada: "))
                        if escolha not in (1, 2, 3, 4, 5):
                            raise ValueError("Opção inválida")
                    except ValueError:
                        print("Opção inválida. Por favor, digite um número de opção válido (1, 2, 3, 4 ou 5).")
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
                                Gerenciadora.Consultar_aluno(temp_matricula, alunos)
                                break  # Saia do loop após consultar o aluno
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
                                escolha_aux = input(f"Você está prestes a excluir o aluno de matrícula {temp_matricula2} tem certeza ? (S/N)").lower()
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
                        print("Saindo do programa...")
                        break  # Saia do loop principal e encerre o programa


alunos = []  # Lista para armazenar os objetos Aluno
Gerenciadora.Menu(alunos)
    

