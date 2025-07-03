import random
import tkinter as tk

class Operacao:
    def __init__(self, grafico):
        self.grafico = grafico
        self.pontos_aleatorio = 0
        self.pontos_linha = 0
        self.pontos_coluna = 0

        self.modo_jogo = "Linha"
        self.linha_atual = 0
        self.coluna_atual = 0
        self.jogo_encerrado = False
        self.ciclos = 1
    def jogadas(self):
        self.linha_atual = 0
        self.coluna_atual = 0

        if self.modo_jogo == "Linha":
            self.jogada_linha()
        elif self.modo_jogo == "Coluna":
            self.jogada_coluna()
        elif self.modo_jogo == "Aleatorio":
            self.jogada_aleatoria()


    def jogada_linha(self):
        if self.jogo_encerrado:
            self.finalizar_modo()
            return

        if self.linha_atual < self.grafico.linhas:
            if self.coluna_atual < self.grafico.colunas:
                self.on_click(self.linha_atual, self.coluna_atual)
                self.coluna_atual += 1
            else:
                self.coluna_atual = 0
                self.linha_atual += 1

            self.grafico.canvas.after(300, self.jogada_linha)
        else:
            self.finalizar_modo()

    def jogada_coluna(self):
        if self.jogo_encerrado:
            self.finalizar_modo()
            return

        if self.coluna_atual < self.grafico.colunas:
            if self.linha_atual < self.grafico.linhas:
                self.on_click(self.linha_atual, self.coluna_atual)
                self.linha_atual += 1
            else:
                self.linha_atual = 0
                self.coluna_atual += 1

            self.grafico.canvas.after(300, self.jogada_coluna)
        else:
            self.finalizar_modo()

    def jogada_aleatoria(self):
        if self.jogo_encerrado:
            self.finalizar_modo()
            return

        posicoes_fechadas = [pos for pos, status in self.grafico.campo.items() if status != "Opened"]
        if not posicoes_fechadas:
            self.jogo_encerrado = True
            self.finalizar_modo()
            return

        i, j = random.choice(posicoes_fechadas)
        self.on_click(i, j)

        self.grafico.canvas.after(300, self.jogada_aleatoria)

    def on_click(self, linha, coluna):
        posicao = (linha, coluna)
        x = coluna * 16
        y = linha * 16 

        if self.grafico.campo[posicao] == 1:
            self.grafico.canvas.create_image(x, y, anchor="nw", image=self.grafico.mine_img, tags="revelado")
            self.grafico.campo[posicao] = "Mine"
            self.jogo_encerrado = True
        elif self.grafico.campo[posicao] == 0:
            self.grafico.canvas.create_image(x, y, anchor="nw", image=self.grafico.nomine_img, tags="revelado")
            self.grafico.campo[posicao] = "Opened"
            self.atualiza_pontos()

    def finalizar_modo(self):
        self.grafico.canvas.after(1000, self.resetar_e_continuar)

    def resetar_e_continuar(self):
        self.resetar_campo()
        self.jogo_encerrado = False
        self.linha_atual = 0
        self.coluna_atual = 0

        if self.modo_jogo == "Linha":
            self.modo_jogo = "Coluna"
        elif self.modo_jogo == "Coluna":
            self.modo_jogo = "Aleatorio"
        elif self.modo_jogo == "Aleatorio":
            if self.ciclos >=10:
                self.grafico.ciclo_jogada_label.config(text="Fim de jogo!")
                return
            else:
                self.ciclos +=1
                self.modo_jogo = "Linha"
                self.grafico.ciclo_jogada_label.config(text=f"Ciclos: {self.ciclos}")
                self.grafico.criar_campo()

        self.grafico.canvas.after(500, self.jogadas)

    def resetar_campo(self):
        revelados = self.grafico.canvas.find_withtag("revelado")
        for item in revelados:
            x, y = self.grafico.canvas.coords(item)
            self.grafico.canvas.delete(item)
            self.grafico.canvas.create_image(x, y, anchor="nw", image=self.grafico.default_img)

        for i in range(self.grafico.linhas):
            for j in range(self.grafico.colunas):
                if self.grafico.campo[(i, j)] == "Opened":
                    self.grafico.campo[(i, j)] = 0
                elif self.grafico.campo[(i, j)] == "Mine":
                    self.grafico.campo[(i, j)] = 1

    def atualiza_pontos(self):
        if self.modo_jogo == "Aleatorio":
            self.pontos_aleatorio +=10
            self.grafico.pontos_jogador_aleatorio_label.config(text=f"Aleatorio: {int(self.pontos_aleatorio)}")
        elif self.modo_jogo == "Coluna":
            self.pontos_coluna +=10
            self.grafico.pontos_jogador_coluna_label.config(text=f"Coluna: {int(self.pontos_coluna)}")
        else:
            self.pontos_linha +=10
            self.grafico.pontos_jogador_linha_label.config(text=f"Linha: {int(self.pontos_linha)}")
