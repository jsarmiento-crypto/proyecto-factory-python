from notificaciones.base import NotificacionBase


class NotificacionEmail(NotificacionBase):

  def enviar(self, mensaje: str, usuario: str) -> None:
    print(f"[EMAIL] Enviando a {usuario}: {mensaje}")


class NotificacionSMS(NotificacionBase):

  def enviar(self, mensaje: str, usuario: str) -> None:
    print(f"[SMS] Enviando a {usuario}: {mensaje}")


class NotificacionPush(NotificacionBase):

  def enviar(self, mensaje: str, usuario: str) -> None:
    print(f"[PUSH] Enviando a {usuario}: {mensaje}")