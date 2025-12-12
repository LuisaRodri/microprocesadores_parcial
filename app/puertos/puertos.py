import serial
import serial.tools.list_ports

class Puertos:
    def __init__(self):
        self.lista = serial.tools.list_ports

    def puertos_disponibles(self) -> list:
        puertos = self.lista.comports()
        return puertos
    
    