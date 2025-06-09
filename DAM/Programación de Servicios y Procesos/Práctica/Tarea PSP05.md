---
tags: [DAM, PSP]
cssclasses:
  - dam-psp
  - table-compact-clean
banner: "![[psp.jpg]]"
banner_y: 0.25
number headings: off
---

# Tarea **PSP05**
## Enunciado

Crear un programa en Java que permita simular la comunicación SSL mediante un modelo cliente/servidor. El objetivo final es que un cliente pueda enviar datos (palabras) cifradas con AES a un servidor utilizando una clave simétrica compartida entre el cliente y el servidor. Para lograr este objetivo, se debe garantizar que solo el cliente y el servidor puedan tener la clave, lo que implica un proceso y un flujo que se describe a continuación. Finalmente, en todo momento se debe garantizar que los datos enviados no hayan sido modificados durante la comunicación, de tal forma que se cumpla la integridad de los datos. Esto solo es posible utilizando Hash. Para más información o resolución de dudas, podéis escribir en el foro.  

### Comunicación cliente/servidor
1. **Cliente:** Solicita la clave pública al servidor.  
2. **Servidor:** Genera un conjunto de claves (pública y privada) y envía la clave pública al cliente.  
3. **Cliente:** Genera una clave simétrica, genera un hash sobre esta clave simétrica y lo cifra todo utilizando la clave pública recibida del servidor. Finalmente, el cliente envía los datos al servidor.  
4. **Servidor:** Recibe el mensaje cifrado, lo descifra utilizando su clave privada, genera un hash sobre los datos recibidos que hacen referencia a la clave simétrica enviada por el cliente, comprueba que el hash recibido y el hash generado son iguales para garantizar la integridad y, finalmente, guarda la clave compartida en una variable `SecretKey`.  
5. **Cliente:** Captura palabras por teclado escritas por el usuario, genera un hash sobre la palabra, lo cifra todo con la clave compartida y lo envía al servidor.  
6. **Servidor:** Recibe el mensaje cifrado, lo descifra utilizando su clave compartida simétrica, genera un hash sobre los datos recibidos que hacen referencia a la palabra enviada por el cliente, comprueba que el hash recibido y el hash generado son iguales para garantizar la integridad, imprime la palabra por pantalla y envía un acuse de recibo al cliente.  
7. **Opcional:** Implementación de certificados digitales autofirmados. Para aumentar la seguridad y simular el uso de certificados en protocolos como HTTPS, se propone generar y utilizar un certificado digital autofirmado para verificar la identidad del servidor antes de enviar la clave simétrica. Esto añade una capa de autenticidad al proceso, simulando cómo funcionan las conexiones SSL/TLS con certificados en entornos reales.  

### Sugerencias de pasos a seguir
1. **Generación del certificado:**  
   - El servidor genera un certificado autofirmado utilizando Java KeyStore (JKS) o herramientas como `keytool`.  
1. **Compartición del certificado:**  
   - El servidor envía el certificado al cliente en lugar de solo la clave pública.  
1. **Validación del certificato:**  
   - El cliente verifica la validez del certificado antes de utilizar la clave pública que incluye.  
   - Simular posibles ataques de certificados falsos para enseñar qué pasa si la verificación falla.  

**Información adicional:** El acuse de recibo del servidor es un mensaje que dice: “DataRecived”, el envío se cifra a través de la clave simétrica y con hash, igual que lo hace el cliente.  

### Ayuda  

```java
package practica.u5;  
import java.io.Serializable;  

public class packet implements Serializable {  
    byte[] message;  
    byte[] hash;  

    public packet(byte[] m, byte[] k) {  
        message = m;  
        hash = k;  
    }  
}  
```  

```java
package practica.u5;  
import java.nio.charset.StandardCharsets;  
import java.security.MessageDigest;  
import java.util.Arrays;  
import javax.crypto.SecretKey;  
import javax.crypto.spec.SecretKeySpec;  

public class Hash {  
    public static SecretKey passwordKeyGeneration(String text, int keySize) {  
        SecretKey sKey = null;  
        if ((keySize == 128) || (keySize == 192) || (keySize == 256)) {  
            try {  
                byte[] data = text.getBytes("UTF-8");  
                MessageDigest md = MessageDigest.getInstance("SHA-256");  
                byte[] hash = md.digest(data);  
                byte[] key = Arrays.copyOf(hash, keySize / 8);  
                sKey = new SecretKeySpec(key, "AES");  
            } catch (Exception ex) {  
                System.err.println("Error generando la clave:" + ex);  
            }  
        }  
        return sKey;  
    }  

    public static boolean compareHash(SecretKey hashclient, SecretKey hashserver) {  
        if (new String(hashclient.getEncoded(), StandardCharsets.UTF_8).equals(new String(hashserver.getEncoded(), StandardCharsets.UTF_8))) {  
            System.out.println("CORRECTO hash, el mensaje no ha sido modificado");  
            return true;  
        } else {  
            System.out.println("FALSO hash, el mensaje ha sido modificado");  
            return false;  
        }  
    }  
}  
```  

