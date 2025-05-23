---
tags:
  - DAM
  - AD
cssclasses:
  - dam-ad
  - table-clean
banner: "![[ad.jpg]]"
banner_y: 0.32
---

# **Resumen TEMA 5.** <br>Bases de datos objeto-relacionales con PostgreSQL

## 1. Conceptos clave
- **PostgreSQL.** Sistema de gestión de bases de datos objeto-relacional (ORDBMS)
- **SQL99.** Estándar que introdujo tipos de datos avanzados
- **Características principales.** Soporte para tipos complejos, arrays y objetos

## 2. Tipos avanzados en PostgreSQL

### 2.1. **Tipo BOOLEAN**

```sql
CREATE TABLE clients (
    id INT PRIMARY KEY,
    nombre VARCHAR(75),
    recomendaria BOOLEAN
);
```

Valores aceptados:

- Verdaderos: `TRUE`, `'t'`, `'true'`, `'y'`, `'yes'`, `'on'`, `'1'`
- Falsos: `FALSE`, `'f'`, `'false'`, `'n'`, `'no'`, `'off'`, `'0'`

Ejemplo de uso:

```sql
INSERT INTO clients VALUES (1, 'Juan Pérez', 'yes');
UPDATE clients SET recomendaria = 'off' WHERE id = 1;
```

### 2.2. **Arrays (Colecciones)**
#### Declaración

```sql
CREATE TABLE clients (
    id INT PRIMARY KEY,
    emails VARCHAR(75)[]  -- Sintaxis PostgreSQL
    -- emails VARCHAR(75) ARRAY  -- Sintaxis estándar SQL
);
```

#### Operaciones con arrays
**Inserción:**

```sql
INSERT INTO clients VALUES 
(1, 'Juan', ARRAY['juan@mail.com', 'juan@work.com']);
-- Alternativa:
INSERT INTO clients VALUES 
(2, 'Ana', '{"ana@mail.com", "ana@work.com"}');
```

**Actualización:**

```sql
-- Actualizar posición específica
UPDATE clients SET emails[2] = 'nuevo@mail.com' WHERE id = 1;

-- Añadir elemento
UPDATE clients SET emails = array_append(emails, 'extra@mail.com');

-- Eliminar elemento
UPDATE clients SET emails = array_remove(emails, 'juan@mail.com');
```

**Consultas:**

```sql
-- Acceder a elementos
SELECT emails[1] FROM clients WHERE id = 1;

-- Consultar dimensiones
SELECT array_ndims(emails), array_length(emails, 1) FROM clients;

-- Filtrar
SELECT * FROM clients WHERE 'juan@mail.com' = ANY(emails);
```

### 2.3. **Tipos compuestos (Objetos)**
#### Definición de tipos

```sql
CREATE TYPE direccion AS (
    calle VARCHAR(255),
    codigo_postal VARCHAR(5),
    ciudad VARCHAR(100),
    pais VARCHAR(100)
);

CREATE TYPE telefono AS (
    tipo VARCHAR(25),
    numero VARCHAR(20)
);
```

#### Uso en tablas

```sql
CREATE TABLE clients (
    id INT PRIMARY KEY,
    nombre VARCHAR(75),
    direccion direccion,
    telefonos telefono[]
);
```

#### Operaciones con tipos compuestos
**Inserción:**

```sql
INSERT INTO clients VALUES (
    1, 
    'María García',
    ROW('Calle Mayor 1', '28001', 'Madrid', 'España'),
    ARRAY[
        ROW('Móvil', '612345678'),
        ROW('Trabajo', '915555555')
    ]
);
```

**Consultas:**

```sql
-- Acceder a campos
SELECT (direccion).ciudad FROM clients WHERE id = 1;

-- Acceder a arrays de objetos
SELECT (telefonos[1]).tipo, (telefonos[1]).numero FROM clients;
```

**Actualización:**

```sql
-- Modificar campo de objeto
UPDATE clients 
SET direccion.ciudad = 'Barcelona' 
WHERE id = 1;

-- Modificar array de objetos
UPDATE clients 
SET telefonos[1].numero = '666777888'
WHERE id = 1;
```

## 3. Características avanzadas de PostgreSQL

1. **MVCC (Multi-Version Concurrency Control).** Permite alta concurrencia sin bloqueos
2. **Amplia variedad de tipos nativos.** 
   - Números de precisión arbitraria
   - Texto ilimitado
   - Tipos geométricos
   - Direcciones IP (IPv4/IPv6)
3. **Funciones en múltiples lenguajes.** PL/pgSQL, Python, Perl, etc.

## 4. Buenas prácticas

1. Usar esquemas para organizar objetos relacionados (`proves."Clients"`)
2. Preferir tipos específicos (BOOLEAN) sobre representaciones alternativas (BIT)
3. Documentar tipos compuestos complejos
4. Usar paréntesis para acceder a campos de objetos en consultas

## 5. Ejemplo completo

```sql
-- Definición de tipos
CREATE TYPE direccion AS (
    calle VARCHAR(255),
    cp VARCHAR(5),
    ciudad VARCHAR(100)
);

CREATE TYPE contacto AS (
    tipo VARCHAR(20),
    valor VARCHAR(100)
);

-- Creación de tabla
CREATE TABLE clientes (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    direccion direccion,
    contactos contacto[],
    activo BOOLEAN DEFAULT true
);

-- Inserción de datos
INSERT INTO clientes (nombre, direccion, contactos) VALUES (
    'Empresa XYZ',
    ROW('Av. Diagonal 123', '08001', 'Barcelona'),
    ARRAY[
        ROW('email', 'info@xyz.com'),
        ROW('teléfono', '932123456')
    ]
);

-- Consulta compleja
SELECT 
    nombre, 
    (direccion).ciudad,
    (contactos[1]).tipo AS tipo_contacto_principal
FROM clientes
WHERE activo AND 'Barcelona' = (direccion).ciudad;
```
