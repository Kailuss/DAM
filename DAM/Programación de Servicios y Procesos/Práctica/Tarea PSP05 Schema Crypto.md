
### 🔐 Esquema de Comunicación Segura: Servidor - Cliente

#### 1. **Intercambio de claves (asimétrico + simétrico)**

- **Servidor:**
    
    - Genera par de claves pública/privada.
        
    - Envía su **clave pública** al cliente (sin cifrar).
        
- **Cliente:**
    
    - Recibe la clave pública del servidor.
        
    - Genera:
        
        - Una **clave simétrica**.
            
        - Un **hash** de la clave simétrica.
            
    - Encripta ambos con la clave **pública del servidor**.
        
    - Envía el paquete al servidor.
        
- **Servidor:**
    
    - Desencripta con su **clave privada**.
        
    - Compara el hash recibido con el generado localmente para verificar integridad.
        

---

#### 2. **Comunicación cifrada con clave simétrica**

Una vez compartida la clave simétrica, ambos utilizan esa clave para:

- Leer la entrada del usuario (una palabra, por ejemplo).
    
- Generar un hash de esa palabra.
    
- Cifrar **palabra + hash** usando la clave **simétrica**.
    
- Enviar el paquete.
    
- Al recibir:
    
    - Desencriptan con la clave simétrica.
        
    - Generan de nuevo el hash del mensaje.
        
    - Comparan con el hash recibido para verificar integridad.
        
    - Si todo va bien, continúan la comunicación.
        

---

#### 3. **Ciclo de comunicación**

- Se envían y reciben paquetes con mensaje y hash cifrados simétricamente.
    
- Se genera un acuse de recibo con `"DATA_RECEIVED"` para cada mensaje recibido correctamente.
    
- El ciclo se repite hasta que se reciba la palabra clave **"adeu"** ("adiós" en catalán), momento en que termina la sesión.
    

---

### ✅ Elementos de seguridad utilizados:

- **Criptografía asimétrica**: para intercambio inicial de claves.
    
- **Criptografía simétrica**: para comunicación eficiente tras el intercambio.
    
- **Hash (probablemente SHA o similar)**: para asegurar integridad del mensaje.
    
- **Acuse de recibo**: para verificar recepción.