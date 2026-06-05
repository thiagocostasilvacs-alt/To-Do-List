def carregar_tarefas():
    tarefas = []

    try:
        with open("tarefas.txt", "r") as arquivo:
            for linha in arquivo:
                tarefas.append(linha.strip())

    except FileNotFoundError:
        pass

    return tarefas

def adicionar_tarefa(tarefas):
    print("\nAdicionar tarefa selecionado\n")

    tarefa = input("Digite a tarefa: ").strip()

    if not tarefa:
        print("\nA tarefa não pode estar vazia.")
        return
    
    tarefas.append(tarefa)
    salvar_tarefas(tarefas)
    print("\nTarefa adicionada!")

    

def listar_tarefas(tarefas):
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
    
    else:
        print("\nListar tarefas selecionado\n")
        print("\n=== SUAS TAREFAS ===\n")
        
        for numero, tarefa in enumerate(tarefas, start=1):
            print(f"{numero}. {tarefa}")

def remover_tarefa(tarefas):
    if not tarefas:
        print("\nNenhuma tarefa cadastrada")
    
    else:
        try:
            indice = int(input("\nDigite o número da tarefa que deseja remover: "))
            indice -=1

            if 0 <= indice < len(tarefas):
                tarefas.pop(indice)
                salvar_tarefas(tarefas)
                print("\nTarefa removida com sucesso!")
            
            else:
                print("\nTarefa inexistente.")
        
        except ValueError:
            print("\nDigite apenas números.")

def salvar_tarefas(tarefas):
    with open("tarefas.txt", "w") as arquivo:
        for tarefa in tarefas:
            arquivo.write(tarefa + "\n")

def main():
    tarefas = carregar_tarefas()

    while True:
        print("\n=== TO-DO LIST ===")
        print("\n1 - Adicionar tarefa")
        print("2 - Listar tarefas")
        print("3 - Remover tarefa")
        print("4 - Sair")


        opcao = input("\nEscolha: ")

        if opcao == "1":
            adicionar_tarefa(tarefas)

        elif opcao == "2":
            listar_tarefas(tarefas)
        
        elif opcao =="3":
            remover_tarefa(tarefas)

        elif opcao == "4":
            print("\nEncerrando programa...")
            break

        else:
            print("\nOpção inválida!")

if __name__ == "__main__":
    main()