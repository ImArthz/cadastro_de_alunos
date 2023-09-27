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

    def adicionar_disciplina(self, nome_disciplina, professor, notas, informacoes):
        nova_disciplina = Disciplina(nome_disciplina, professor, notas, informacoes)
        self.informacoes.append(nova_disciplina)

    def imprimir_todas_informacoes(self):
        print("-----------------------------------------------")
        print(f"Nome : \t{self.getNome()} \nMatrícula: \t\t{self.getMatricula()} \nIdade: \t\t{self.getIdade()} ")
        print("-----------------------------------------------")
        for disciplina in self.informacoes:
            disciplina.imprimir_informacoes()

    def atualizar_informacoes(self):
        while True:
            print("1- Atualizar informações pessoais")
            print("2- Atualizar informações de disciplina")
            print("3- Atualizar ambas")
            print("4- Sair")
            escolha = input("Digite a opção desejada: ")
            if escolha == "1":
                self.atualizar_pessoais()
            elif escolha == "2":
                self.atualizar_disciplina()
            elif escolha == "3":
                self.atualizar_pessoais()
                self.atualizar_disciplina()
            elif escolha == "4":
                break
            else:
                print("Opção inválida. Tente novamente.")

    def atualizar_pessoais(self):
        try:
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

            self.__nome = temp_aluno_nome
            self.__idade = temp_aluno_idade
            print("Informações pessoais atualizadas com sucesso!")

        except Exception as error:
            print(f"Erro ao atualizar informações pessoais: {str(error)}")

    def atualizar_disciplina(self):
        try:
            while True:
                disciplina_atualizar = input("Digite o nome da disciplina a ser atualizada: ")
                disciplina_existente = next((disc for disc in self.informacoes if disc.nome_disciplina == disciplina_atualizar), None)
                if disciplina_existente:
                    notas = input("Digite as notas atualizadas (separadas por vírgula): ").split(',')
                    informacoes = input("Digite informações adicionais atualizadas: ")
                    disciplina_existente.notas = notas
                    disciplina_existente.informacoes = informacoes
                    print("Informações da disciplina atualizadas com sucesso!")
                    break
                else:
                    print("Disciplina não encontrada. Tente novamente.")

        except Exception as error:
            print(f"Erro ao atualizar informações da disciplina: {str(error)}")

# Classe Disciplina
class Disciplina:
    def __init__(self, nome_disciplina, professor, notas, informacoes):
        self.nome_disciplina = nome_disciplina
        self.professor = professor
        self.notas = notas
        self.informacoes = informacoes

    def imprimir_informacoes(self):
        print(f"Disciplina: \t{self.nome_disciplina}")
        print(f"Professor: \t{self.professor.getNome()}")
        print(f"Notas: \t{', '.join(self.notas)}")
        print(f"Informações: \t{self.informacoes}")

# Classe Professor (Pessoa <- Pai)
class Professor(Pessoa):
    def __init__(self, nome, idade, salario, formacao):
        super().__init__(nome, idade)
        self.__salario = salario
        self.__formacao = formacao

    def Consultar_pessoa(self):
        return f'Nome: {self.getNome()}, Idade: {self.getIdade()}'

    def Consultar_professor(self):
        return f'{super().Consultar_pessoa()}, Salário: {self.getSalario()}R$, Formação: {self.getFormacao()}'

    def getSalario(self):
        return self.__salario

    def getFormacao(self):
        return self.__formacao

