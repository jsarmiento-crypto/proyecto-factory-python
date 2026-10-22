from abc import ABC, abstractmethod

class NotificacionBase(ABC):
    @abstractmethod
    def enviar(self, mensaje: str, usuario: str) -> None:
        pass