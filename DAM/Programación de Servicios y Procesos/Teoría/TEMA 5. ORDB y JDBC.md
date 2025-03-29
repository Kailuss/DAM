---
tags: [DAM, PSP]
cssclasses:
  - dam-psp
  - table-compact-clean
banner: "![[psp.jpg]]"
banner_y: 0.26
---

# **TEMA 5.** <br>Bases de datos objeto-relacionales (PostgreSQL)

Las diferentes versiones del lenguaje SQL han ido incorporando características que permiten trabajar directamente con objetos. La revisión más significativa se produjo en 1999, dando lugar al estándar SQL99. Esta revisión introdujo tipos de datos no convencionales y permitió la definición de tipos compuestos o estructurados. Los principales tipos que incorpora son:

- **Boolean.** Antes se solía usar el tipo BIT para valores lógicos.  
- **Grandes objetos.** SQL99 define dos tipos: BLOB (Binary Large Object) para datos binarios como imágenes o vídeos, y CLOB (Character Large Object) para textos extensos como informes o páginas web.  
- **Colecciones.** Permiten almacenar conjuntos de datos, tanto básicos como estructurados.  
- **Tipos compuestos o estructurados.** Facilitan la creación de tipos definidos por el usuario.  
- **Referencias a tipos estructurados.** Actúan como punteros a tipos compuestos, abstraendo su ubicación física.  

Estos tipos aportan flexibilidad al mapear clases del modelo utilizando directamente el lenguaje de definición DDL. Además, SQL amplía su sintaxis para manipular estos nuevos tipos de manera similar a los atributos de objetos.

## 1. PostgreSQL

PostgreSQL es una base de datos relacional de código abierto que implementa muchas características de SQL99. Algunas de sus principales características son:

- **Alta concurrencia.** Utiliza el sistema MVCC (Acceso Concurrente Multiversión) para permitir escrituras sin bloqueos mutuos.  
- **Amplia variedad de tipos nativos.** Soporta números de precisión arbitraria, texto de longitud ilimitada, figuras geométricas y direcciones IP (IPv4 e IPv6).  
- **Tipos definidos por el usuario.**  
- **Funciones.** Pueden escribirse en varios lenguajes como C, Java o PL.  

## 2. Características nuevas de PostgreSQL

### 2.1. **Boolean**

PostgreSQL soporta el tipo BOOLEAN según el estándar:

```sql
CREATE TABLE IF NOT EXISTS proves."Clients"
(
    id integer NOT NULL,
    nom character varying(75),
    recomanaria boolean,
    CONSTRAINT "Clients_pkey" PRIMARY KEY (id)
)
```

Valores admitidos:  

- **Verdadero.** `TRUE`, `'t'`, `'true'`, `'y'`, `'yes'`, `'on'`, `'1'`.  
- **Falso.** `FALSE`, `'f'`, `'false'`, `'n'`, `'no'`, `'off'`, `'0'`.  

Ejemplos:  

```sql
INSERT INTO proves."Clients"(id, nom, recomanaria) VALUES (1, 'Jo Mateix', TRUE);
UPDATE proves."Clients" SET recomanaria='off' WHERE id=1;
```

### 2.2. **Colecciones**

PostgreSQL soporta el tipo ARRAY, que puede declararse de dos formas:

1. Según el estándar:  

```sql
CREATE TABLE IF NOT EXISTS proves."Clients"
(
    id integer NOT NULL,
    nom character varying(75),
    recomanaria boolean,
    emails character varying(75) ARRAY,
    CONSTRAINT "Clients_pkey" PRIMARY KEY (id)
)
```

2. Usando la sintaxis específica de PostgreSQL:  

```sql
CREATE TABLE IF NOT EXISTS proves."Clients"
(
    id integer NOT NULL,
    nom character varying(75),
    recomanaria boolean,
    emails character varying(75)[],
    CONSTRAINT "Clients_pkey" PRIMARY KEY (id)
)
```

**Nota.** La primera posición del array es la 1, no la 0.

### 2.3. **Insert**

Los arrays pueden especificarse de dos maneras:

1. Usando la función `ARRAY`:  

```sql
INSERT INTO proves."Clients"
VALUES (2, 'Un Altre', FALSE, ARRAY['unaltre@mail.org','unaltre@feina.com']);
```