```java
package practica.u5;  
import java.security.NoSuchAlgorithmException;  
import javax.crypto.Cipher;  
import javax.crypto.KeyGenerator;  
import javax.crypto.SecretKey;  
import javax.crypto.spec.IvParameterSpec;  

public class AES_Simetric {  
    public static final byte[] IV_PARAM = {0x00, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 0x09, 0x0A, 0x0B, 0x0C, 0x0D, 0x0E, 0x0F};  

    public static byte[] encryptData(SecretKey sKey, byte[] data) {  
        byte[] encryptedData = null;  
        try {  
            Cipher cipher = Cipher.getInstance("AES/CBC/PKCS5Padding");  
            IvParameterSpec iv = new IvParameterSpec(IV_PARAM);  
            cipher.init(Cipher.ENCRYPT_MODE, sKey, iv);  
            encryptedData = cipher.doFinal(data);  
        } catch (Exception ex) {  
            System.err.println("Error cifrando los datos: " + ex);  
        }  
        return encryptedData;  
    }  

    public static byte[] decryptData(SecretKey sKey, byte[] dataEncrypted) {  
        byte[] Data = null;  
        try {  
            Cipher cipher = Cipher.getInstance("AES/CBC/PKCS5Padding");  
            IvParameterSpec iv = new IvParameterSpec(IV_PARAM);  
            cipher.init(Cipher.DECRYPT_MODE, sKey, iv);  
            Data = cipher.doFinal(dataEncrypted);  
        } catch (Exception ex) {  
            System.err.println("Error cifrando los datos: " + ex);  
        }  
        return Data;  
    }  

    public static SecretKey keygenKeyGeneration(int keySize) {  
        SecretKey sKey = null;  
        if ((keySize == 128) || (keySize == 192) || (keySize == 256)) {  
            try {  
                KeyGenerator kgen = KeyGenerator.getInstance("AES");  
                kgen.init(keySize);  
                sKey = kgen.generateKey();  
            } catch (NoSuchAlgorithmException ex) {  
                System.err.println("Generador no disponible.");  
            }  
        }  
        return sKey;  
    }  
}  
```  

```java
package practica.u5;  
import java.security.KeyPair;  
import java.security.KeyPairGenerator;  
import java.security.NoSuchAlgorithmException;  
import java.security.PrivateKey;  
import java.security.PublicKey;  
import javax.crypto.Cipher;  

public class RSA_Asimetric {  
    public static KeyPair randomGenerate(int len) {  
        KeyPair keys = null;  
        try {  
            KeyPairGenerator keyGen = KeyPairGenerator.getInstance("RSA");  
            keyGen.initialize(len);  
            keys = keyGen.genKeyPair();  
        } catch (NoSuchAlgorithmException ex) {  
            System.err.println("Generador no disponible.");  
        }  
        return keys;  
    }  

    public static byte[] encryptData(byte[] data, PublicKey pub) {  
        byte[] encryptedData = null;  
        try {  
            Cipher cipher = Cipher.getInstance("RSA/ECB/PKCS1Padding", "SunJCE");  
            cipher.init(Cipher.ENCRYPT_MODE, pub);  
            encryptedData = cipher.doFinal(data);  
        } catch (Exception ex) {  
            System.err.println("Error cifrando: " + ex);  
        }  
        return encryptedData;  
    }  

    public static byte[] decryptData(byte[] dataEncrypted, PrivateKey priv) {  
        byte[] Data = null;  
        try {  
            Cipher cipher = Cipher.getInstance("RSA/ECB/PKCS1Padding", "SunJCE");  
            cipher.init(Cipher.DECRYPT_MODE, priv);  
            Data = cipher.doFinal(dataEncrypted);  
        } catch (Exception ex) {  
            System.err.println("Error cifrando: " + ex);  
        }  
        return Data;  
    }  
}  
```

**Enviar cualquier objeto serializado a través del flujo:**  
```java
ObjectOutputStream obOut = new ObjectOutputStream(server.getOutputStream());  
obOut.writeObject(pub);  
obOut.flush();  
ObjectInputStream obIn = new ObjectInputStream(server.getInputStream());  
Object obj = obIn.readObject();  
byte[] data = (byte[]) obj;  
```  

**Codificar de byte[] a Base64:**  
```java
varx = byte[];  
Base64.getEncoder().encode(varx);  
```  

**Decodificar de Base64 a byte[]:**  
```java
byte[] var = Base64.getDecoder().decode(varx);  
// varx = byte[] en formato Base64  
```  

**Convertir byte[] a String:**  
```java
Data = byte[];  
new String(data, StandardCharsets.UTF_8);  
```  

**Comparar dos SecretKey:**  
```java
new String(SecretKey1.getEncoded(), StandardCharsets.UTF_8).equals(  
    new String(SecretKey2.getEncoded(), StandardCharsets.UTF_8)  
);  
```