# Classe Gerenciadora
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
                    aluno.atualizar_informacoes()  # Chama a função de atualização
                    encontrado = True
                    break
            if not encontrado:
                print("Não existe nenhum aluno com este número de matrícula.")
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
                    encontrado = True
                    nome_disciplina = input("Digite o nome da disciplina: ")
                    professor = input("Digite o nome do professor: ")
                    notas = input("Digite as notas (separadas por vírgula): ").split(',')
                    informacoes = input("Digite informações adicionais: ")

                    # Verificar se o professor já existe na lista de professores
                    professor_existente = next((p for p in professores if p.getNome() == professor), None)
                    if professor_existente is None:
                        print("Professor não encontrado. Você precisa cadastrar o professor primeiro.")
                        Gerenciadora.Criar_professor(professores)
                        professor_existente = next((p for p in professores if p.getNome() == professor), None)

                    aluno.adicionar_disciplina(nome_disciplina, professor_existente, notas, informacoes)
                    print("Informações da disciplina adicionadas com sucesso!")

            if not encontrado:
                print("Não existe nenhum aluno com esta matrícula.")

        except Exception as error:
            print(f"Erro ao inserir informações do aluno: {str(error)}")

    @staticmethod
    def Imprimir_todos_alunos(alunos):
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
                    print("Nome de professor já existe na lista. Por favor, escolha outro nome.")

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
        print("--------------------------------------------------")
        print("\t\t\t LISTA DE TODOS OS PROFESSORES ")
        print("--------------------------------------------------")
        for professor in professores:
            print(professor.Consultar_professor())

    @staticmethod
    def Atualizar_professor(nome_professor, professores):
        try:
            encontrado = False
            for professor in professores:
                if professor.getNome() == nome_professor:
                    temp_professor_nome = professor.getNome()
                    while True:
                        temp_professor_idade = int(input("Digite a idade atualizada do professor: "))
                        if temp_professor_idade < 0 or temp_professor_idade > 121:
                            raise ValueError("Idade inválida. A idade deve estar entre 0 e 120 anos.")
                        break  # Saia do loop se a entrada for válida

                    while True:
                        temp_professor_salario = float(input("Digite o salário atualizado do professor: "))
                        if temp_professor_salario < 0:
                            raise ValueError("Salário inválido. O salário não pode ser negativo.")
                        break  # Saia do loop se a entrada for válida

                    temp_professor_formacao = input("Digite a formação acadêmica atualizada do professor: ")

                    professor_atualizado = Professor(temp_professor_nome, temp_professor_idade, temp_professor_salario, temp_professor_formacao)
                    professores.remove(professor)
                    professores.append(professor_atualizado)
                    print("Professor atualizado com sucesso!")
                    encontrado = True
                    break

            if not encontrado:
                print("Não existe nenhum professor com este nome.")

        except Exception as error:
            print(f"Erro ao atualizar professor: {str(error)}")

    @staticmethod
    def Excluir_professor(nome_professor, professores):
        try:
            encontrado = False
            for professor in professores:
                if professor.getNome() == nome_professor:
                    professores.remove(professor)
                    encontrado = True
                    print("Professor excluído com sucesso!")
                    break  # Saia do loop após encontrar e excluir o professor

            if not encontrado:
                print("Não existe nenhum professor com este nome.")

        except Exception as error:
            print(f"Erro ao excluir professor: {str(error)}")

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
            print("5- Inserir informações de Aluno")
            print("6- Imprimir todos os Alunos")
            print("7- Criar Professor")
            print("8- Listar Professores")
            print("9- Atualizar Professor")
            print("10- Excluir Professor")
            print("11- Sair")

            try:
                escolha = int(input("Digite o número da opção desejada: "))
                if escolha not in range(1, 12):
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
                    temp_matricula3 = input("Digite a matrícula do aluno para inserir informações: ")
                    aux = input(f"Você digitou {temp_matricula3}. Está correto? (S/N) ").lower()
                    if aux in ('nao', 'n', 'não'):
                        continue  # Volte ao início do loop
                    elif aux in ('sim', 's'):
                        Gerenciadora.Inserir_informacoes_aluno(temp_matricula3, alunos)
                        break  # Saia do loop após inserir as informações
                    else:
                        print("Opção inválida. Por favor, digite 'S' ou 'N'.")
            elif escolha == 6:
                if not alunos:
                    print("Não há alunos cadastrados.")
                else:
                    Gerenciadora.Imprimir_todos_alunos(alunos)
            elif escolha == 7:
                Gerenciadora.Criar_professor(professores)
            elif escolha == 8:
                if not professores:
                    print("Não há professores cadastrados.")
                else:
                    Gerenciadora.Listar_professores(professores)
            elif escolha == 9:
                while True:
                    nome_professor = input("Digite o nome do professor que deseja atualizar: ")
                    aux = input(f"Você digitou {nome_professor}. Está correto? (S/N) ").lower()
                    if aux in ('nao', 'n', 'não'):
                        continue  # Volte ao início do loop
                    elif aux in ('sim', 's'):
                        Gerenciadora.Atualizar_professor(nome_professor, professores)
                        break  # Saia do loop após atualizar o professor
                    else:
                        print("Opção inválida. Por favor, digite 'S' ou 'N'.")
            elif escolha == 10:
                while True:
                    nome_professor = input("Digite o nome do professor que deseja excluir: ")
                    aux = input(f"Você digitou {nome_professor}. Está correto? (S/N) ").lower()
                    if aux in ('nao', 'n', 'não'):
                        continue  # Volte ao início do loop
                    elif aux in ('sim', 's'):
                        escolha_aux = input(f"Você está prestes a excluir o professor {nome_professor}. Tem certeza? (S/N)").lower()
                        if escolha_aux in ('nao', 'n', 'não'):
                            continue
                        elif escolha_aux in ('sim', 's'):
                            Gerenciadora.Excluir_professor(nome_professor, professores)
                            break  # Saia do loop após excluir o professor
                        else:
                            print("Opção inválida. Por favor, digite 'S' ou 'N'.")
                    else:
                        print("Opção inválida. Por favor, digite 'S' ou 'N'.")
            elif escolha == 11:
                print("Saindo do programa...")
                print("-------------------------------------------------------")
                print("\t\t\tPrograma feito por Arthur De Oliveira Mendonça ")
                print("-------------------------------------------------------")
                print("\tLink github : https://github.com/ImArthz/cadastro_de_alunos")
                print("-------------------------------------------------------")
                break  # Saia do loop principal e encerre o programa

if __name__ == "__main__":
    alunos = []  # Lista para armazenar os objetos Aluno
    professores = []  # Lista para armazenar os objetos Professor
    Gerenciadora.Menu(alunos, professores)
