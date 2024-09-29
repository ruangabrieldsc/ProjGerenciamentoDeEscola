

import json

#Arquivos
alunos = "alunos.json"
professores = "professores.json"
disciplinas = "disciplinas.json"
turmas = "turmas.json"
matriculas = "matriculas.json"
lista_random=[]

#Todas as funções

def verificar_codigo(tipo, arquivo):
    lista_random=ler_arquivo(arquivo)
    parar = True
    while parar is True:  # loop para evitar erros no código
        if lista_random != []:
            try:
                codigo = int(input(f"Qual será o código do novo(a) {tipo}? "))
                for i in lista_random:
                    if i["Código"] == codigo:
                        print(f"Um(a) {tipo} com este código já existe.")
                        break
                    else:
                        parar = False
                        return codigo
            except:
                print("Você digitou um valor inválido, códigos só aceitam números.")
        else:
            codigo = int(input(f"Qual será o código do novo(a) {tipo}? "))
            return codigo

def verificar_cod_atualizar(tipo, arquivo, codigoatt):
    lista_random=ler_arquivo(arquivo)
    parar = True
    while parar is True:  # loop para evitar erros no código
        if lista_random != []:
            for i in lista_random:
                if i["Código"] == codigoatt:
                    try:
                        codigoatt=int(input(f"Um(a) {tipo} com este código já existe. Digite outro código. "))
                        break
                    except:
                        print("Você digitou um valor inválido, códigos só aceitam números.")

                else:
                    parar = False
                    return codigoatt

        else:
            return codigoatt

def escolha_menu_princ():
    while True:
        print("MENU PRINCIPAL")
        print("(1) Gerenciar estudantes")
        print("(2) Gerenciar professores")
        print("(3) Gerenciar disciplinas")
        print("(4) Gerenciar turmas")
        print("(5) Gerenciar matrículas")
        print("(9) Sair")

        #Isso retorna uma informação que usamos nas funções no menu de operações

        escolha1 = int(input("O que deseja fazer hoje? "))
        if escolha1 == 1:
            print("Você selecionou 1 (Gerenciar estudantes)")
            return "ESTUDANTES"
        elif escolha1 == 2:
            print("Você selecionou 2 (Gerenciar professores)")
            return "PROFESSORES"
        elif escolha1 == 3:
            print("Você selecionou 3 (Gerenciar disciplinas)")
            return "DISCIPLINAS"
        elif escolha1 == 4:
            print("Você selecionou 4 (Gerenciar turmas)")
            return "TURMAS"
        elif escolha1 == 5:
            print("Você selecionou 5 (Gerenciar matrículas)")
            return "MATRÍCULAS"

        #Sair do programa
        elif escolha1 == 9:
            print("Você selecionou 9 (Sair)")
            return False

        else:
            print("Escolha inválida.")
            continue



def menu_operacoes(tipo):
    voltar_ao_menu = True
    while voltar_ao_menu == True:
        print(f"MENU DE OPERAÇÕES ({tipo})")
        print("(1) Incluir")
        print("(2) Listar")
        print("(3) Atualizar")
        print("(4) Excluir")
        print("(9) Voltar ao menu principal")
        escolha2 = int(input("O que deseja fazer? "))


        #Adaptar as variáveis das funções conforma a escolha do primeiro menu

        if tipo == "ESTUDANTES":
            arquivo = alunos
            tipooperante = "aluno"

        elif tipo == "PROFESSORES":
            arquivo = professores
            tipooperante = "professor"

        elif tipo == "DISCIPLINAS":
            arquivo = disciplinas
            tipooperante = "disciplina"

        elif tipo == "TURMAS":
            arquivo = turmas
            tipooperante = "turma"

        elif tipo == "MATRÍCULAS":
            arquivo = matriculas
            tipooperante = "matricula"


        #Utilizar as funções

        if escolha2 == 1:
            incluir(arquivo, tipooperante)

        elif escolha2 == 2:
            listar(arquivo, tipooperante)

        elif escolha2 == 3:
            lista_random=ler_arquivo(arquivo)
            if len(lista_random) >= 1:
                atualizar(arquivo, tipooperante)
            else:
                print(f"Ainda não existem dados cadastrados deste setor. ")

        elif escolha2 == 4:
            excluir(arquivo, tipooperante)

        elif escolha2 == 9:
            print("Você selecionou (9) Voltar ao menu principal")
            voltar_ao_menu = False
        else:
            print("Escolha inválida.")
            continue


