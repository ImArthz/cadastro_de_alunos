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
        self.disciplinas = {}

    def Consultar_pessoa(self):
        return f'Nome: {self.getNome()}, Idade: {self.getIdade()}'

    def Consultar_aluno(self):
        return f'{super().Consultar_pessoa()}, Matrícula: {self.getMatricula()}'

    def getMatricula(self):
        return self.__matricula

    def inserir_info(self, info):
        self.informacoes.append(info)

    def adicionar_disciplina(self, nome_disciplina, professor, notas, informacoes):
        self.disciplinas[nome_disciplina] = {
            'Professor': professor,
            'Notas': notas,
            'Informacoes': informacoes
        }

    def imprimir_todas_informacoes(self):
        print("-----------------------------------------------")
        print(f"Nome: {self.getNome()}")
        print(f"Matrícula: {self.getMatricula()}")
        print(f"Idade: {self.getIdade()}")
        print("Disciplinas:")
        for disciplina, info in self.disciplinas.items():
            print(f"  Disciplina: {disciplina}")
            print(f"  Professor: {info['Professor']}")
            print(f"  Notas: {info['Notas']}")
            print(f"  Informações: {info['Informacoes']}")
            print("-----------------------------------------------")

# Classe Professor (Pessoa <- Pai)
class Professor(Pessoa):
    def __init__(self, nome, idade, salario, formacao_academica):
        super().__init__(nome, idade)
        self.salario = salario
        self.formacao_academica = formacao_academica

    def Consultar_pessoa(self):
        return f'Nome: {self.getNome()}, Idade: {self.getIdade()}, Salário: {self.salario}, Formação: {self.formacao_academica}'

class Gerenciadora:
    def __init__(self, alunos, professores):
        self.alunos = alunos
        self.professores = professores

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
    def Inserir_informacoes_aluno(matricula, alunos):
        try:
            encontrado = False
            for aluno in alunos:
                if aluno.getMatricula() == matricula:
                    nome_disciplina = input("Digite o nome da disciplina: ")
                    professor = input("Digite o nome do professor: ")
                    notas = input("Digite as notas da disciplina (separadas por vírgula): ").split(',')
                    informacoes = input("Digite informações sobre a disciplina: ")

                    aluno.adicionar_disciplina(nome_disciplina, professor, notas, informacoes)
                    encontrado = True
                    print("Informações da disciplina adicionadas com sucesso!")
                    break
            if not encontrado:
                print("Não existe nenhum aluno com este número de matrícula.")
        except Exception as error:
            print(f"Erro ao inserir informações da disciplina: {str(error)}")

    @staticmethod
    def Imprimir_todos_alunos(alunos):
        if not alunos:
            print("Não existem alunos cadastrados.")
        else:
            print("Lista de Alunos:")
            for aluno in alunos:
                aluno.imprimir_todas_informacoes()

    @staticmethod
    def Criar_professor(professores):
        try:
            while True:
                temp_professor_nome = input("Digite o nome do professor: ")

                if not any(professor.getNome() == temp_professor_nome for professor in professores):
                    break
                else:
                    print("Nome já existe na lista. Por favor, escolha outro nome.")

            while True:
                temp_professor_idade = int(input("Digite a idade do professor: "))
                if temp_professor_idade < 0 or temp_professor_idade > 121:
                    raise ValueError("Idade inválida. A idade deve estar entre 0 e 120 anos.")
                break  # Saia do loop se a entrada for válida

            while True:
                temp_professor_salario = float(input("Digite o salário do professor: "))
                if temp_professor_salario < 0:
                    raise ValueError("Salário inválido. O salário não pode ser negativo.")
                break  # Saia do loop se a entrada for válida

            temp_professor_formacao = input("Digite a formação acadêmica do professor: ")

            novo_professor = Professor(temp_professor_nome, temp_professor_idade, temp_professor_salario, temp_professor_formacao)
            professores.append(novo_professor)
            print("Professor cadastrado com sucesso!")
        except Exception as error:
            print(f"Erro ao cadastrar professor: {str(error)}")

    @staticmethod
    def Listar_professores(professores):
        if not professores:
            print("Não existem professores cadastrados.")
        else:
            print("Lista de Professores:")
            for professor in professores:
                print(professor.Consultar_pessoa())

    @staticmethod
    def Menu(alunos, professores):
        while True:
            print("---------------------------------------------------------")
            print("\t\t MENU ")
            print("---------------------------------------------------------")
            print("1- Criar Aluno")
            print("2- Buscar Aluno")
            print("3- Atualizar Aluno")
            print("4- Excluir Aluno")
            print("5- Inserir informações do Aluno")
            print("6- Imprimir todos os Alunos")
            print("7- Criar Professor")
            print("8- Listar Professores")
            print("9- Sair")

            try:
                escolha = int(input("Digite o número da opção desejada: "))
                if escolha not in (1, 2, 3, 4, 5, 6, 7, 8, 9):
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
                while True:
                    temp_matricula3 = input("Digite a matrícula do aluno para inserir informações da disciplina: ")
                    aux = input(f"Você digitou {temp_matricula3}. Está correto? (S/N) ").lower()
                    if aux in ('nao', 'n', 'não'):
                        continue  # Volte ao início do loop
                    elif aux in ('sim', 's'):
                        Gerenciadora.Inserir_informacoes_aluno(temp_matricula3, alunos)
                        break  # Saia do loop após inserir informações
                    else:
                        print("Opção inválida. Por favor, digite 'S' ou 'N'.")
            elif escolha == 6:
                Gerenciadora.Imprimir_todos_alunos(alunos)
            elif escolha == 7:
                Gerenciadora.Criar_professor(professores)
            elif escolha == 8:
                Gerenciadora.Listar_professores(professores)
            elif escolha == 9:
                print("Saindo do programa...")
                break  # Saia do loop principal e encerre o programa

if __name__ == "__main__":
    alunos = []  # Lista para armazenar os objetos Aluno
    professores = []  # Lista para armazenar os objetos Professor
    Gerenciadora.Menu(alunos, professores)
