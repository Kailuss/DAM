---
tags:
  - Focus
  - PSP
  - Tarea
obsidianUIMode: preview
banner: "![[psp.jpg]]"
banner_y: 0.32
---

# Tarea PSP03
## 1 Introducción

En esta práctica, se desarrollará un sistema de chat multiusuario que permita a múltiples clientes conectarse a un servidor centralizado para intercambiar mensajes en tiempo real. El objetivo es poner en práctica los conceptos de comunicación en red utilizando sockets TCP para gestionar conexiones cliente-servidor y datagramas UDP para enviar notificaciones rápidas.

## 2 Requisitos funcionales

- El servidor debe poder gestionar conexiones de múltiples clientes de forma concurrente utilizando sockets TCP.
- Cada cliente podrá enviar mensajes al servidor, y este reenviará el mensaje a todos los demás clientes conectados (funcionalidad de “broadcast”).
- Se debe mantener un registro de los clientes conectados (direcciones IP y puertos).
- Cada cliente podrá:
	- Conectarse al servidor.
	- Enviar mensajes que el servidor retransmitirá al resto de los clientes.
	- Recibir mensajes enviados por los demás clientes a través del servidor.
	- Cuando un nuevo cliente se conecte al servidor, este enviará una notificación UDP a todos los clientes conectados para indicarles que un nuevo usuario ha entrado al chat.
	- De igual forma, cuando un cliente se desconecte, se enviará una notificación UDP al resto.

## 3 Requisitos no funcionales

- Utilizar una interfaz de usuario sencilla (puede ser por consola) tanto para el cliente como para el servidor.
- Garantizar que el servidor no colapse cuando múltiples clientes se conecten o desconecten al mismo tiempo.

## 4 Detalles técnicos

**Servidor:**

- Debe usar hilos o ejecutores para gestionar múltiples conexiones de clientes.
- Utilizar sockets TCP (ServerSocket y Socket) para establecer conexiones y enviar mensajes.
- Utilizar datagramas UDP (DatagramSocket y DatagramPacket) para enviar notificaciones.

**Clientes:**

- Cada cliente debe tener:
	- Un hilo para enviar mensajes al servidor.
	- Un hilo para recibir mensajes del servidor.
	- Capacidad de recibir notificaciones vía UDP.

**Protocolo de comunicación:**

- Los mensajes se enviarán en formato de texto, con el siguiente formato:  
	`[NombreUsuario]: [Mensaje]`.
- Las notificaciones UDP tendrán el formato:  
	`NOTIFICACIÓN: [NombreUsuario] se ha unido/desconectado del chat`.

## 5 Tareas a realizar

1. **Implementar el servidor:**
	
	- Crear un servidor que escuche conexiones TCP en un puerto específico.
	- Gestionar múltiples clientes mediante hilos.
	- Reenviar mensajes a todos los clientes conectados.
	- Enviar notificaciones UDP a los clientes conectados cuando haya cambios.
2. **Implementar el cliente:**
	
	- Desarrollar una aplicación que permita al usuario introducir su nombre y conectarse al servidor.
	- Implementar el envío y recepción de mensajes vía TCP.
	- Implementar la recepción de notificaciones UDP.
3. **Probar el sistema:**
	
	- Simular múltiples clientes conectados al servidor.
	- Verificar el correcto funcionamiento del chat y las notificaciones UDP.

## 6 Extensión opcional

- Añadir la posibilidad de que los usuarios envíen mensajes privados a otros usuarios.
- Implementar un sistema de logs en el servidor (un único log) para registrar todas las interacciones (conexiones, desconexiones y mensajes enviados).