def incluir(arquivo, tipo):

    #Aqui utilizei ifs e elifs para que o código se adapte com o "tipo" que recebemos no menu de oper.
    #Optei por usar isso para não ter que utilizar funções diferentes para cada uma das inclusões

    print("Você selecionou (1) Incluir")
    if tipo == "aluno":
        codigo=verificar_codigo("aluno", arquivo)
        nom = input(f"Qual é o nome do novo(a) {tipo}? ")
        cpf = input(f"Qual é o cpf do novo(a) {tipo}(a)? ")
        dados = {"Código": codigo, "Nome": nom, "CPF": cpf}
        print(f"O(a) {tipo}(a) {nom} foi adicionado ao sistema!")
        lista_random=ler_arquivo(arquivo)
        lista_random.append(dados)
        guardar_arquivo(lista_random, arquivo)
        return dados

    elif tipo == "professor":
        codigo=verificar_codigo("professor", arquivo)
        nom = input(f"Qual é o nome do novo(a) {tipo}? ")
        cpf = input(f"Qual é o cpf do novo(a) {tipo}(a)? ")
        dados = {"Código": codigo, "Nome": nom, "CPF": cpf}
        print(f"O(a) {tipo}(a) {nom} foi adicionado ao sistema!")
        lista_random=ler_arquivo(arquivo)
        lista_random.append(dados)
        guardar_arquivo(lista_random, arquivo)
        return dados

    elif tipo == "disciplina":
        codigo=verificar_codigo("disciplina", arquivo)

        nom = input(f"Qual é o nome do novo(a) {tipo}? ")
        dados = {"Código": codigo, "Nome": nom}
        print(f"A {tipo} {nom} foi adicionado ao sistema!")
        lista_random=ler_arquivo(arquivo)
        lista_random.append(dados)
        guardar_arquivo(lista_random, arquivo)
        return dados

    elif tipo == "turma":
        codigo = verificar_codigo("turma", arquivo)
        while True:
            try:
                codigo_professor = int(input(f"Qual é o código do professor? "))
                break
            except:
                print("Você digitou um valor inválido, códigos só aceitam números.")
        while True:
            try:
                codigo_disciplina = int(input(f"Qual é o código da disciplina? "))
                break
            except:
                print("Você digitou um valor inválido, códigos só aceitam números.")


        dados = {"Código": codigo, "Código_prof": codigo_professor, "Código_disc": codigo_disciplina}
        print(f"A {tipo} foi adicionada ao sistema!")
        lista_random=ler_arquivo(arquivo)
        lista_random.append(dados)
        guardar_arquivo(lista_random, arquivo)
        return dados

    elif tipo == "matricula":
        codigo = verificar_codigo("matricula", arquivo)
        while True:
            try:
                codigo_turma = int(input(f"Qual é o código da turma? "))
                break
            except:
                print("Você digitou um valor inválido, códigos só aceitam números.")

        while True:
            try:
                codigo_aluno = int(input(f"Qual é o código do(a) aluno(a)? "))
                break
            except:
                print("Você digitou um valor inválido, códigos só aceitam números.")

        dados = {"Código": codigo, "Código_turma": codigo_turma, "Código_aluno": codigo_aluno}
        print(f"A {tipo} foi adicionada ao sistema!")
        lista_random=ler_arquivo(arquivo)
        lista_random.append(dados)
        guardar_arquivo(lista_random, arquivo)
        return dados

def listar(arquivo, tipo):
    lista=ler_arquivo(arquivo)
    print("Você selecionou (2) Listar")
    if len(lista) == 0:
        print(f"Não há {tipo}s cadastrados(as). ")
    else:
        for dicionario in lista:
            print(f"Dados ({tipo}): {dicionario}")

