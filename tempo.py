from datetime import datetime
import tkinter as tk

class Tempo:
    def __init__(self, root: tk.Tk, label: tk.Label):
        self.__start = None
        self.__finish = None
        self.__root = root
        self.__label = label
        self.__job_id = None

    def iniciar(self):
        self.__start = datetime.now()
        self.__finish = None
        self.__atualizar_label()

    def parar(self):
        self.__finish = datetime.now()
        if self.__job_id:
            self.__root.after_cancel(self.__job_id)

    def tempo_decorrido(self) -> float:
        if self.__start is None:
            return 0.0
        fim = self.__finish or datetime.now()
        return (fim - self.__start).total_seconds()

    def __atualizar_label(self):
        segundos = int(self.tempo_decorrido())
        self.__label.config(text=f"Tempo: {segundos}s")
        self.__job_id = self.__root.after(1000, self.__atualizar_label)
