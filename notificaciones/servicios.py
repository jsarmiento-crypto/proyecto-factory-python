class NotificacionWhatsApp(NotificacionBase):

  def enviar(self, mensaje: str, usuario: str) -> None:
    print(f"[WHATSAPP] Enviando a {usuario}: {mensaje}")