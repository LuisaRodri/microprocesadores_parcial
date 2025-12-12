import math
import cmath

class Luisa:
    def __init__(self, señal: list[float]):
        """
        Inicializa la clase con una señal (lista de números).
        """
        self.señal = señal
        self.N = len(señal)
        self.transformada: list[complex] | None = None

    def fft(self) -> list[complex]:
        """
        Calcula la Transformada Rápida de Fourier (FFT) usando el algoritmo recursivo Cooley–Tukey.
        Requiere que la longitud de la señal sea potencia de 2.
        """
        def _fft(x: list[complex]) -> list[complex]:
            n = len(x)
            if n <= 1:
                return x
            even = _fft(x[0::2])
            odd = _fft(x[1::2])
            T = [cmath.exp(-2j * math.pi * k / n) * odd[k] for k in range(n // 2)]
            return [even[k] + T[k] for k in range(n // 2)] + \
                   [even[k] - T[k] for k in range(n // 2)]

        # Convertimos la señal a complejos
        señal_c = [complex(x, 0) for x in self.señal]
        X = _fft(señal_c)
        self.transformada = X
        return X

    def abs_complejo_formula(z: complex) -> complex:
        """
        Calcula el valor absoluto de un número complejo y lo devuelve como complejo.
        """
        if isinstance(z, complex):
            a = z.real
            b = z.imag
            magnitud: float = math.sqrt(a*a + b*b)
            return complex(magnitud, 0)
        try:
            return complex(abs(z), 0)
        except Exception as e:
            raise TypeError(f"No se pudo calcular |z| para tipo {type(z)}: {e}")

    def fase(z: complex) -> float:
        """
        Calcula la fase (argumento) de un número complejo en radianes.
        """
        return cmath.phase(z)
    
    
    def obtener_magnitudes(self) -> list[float]:
        """
        Devuelve la lista de magnitudes de la transformada.
        """
        if self.transformada is None:
            raise ValueError("Primero debes calcular la FFT.")
        return [abs(z) for z in self.transformada]

    def obtener_fases(self) -> list[float]:
        """
        Devuelve la lista de fases (argumentos en radianes) de la transformada.
        """
        if self.transformada is None:
            raise ValueError("Primero debes calcular la FFT.")
        return [cmath.phase(z) for z in self.transformada]


#  Bloque de prueba: se ejecuta solo si corres el archivo directamente
if __name__ == "__main__":
    # Señal de ejemplo
    señal = [0, 1, 0, -1]
    tf = Luisa(señal)

    # Ejecutar FFT
    resultado = tf.fft()
    print("Resultado FFT:", resultado)

    # Magnitudes y fases
    print("Magnitudes:", tf.obtener_magnitudes())
    print("Fases:", tf.obtener_fases())

    # Ejemplo de uso de métodos estáticos
    print("Fase de (1+1j):", Luisa.fase(complex(1, 1)))
    print("Magnitud de (3+4j):", Luisa.abs_complejo_formula(complex(3, 4)))
