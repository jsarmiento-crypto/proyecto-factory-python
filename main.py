from notificaciones.factory import NotificacionFactory


def main():
  print("--- Demostración del Patrón Factory Method ---")

  canales = ["email", "sms", "push", "whatsapp"]
  destinatario = "usuario_ejemplo@ecotec.edu.ec"
  mensaje = "Tu pedido #1042 ha sido procesado con éxito."

  for canal in canales:
    notificador = NotificacionFactory.crear_notificacion(canal)
    notificador.enviar(mensaje, destinatario)


if __name__ == "__main__":
  main()