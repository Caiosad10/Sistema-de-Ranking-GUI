import tkinter as tk
from tkinter import FLAT, ttk
from tkinter.messagebox import showinfo

#Variaveis para armazenar os dados

position = ["1º", "2º", "3º"]

#Dicionario para armazenar os dados com as respectivas posições
posicaoAluno = {"1º": None, "2º": None, "3º": None}

#Lista para armazenar alunos
alunos = []

#Lista para armazenar as notas
notas = []

#Lista para armazenar as notas do maior para o menor
notasMaiorMenor = []

#Indice para a função de adicionar notas
iNotas = 0

#Criando a janela
janela = tk.Tk()
janela.title("Sistema de nota")
janela.geometry("800x600")
janela.resizable(True, True)

#Configurando por tabela
janela.columnconfigure(0, weight=2)
janela.columnconfigure(1, weight=1)
janela.columnconfigure(2, weight=3)

#Titulo informando das escolhas
titulo = tk.Label(janela, text="Ações disponiveis:").grid(column=1, row=0, sticky=tk.N, padx=5, pady=5)

#Funções para botões

#Função para adicionar alunos
def add_alunos():
  #Frame
  frame_add_alunos = ttk.Frame(janela, borderwidth= 2, relief= "groove")
  frame_add_alunos.columnconfigure(0, weight=1)
  frame_add_alunos.columnconfigure(1, weight=2)
  frame_add_alunos.columnconfigure(2, weight=1)
  frame_add_alunos.grid(column=2, row=1, sticky=tk.NSEW, padx=10, pady=10)

  #widgets
  title_add_alunos = ttk.Label(frame_add_alunos, text="Adicionar alunos:", font=("Arial", 10))
  title_add_alunos.grid(column=1, row=0, sticky=tk.W, pady= 8)
  i = 1
  add_nomes = ttk.Label(frame_add_alunos, text=f"Digite o nome do aluno:")
  add_nomes.grid(column=0, row=1, sticky=tk.W, padx= 2)
  nome_input = tk.Entry(frame_add_alunos, width=30)
  nome_input.grid(column=1, row=1, sticky=tk.W)

  #Função para adicionar os nomes na lista
  def add():
    nonlocal i  # Permite modificar a variável 'i' dentro da função interna
    nome = nome_input.get()
    alunos.append(nome)
    print(f"Aluno '{nome}' adicionado à lista!")
    i +=1
    nome_input.delete(0, tk.END) #Limpa o input
    add_nomes.config(text=f"Digite o nome do {i}º aluno:") #reescreve o texto para atualizar

  #Função para aparecer uma mensagem informando a quantidade de alunos adicionados 
  def informacao():
    showinfo(
        title='Informação',
        message=f'Adicionado {len(alunos)} alunos!'
    )
    frame_add_alunos.destroy()

  #Botão adicionar
  button_add = ttk.Button(frame_add_alunos, text="Adicionar", command=add)
  button_add.grid(column=2, row=1)

  #Botão de finalizar
  button_close = ttk.Button(frame_add_alunos, text="Finalizar", command=informacao)
  button_close.grid(column=1, row=2, sticky=tk.W, pady= 8)

#Função para ver alunos
def ver_alunos():
  #Frame
  frame_ver_alunos = ttk.Frame(janela, borderwidth= 2, relief= "groove")
  frame_ver_alunos.columnconfigure(0, weight=3)
  frame_ver_alunos.grid(column=2, row=2, sticky=tk.NSEW, padx=10, pady=10)

  #Widgets
  title_ver_alunos = ttk.Label(frame_ver_alunos, text="Lista de Alunos:", font=("Arial", 10))
  title_ver_alunos.grid(column=0, row=0, pady= 5)
  iRow= 1
  for i, aluno in enumerate(alunos):
    ttk.Label(frame_ver_alunos, text=f'{i + 1}º - {aluno}', font=("Arial", 10)).grid(column=0, row=(i + 1), sticky=tk.N, pady= 5)
    iRow += 1

  #Botão para finalizar
  button_end = ttk.Button(frame_ver_alunos, text="Sair", command=lambda: frame_ver_alunos.destroy())
  button_end.grid(sticky=tk.S)

#Função para mostrar a informação das posições
def posicoes_dispo():
  showinfo(
     title="Posições",
     message="1º Lugar\n2º Lugar\n3º Lugar"
    )

