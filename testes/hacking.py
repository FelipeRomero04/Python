import tkinter as tk

def inserir_inicio():
    entrada.insert(0, "INÍCIO ")

def inserir_meio():
    entrada.insert(5, "MEIO ")

def inserir_fim():
    entrada.insert(tk.END, " FIM")

janela = tk.Tk()
janela.title("Teste de Índices no Entry")

# Entry já começa com conteúdo
entrada = tk.Entry(janela, width=40)
entrada.insert(0, "Texto original aqui.")
entrada.pack(pady=10)

# Botões para testar inserções
tk.Button(janela, text="Inserir no início", command=inserir_inicio).pack()
tk.Button(janela, text="Inserir no meio (posição 5)", command=inserir_meio).pack()
tk.Button(janela, text="Inserir no fim", command=inserir_fim).pack()

janela.mainloop()

    