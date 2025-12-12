from app.signal.analyzer import Analyzer
from app.modulo.analizador.analizador import Luisa
from app.puertos import Puertos
from app.modulo.graficador.graficador import GraficadorFFT

puertos = Puertos()
raspberry = Analyzer()

# Mostrar puertos disponibles
puertos_disponibles = puertos.puertos_disponibles()
print("Puertos disponibles:", puertos_disponibles)

muestras = raspberry.leer_valores()

ff = Luisa(muestras)
graficos = GraficadorFFT(muestras)
graficos.graficar()
complejos = ff.fft()