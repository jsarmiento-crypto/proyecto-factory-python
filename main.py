from notificaciones.factory import NotificacionFactory


def main():
  print('--- Demostracion del Patron Factory ---')

  canales = ['email', 'sms', 'push', 'whatsapp']
  usuario_destino = 'usuario_ejemplo@ecotec.edu.ec'
  mensaje_prueba = 'Tu pedido #1042 ha sido procesado con exito.'

  for canal in canales:
    notificador = NotificacionFactory.crear_notificacion(canal)
    notificador.enviar(mensaje_prueba, usuario_destino)


if __name__ == '__main__':
  main()