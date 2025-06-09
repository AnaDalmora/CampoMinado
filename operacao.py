class Operacao:
    def __init__(self, grafico):
        self.grafico = grafico

    def on_click(self, linha, coluna):
        posicao = (linha, coluna)
        x = coluna * 16
        y = linha * 16 + 32

        if posicao in self.grafico.campo:
            if self.grafico.campo[posicao] == 1:
                self.grafico.canvas.create_image(x, y, anchor="nw", image=self.grafico.mine_img)
            else:
                self.grafico.canvas.create_image(x, y, anchor="nw", image=self.grafico.nomine_img)

            # Armazena referência para não perder imagem
            self.grafico.canvas.image = self.grafico.mine_img
            self.grafico.canvas.image2 = self.grafico.nomine_img