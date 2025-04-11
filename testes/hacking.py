import tkinter as tk

janela = tk.Tk()
janela.title("Label vs Canvas.create_text")
janela.geometry("400x200")

# Criar o canvas
canvas = tk.Canvas(janela, bg="black", width=400, height=200)
canvas.pack()

# Fundo visual (uma "caixa") só pra você ver o espaço
canvas.create_rectangle(50, 40, 350, 160, fill="#253034")

# --------- 1. Usando Label sobre o Canvas (com place) ---------
label = tk.Label(janela,
                 text="Texto com Label",
                 font=("Arial", 14),
                 fg="black",
                 bg="white",
                 padx=0,
                 pady=0,
                 borderwidth=0,
                 highlightthickness=0)
label.place(x=60, y=60)  # Posição sobre a área do canvas

# --------- 2. Usando create_text diretamente ---------
canvas.create_text(60, 120, 
                   text="Texto com create_text", 
                   font=("Arial", 14), 
                   fill="white", 
                   anchor="nw")  # "nw" = canto superior esquerdo como referência

tk.mainloop()