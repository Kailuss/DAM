---
tags: [DAM, DI]
cssclasses: [dam-di, table-compact-clean]
banner: "![[di.jpg]]"
banner_y: 0.72
---

# Resumen: TEMA 7. Distribución de aplicaciones

```audio-player
[[Lecturas/Lectura_Tema_07.mp3]]
```

## 1. Definición y composición de una distribución  
Una **distribución de software** incluye programas compilados, aplicaciones y un sistema operativo, común en distribuciones Linux como Debian o Ubuntu. Las licencias como **GPL** permiten libre distribución y modificación. Las distribuciones pueden ser **oficiales** o de **terceros**, y pueden ser binarias (ej. .exe, .msi).  
### 1.1. **Sistema de gestión de paquetes  **
Automatiza instalación, actualización y eliminación de software. Ejemplos:  
- Ubuntu: Centro de Software.  
- Synaptic: Gestor de paquetes gráfico.  
Los paquetes contienen:  
- Nombre, versión, descripción.  
- Dependencias y suma de verificación.  
## 2. Instaladores  
Programas que automatizan la instalación, copiando archivos, registrando la aplicación y creando accesos directos. Ejemplos:  
- **Windows.** InstallShield, NSIS.  
- **Multiplataforma.** InstallAnywhere, IzPack.  
### 2.1. **Pasos en la instalación  **
1. Verificación de compatibilidad.  
2. Creación de directorios.  
3. Copia y descompresión de archivos.  
4. Configuración y registro.  
### 2.2. **Asistentes de instalación  **
Guian al usuario con formularios para personalizar:  
- Ruta de instalación.  
- Componentes opcionales.  
- Aceptación de licencias.  
## 3. Paquetes autoinstalables  
Empaquetan la aplicación en un solo archivo:  
- **Windows.** .exe.  
- **Ubuntu.** .deb.  
- **Red Hat.** .rpm.  
Funcionamiento:  
- Descomprimen archivos.  
- Crean directorios.  
- Modifican el registro (Windows).  
## 4. Herramientas para crear paquetes  
- **Windows.** NSIS, Inno Setup.  
- **Linux.** dpkg (.deb), rpm (.rpm).  
### 4.1. **Repositorios  **
Servidores centralizados de paquetes. Ejemplo en Ubuntu:  
```bash
sudo apt update
sudo apt install nombre-paquete
```
## 5. Personalización de la instalación  
- **Logotipos.** Usando `AddBrandingImage` en NSIS:  
  ```nsis
  AddBrandingImage top 100 10
  ```  
- **Fondos y botones.** Coherentes con el diseño.  
- **Idioma.** Soporte para múltiples idiomas.  
## 6. Generación de paquetes de instalación  
### 6.1. **Entorno de desarrollo (Java)  **
- Crear archivo JAR con clase principal en `MANIFEST.MF`.  
- Ejecutar con:  
  ```bash
  java -jar aplicacion.jar
  ```  
### 6.2. **Herramientas externas (NSIS)  **
Ejemplo de script NSIS:  
```nsis
Name "Mi Aplicación"
OutFile "Instalador.exe"
InstallDir "$PROGRAMFILES\MiApp"
Section "Instalar"
  SetOutPath $INSTDIR
  File "app.jar"
  CreateShortcut "$DESKTOP\MiApp.lnk" "$INSTDIR\app.jar"
SectionEnd
```  
### 6.3. **Modo desatendido  **
Comandos para instalación silenciosa:  
- **NSIS.** `Instalador.exe /S`.  
- **MSI.** `msiexec /qn /i aplicacion.msi`.  
## 7. Parámetros de la instalación  
- Selección de idioma.  
- Ruta de instalación.  
- Componentes opcionales.  
- Creación de accesos directos.  
## 8. Interacción con el usuario  
Flujo típico en GUI:  
1. Selección de idioma.  
2. Aceptación de licencia.  
3. Elección de componentes.  
4. Progreso de instalación.  
## 9. Ficheros firmados digitalmente  
### 9.1. **Firma digital en JAR  **
Proceso con `jarsigner`:  
```bash
jarsigner -keystore miKeystore -storepass clave app.jar alias
```  
Verificación:  
```bash
jarsigner -verify app.jar
```  
Archivos generados:  
- `MANIFEST.MF`: Hashes de archivos.  
- `.SF`: Resumen del manifiesto.  
- `.DSA`: Firma digital.  
## 10. Instalación desde servidor  
### 10.1. **Uso de `apturl` en Ubuntu  **
Enlace para instalar múltiples paquetes:  
```html
<a href="apt:pidgin,pidgin-plugin-pack">Instalar Pidgin</a>
```  
## 11. Descarga y ejecución desde servidores web  
- **Ejecutables.** .exe (Windows), .sh (Linux).  
- **Paquetes Linux.**  
  ```bash
  sudo dpkg -i paquete.deb
  ```  
