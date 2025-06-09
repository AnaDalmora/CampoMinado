import tkinter as tk
from PIL import Image, ImageTk
from Mina import Mina
from operacao import Operacao
from tempo import Tempo  # tempo com auto atualização

class Interface:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Campo Minado")
        self.root.configure(bg="lightgray")
        self.root.geometry("200x300")  # tamanho da janela
        self.root.resizable(False, False)
        # Label de tempo
        self.tempo_label = tk.Label(self.root, text="Tempo: 0s", bg="lightgray",font=("Arial", 16), width=15, height=2)
        self.tempo_label.place(relx=0.5, y=5, anchor="n")

        # Canvas
        self.canvas = tk.Canvas(self.root, width=160, height=208, bg="lightgray", highlightthickness=0)
        self.canvas.place(relx=0.5, rely=0.5, anchor="center")

        # Tempo
        self.tempo = Tempo(self.root, self.tempo_label)
        self.tempo.iniciar()

        # Imagens
        self.default_img = tk.PhotoImage(file="assets/default.png")
        self.mine_img = tk.PhotoImage(file="assets/mine.png")
        self.nomine_img = tk.PhotoImage(file="assets/nomine.png")

        # Operação e campo
        self.operacao = Operacao(self)
        self.campo = {}
        self.criar_campo()

        self.root.mainloop()

    def criar_campo(self):
        for i in range(13):  # linhas
            for j in range(10):  # colunas
                x = j * 16
                y = i * 16 + 32
                image_id = self.canvas.create_image(x, y, anchor="nw", image=self.default_img)
                self.campo[(i, j)] = Mina().tem_mina
                self.canvas.tag_bind(image_id, "<Button-1>", lambda e, linha=i, coluna=j: self.operacao.on_click(linha, coluna))

        self.canvas.image = self.default_img
