from serial import Serial

class Analyzer: 
    def __init__(self,baudrate: int = 115200, port: str = "COM3"):
        self.bautrate = baudrate
        self.port = port
        self.ser = Serial(self.port, self.bautrate, timeout=1)

    def leer_linea(self) -> str:
        raw = self.ser.readline()
        return raw.decode("utf-8").strip()
    
    def leer_valores(self) -> list[float]:
        linea = self.leer_linea()
        if linea.startswith("[") and linea.endswith("]"):
            valores = linea[1:-1].split(",")
            response = [float(v.strip()) for v in valores]
            return response
        return []