2. Usando la sintaxis alternativa:  

```sql
INSERT INTO proves."Clients"
VALUES (1, 'Jo Mateix', TRUE, '{"jomateix@mail.org","jomateix@feina.com"}');
```

Para arrays bidimensionales:  

```sql
INSERT INTO sal_emp VALUES ('Carol',
    ARRAY[20000, 25000, 25000, 25000],
    ARRAY[['breakfast', 'consulting'], ['meeting', 'lunch']]);
```

### 2.4. **Update**

Se puede actualizar todo el array:  

```sql
UPDATE proves."Clients"
SET emails = '{"nouEmail1@mail.com", "nouEmail2@mail.com", "nouEmail3@mail.com"}'
WHERE nom='Jo Mateix';
```

O una posición específica. Si la posición no existe, se crean las necesarias inicializadas a `NULL`:  

```sql
UPDATE proves."Clients" SET emails[3] = 'nouEmail3@mail.com' WHERE nom='Jo Mateix';
```

Para añadir un valor al final:  

```sql
UPDATE proves."Clients" SET emails = array_append(emails, 'nouEmail4@mail.com') WHERE nom='Jo Mateix';
```

Para eliminar un valor:  

```sql
UPDATE proves."Clients" SET emails = array_remove(emails, 'nouEmail3@mail.com') WHERE nom='Jo Mateix';
```

### 2.5. **Select**

Se puede seleccionar una posición del array:  

```sql
SELECT emails[1] FROM proves."Clients" WHERE id=1;
```

Un rango de posiciones:  

```sql
SELECT emails[1:2] FROM proves."Clients" WHERE id=1;
```

Consultar dimensiones del array:  

```sql
SELECT array_ndims(emails) FROM proves."Clients" WHERE id=1;
```

Consultar longitud de una dimensión:  

```sql
SELECT array_length(emails, 1) FROM proves."Clients" WHERE id=1;
```

### 2.6. **Where**

Filtrar por una posición:  

```sql
SELECT * FROM proves."Clients" WHERE emails[1]='rang1@mail.org';
```

Comprobar si un valor coincide con cualquier elemento del array:  

```sql
SELECT * FROM proves."Clients" WHERE 'rang1@mail.org' = ANY (emails);
```

Comparar un valor con todos los elementos del array:  

```sql
SELECT * FROM proves."Clients" WHERE 'rang1@mail.org' <> ALL (emails);
```

## 3. Tipos compuestos

### 3.1. **DDL**

PostgreSQL soporta la declaración previa de tipos compuestos. Por ejemplo:

1. Crear el tipo `t_adreca`:  

```sql
CREATE TYPE proves.t_adreca AS
(
    adreca character varying(255),
    codipostal character varying(5)[],
    poblacio character varying(100)[],
    pais character varying(100)[]
);
```

2. Crear el tipo `t_telefon`:  

```sql
CREATE TYPE proves."t_telefon" AS
(
    tipus character varying(25),
    numero character varying(20)
);
```

Usarlos en una tabla:  

```sql
CREATE TABLE IF NOT EXISTS proves."Clients"
(
    id integer NOT NULL,
    nom character varying(75) COLLATE pg_catalog."default",
    emails character varying(75)[] COLLATE pg_catalog."default",
    recomanaria boolean,
    adreca proves.t_adreca,
    telefon proves.t_telefon,
    CONSTRAINT "Clients_pkey" PRIMARY KEY (id)
);
```

**Nota.** Las tablas crean automáticamente un tipo compuesto con su mismo nombre.  

### 3.2. **DML**

Para insertar objetos:  

```sql
INSERT INTO proves."Clients"(..., telefon) VALUES (..., ROW('Casa', '874563254'));
```

Acceder a atributos en consultas:  

```sql
SELECT (telefon).tipus FROM proves."Clients" WHERE (telefon).numero='874563254';
```

**Importante.** Los nombres de campos deben ir entre paréntesis para evitar confusiones con nombres de tablas.  

Modificar atributos individuales:  

```sql
UPDATE proves."Clients"
SET telefon.numero='874563252'
WHERE (telefon).tipus='Casa' AND id=3;
```
