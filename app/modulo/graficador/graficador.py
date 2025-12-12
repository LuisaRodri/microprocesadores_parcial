import matplotlib.pyplot as plt
from app.modulo.analizador.analizador import Luisa

class GraficadorFFT:
    def __init__(self, señal, fs=1.0):
        self.tf = Luisa(señal)
        self.tf.fft()
        self.magnitudes = self.tf.obtener_magnitudes()
        self.fases = self.tf.obtener_fases()
        self.fs = fs
        self.N = len(señal)

    def graficar(self):
        plt.subplot(2, 1, 1)
        plt.title("Magnitud de la Transformada")
        plt.plot(self.magnitudes, marker="o", color="blue")

        plt.subplot(2, 1, 2)
        plt.title("Fase de la Transformada")
        plt.plot(self.fases, marker="o", color="orange")

        plt.tight_layout()
        plt.show()