def atualizar(arquivo, tipo):

    #basicamente o mesmo esquema da função incluir, mas dessa vez também usamos a função de verificar código

    print("Você selecionou (3) Atualizar.")
    lista=ler_arquivo(arquivo)
    paraatt=0
    codigo=-8766352719
    try:
        paraatt = int(input(f"Qual é o código do(a) {tipo} que deseja atualizar os dados? "))
        for i in lista:
            if i["Código"] == paraatt:
                break
            elif i["Código"] != paraatt:
                continue      #fiz assim pois por algum motivo o else gerava problemas

    except:
        print("Você digitou um valor inválido, códigos só aceitam números.")

    if codigo==-8766352719:
        print(f"Nenhum(a) {tipo} com este código está cadastrado.")

    for i in lista:
        if i["Código"] == paraatt and tipo == "aluno" or i["Código"] == paraatt and tipo == "professor":
            while True:
                try:
                    codigo=int(input(f"Digite o novo código do(a) {tipo}(a) {i["Nome"]} (Código atual:{i["Código"]}): "))
                    break
                except:
                    print("Você digitou um valor inválido, códigos só aceitam números.")

            if codigo == paraatt:
                i["Código"]=codigo
                i["CPF"]= input(f"Digite um novo cpf para o(a) {tipo}(a) {i["Nome"]}: ")
                i["Nome"]= input(f"Digite um novo nome para o(a) {tipo}(a) {i["Nome"]}: ")
                print(f"Informações de {tipo} atualizadas. Novas informações: {i}")
                guardar_arquivo(lista, arquivo)
            else:
                codigo=verificar_cod_atualizar("pessoa", arquivo, codigo)
                i["Código"] = codigo
                i["CPF"] = input(f"Digite um novo cpf para o(a) {tipo}(a) {i["Nome"]}: ")
                i["Nome"] = input(f"Digite um novo nome para o(a) {tipo}(a) {i["Nome"]}: ")
                print(f"Informações de {tipo} atualizadas. Novas informações: {i}")
                guardar_arquivo(lista, arquivo)



        elif i["Código"] == paraatt and tipo == "disciplina":
            while True:
                try:
                    codigo=int(input(f"Digite o novo código do(a) {tipo}(a) {i["Nome"]} (Código atual:{i["Código"]}): "))
                    break
                except:
                    print("Você digitou um valor inválido, códigos só aceitam números.")
            if codigo == paraatt:
                i["Código"]=codigo
                i["Nome"]= input(f"Digite um novo nome para o(a) {tipo}(a) {i["Nome"]}: ")
                print(f"Informações de {tipo} atualizadas. Novas informações: {i}")
                guardar_arquivo(lista, arquivo)
            else:
                codigo=verificar_cod_atualizar("disciplina", arquivo, codigo)
                i["Código"] = codigo
                i["Nome"] = input(f"Digite um novo nome para o(a) {tipo}(a) {i["Nome"]}: ")
                print(f"Informações de {tipo} atualizadas. Novas informações: {i}")
                guardar_arquivo(lista, arquivo)

        elif i["Código"] == paraatt and tipo == "turma":
            while True:
                try:
                    codigo = int(input(f"Digite o novo código do(a) {tipo}(a) {i["Código"]}: "))
                    break
                except:
                    print("Você digitou um valor inválido, códigos só aceitam números.")

            if codigo == paraatt:
                i["Código"]=codigo
                i["Código_prof"]= input(f"Digite um novo código para o(a) professor(a) da turma {i["Código"]}: ")
                i["Código_disc"] = input(f"Digite um novo código para o(a) disciplina(a) da turma {i["Código"]}: ")
                print(f"Informações de {tipo} atualizadas. Novas informações: {i}")
                guardar_arquivo(lista, arquivo)
            else:
                codigo=verificar_cod_atualizar("turma", arquivo, codigo)
                i["Código"] = codigo
                i["Código_prof"] = input(f"Digite um novo código para o(a) professor(a) da turma {i["Código"]}: ")
                i["Código_disc"] = input(f"Digite um novo código para o(a) disciplina(a) da turma {i["Código"]}: ")
                print(f"Informações de {tipo} atualizadas. Novas informações: {i}")
                guardar_arquivo(lista, arquivo)

        elif i["Código"] == paraatt and tipo == "matricula":
            while True:
                try:
                    codigo = int(input(f"Digite o novo código do(a) {tipo}(a) {i["Código"]}: "))
                    break
                except:
                    print("Você digitou um valor inválido, códigos só aceitam números.")

            if codigo == paraatt:
                i["Código"]=codigo
                i["Código_turma"]= input(f"Digite um novo código para o(a) turma {i["Código_turma"]}: ")
                i["Código_aluno"] = input(f"Digite um novo código para o(a) aluno {i["Código_aluno"]}: ")
                print(f"Informações de {tipo} atualizadas. Novas informações: {i}")
                guardar_arquivo(lista, arquivo)
            else:
                codigo=verificar_cod_atualizar("matricula", arquivo, codigo)
                i["Código"] = codigo
                i["Código_turma"] = input(f"Digite um novo código para o(a) turma {i["Código_turma"]}: ")
                i["Código_aluno"] = input(f"Digite um novo código para o(a) aluno {i["Código_aluno"]}: ")
                print(f"Informações de {tipo} atualizadas. Novas informações: {i}")
                guardar_arquivo(lista, arquivo)




def excluir(arquivo, tipo):
    print("Você selecionou (4) Excluir.")
    lista = ler_arquivo(arquivo)
    if len(lista) >= 1:
        paraexc = int(input(f"Qual é o código do(a) {tipo} que deseja  excluir? "))
        codparamostrar=""
        auxpex = None
        for i in lista:
            if i["Código"] == paraexc:
                auxpex = i
                codparamostrar=auxpex["Código"]
                break #armazenar variável para excluir e o código
        if auxpex is None:
            print(f"Não foi encontrado nenhum(a) {tipo} com este código. ")

        else:
            while True:
                simnao=input(f"Tem certeza que deseja excluir o(a) {tipo}(a) do código {codparamostrar}? (s/n)")
                if simnao == "s": #verificar se o usuário tem certeza
                    print(f"O {tipo}(a) do código {codparamostrar} foi removido(a)")
                    lista.remove(auxpex)
                    guardar_arquivo(lista, arquivo)
                    break
                elif simnao == "n":
                    print("Operação cancelada.")
                    break
                else:
                    print("Escolha inválida.")
                    continue


    else:
        print(f"Ainda não existem {tipo}s cadastrados. ")

def guardar_arquivo(lista, nomearq):
    with open (nomearq, "w", encoding="utf-8") as f:
        json.dump(lista, f, ensure_ascii=False)

def ler_arquivo(nomearq):
    try:
        with open (nomearq, "r", encoding="utf-8") as f:
            lista=json.load(f)
        return lista
    except:
        return []



#código do sistema

while True:
    escolha1=escolha_menu_princ()
    if escolha1:
        menu_operacoes(escolha1)
    else:
        break


print("Finalizando aplicativo...") #Finalizar programa