#Função para adicionar notas
def add_notas():
  #Frame
  frame_add_notas = ttk.Frame(janela, borderwidth= 2, relief= "groove")
  frame_add_notas.columnconfigure(0, weight=1)
  frame_add_notas.columnconfigure(1, weight=2)
  frame_add_notas.columnconfigure(2, weight=1)
  frame_add_notas.grid(column=2, row=4, sticky=tk.NSEW, padx=10, pady=10)

  #Widgets
  title_notas = ttk.Label(frame_add_notas, text="Adicionar Notas:")
  title_notas.grid(column=1, row=0, pady=5)
  i = 0
  
  add_notas = ttk.Label(frame_add_notas, text=f"Adicione a note do {alunos[i]}:")
  add_notas.grid(column=0, row=1, sticky=tk.W, pady=5)

  notas_input = tk.Entry(frame_add_notas, width=5)
  notas_input.grid(column=1, row= 1, sticky=tk.W, pady=5)

  #Função para armazenar as notas
  def adicionarNotas():
    nonlocal i
    nota = notas_input.get()
    notas.append(nota)
    print(f"Nota adicionado para o aluno {alunos[i]}")
    i += 1
    notas_input.delete(0, tk.END) #Limpa o input
    add_notas.config(text=f"Adicione a nota do {alunos[i]}:")

  def informacaoNotas():
    for i in range(len(alunos)):
      showinfo(
        title='Informação',  
        message=f'A nota do aluno {alunos[i]} é {notas[i]}!')
    frame_add_notas.destroy()

  #IDEIA - Criar função para alterar notas

  button_add_nota = ttk.Button(frame_add_notas, text="Adicionar nota", command=adicionarNotas)
  button_add_nota.grid(column=2, row=1, pady=5)

  button_close = ttk.Button(frame_add_notas, text="Finalizar", command=informacaoNotas)
  button_close.grid(column=1, row=2, sticky=tk.W, pady= 8)

#Função para determinar o ranking
def determinacao():
  global notasMaiorMenor
  notasMaiorMenor = sorted(notas, reverse=True)
  indicesMaiorMenor = sorted(range(len(notas)), key=lambda k: notas[k], reverse=True)
  for i in range(3):
    posicaoAluno[position[i]] = alunos[indicesMaiorMenor[i]]
    print(f"\n{position[i]} - {alunos[indicesMaiorMenor[i]]}\n")
      
  if all(value is not None for value in posicaoAluno.values()):
    showinfo(
      title= 'Informação',
      message='Ranking determinado!'
    )
  else:
    showinfo(
      title= 'Informação',
      message='Erro ao determinar ranking!'
    )
#Função para ver o ranking determinado
def ver_rank():
  frame_ver_rank = ttk.Frame(janela, borderwidth= 2, relief= "groove")
  frame_ver_rank.columnconfigure(0, weight=3)
  frame_ver_rank.columnconfigure(1, weight=3)
  frame_ver_rank.grid(column=2, row=6, sticky=tk.NSEW, padx=10, pady=10)

  title_ver_rank = ttk.Label(frame_ver_rank, text="Ranking")
  title_ver_rank.grid(column=0, row=0, pady= 8)
  
  for i in range(3):
    print(f"{position[i]} - {posicaoAluno[position[i]]}\t\tNota: {notasMaiorMenor[i]}\n")
    label_ranking = ttk.Label(frame_ver_rank, text=f"{position[i]} - {posicaoAluno[position[i]]}\t\tNota: {notasMaiorMenor[i]}\n")
    label_ranking.grid(column=0, row=i + 1, sticky=tk.N, pady=5)
    

  btn_close = ttk.Button(frame_ver_rank, text="Sair", command=lambda: frame_ver_rank.destroy())
  btn_close.grid(sticky=tk.S, pady=5)

def encerrar():
  showinfo(
     title="Encerrando sistema..",
      message="Encerrando, até mais! :)"
    )
  janela.destroy()
  
#Botões
opc1 = ttk.Button(janela, text="Adicionar alunos", command=add_alunos)
opc1.grid(column=1, row=1, sticky=tk.N, padx= 5, pady=5)

opc2 = ttk.Button(janela, text="Ver Alunos", command=ver_alunos)
opc2.grid(column=1, row=2, sticky=tk.N, padx= 5, pady=5)

opc3 = ttk.Button(janela, text="Posições disponiveis", command=posicoes_dispo)
opc3.grid(column=1, row=3, sticky=tk.N, padx= 5, pady=5)

opc4 = ttk.Button(janela, text="Adicionar notas", command=add_notas)
opc4.grid(column=1, row=4, sticky=tk.N, padx= 5, pady=5)

opc5 = ttk.Button(janela, text="Determinar Ranking", command=determinacao)
opc5.grid(column=1, row=5, sticky=tk.N, padx= 5, pady=5)

opc6 = ttk.Button(janela, text="Ver Ranking", command=ver_rank)
opc6.grid(column=1, row=6, sticky=tk.N, padx= 5, pady=5)

opc7 = ttk.Button(janela, text="Encerrar sistema", command=encerrar)
opc6.grid(column=1, row=7, sticky=tk.N, padx= 5, pady=5)

#Configuração do estilo dos botões
style = ttk.Style()
style.configure("TButton", relief=FLAT)



janela.mainloop()