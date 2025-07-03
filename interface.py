import tkinter as tk
from Mina import Mina
from operacao import Operacao

class Interface:

    def __init__(self):
        #tamanho do campo
        self.colunas = 10
        self.linhas = 13

        self.root = tk.Tk()
        self.root.title("Campo Minado")
        self.root.configure(bg="lightgray")
        self.root.geometry("275x400") 
        self.root.resizable(False, False)

        self.operacao = Operacao(self) # Cria uma instância de operação

        # label dos pontos dos jogadores
        self.pontos_label = tk.Label(self.root, text="Pontos", bg="lightgray", font=("Arial", 12), width=15, height=2)
        self.pontos_label.place(relx=0.5, y=5, anchor="n")

        self.pontos_jogador_aleatorio_label = tk.Label(self.root, text="Aleatorio: 0", bg="lightgray", font=("Arial", 8), width=12, height=2)
        self.pontos_jogador_coluna_label = tk.Label(self.root, text="Coluna: 0", bg="lightgray", font=("Arial", 8), width=12, height=2)
        self.pontos_jogador_linha_label = tk.Label(self.root, text="Linha: 0", bg="lightgray", font=("Arial", 8), width=12, height=2)

        self.pontos_jogador_aleatorio_label.place(x=10, y=35, anchor="nw")
        self.pontos_jogador_coluna_label.place(x=105, y=35, anchor="nw")
        self.pontos_jogador_linha_label.place(x=200, y=35, anchor="nw")

        # Campo de jogo
        self.canvas = tk.Canvas(self.root, width=160, height=208, bg="lightgray", highlightthickness=0)
        self.canvas.place(relx=0.5, rely=0, y=75, anchor="n")
        #Ciclo de jogadas
        self.ciclo_jogada_label = tk.Label(self.root, text=f"Ciclo: {self.operacao.ciclos} ", bg="lightgray", font=("Arial", 12), width=15, height=2)
        self.ciclo_jogada_label.place(x=10, y=300, anchor="nw")
        # Imagens
        self.default_img = tk.PhotoImage(file="assets/default.png")
        self.mine_img = tk.PhotoImage(file="assets/mine.png")
        self.nomine_img = tk.PhotoImage(file="assets/nomine.png")

        # cria o Campo 
        self.campo = {}
        self.criar_campo()
        self.operacao.jogadas()

        self.root.mainloop()

    def criar_campo(self):
        for i in range(self.linhas):  
            for j in range(self.colunas):  
                x = j * 16
                y = i * 16
                self.canvas.create_image(x, y, anchor="nw", image=self.default_img)
                self.campo[(i, j)] = Mina().tem_mina

        self.canvas.image = self.default_img  


                

