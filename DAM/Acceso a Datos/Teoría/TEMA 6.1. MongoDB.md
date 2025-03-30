---
tags:
  - DAM
  - AD
cssclasses:
  - dam-ad
  - table-compact-clean
banner: "![[ad.jpg]]"
banner_y: 0.32
---

# **TEMA 6.1** <br>MongoDB  

## 1. Bases de datos documentales  

Las bases de datos documentales priorizan el rendimiento sobre la integridad referencial. Almacenan datos en documentos JSON o XML, evitando *joins* y normalización. Esto permite consultas más rápidas, aunque sacrifica consistencia. Ejemplos: MongoDB (JSON) y eXist-db (XML).  

### 1.1. **Documento**

Un **documento** en MongoDB es un objeto JSON válido, sin estructura predefinida. Ejemplo:  

```json
{ "nombre": "Joan", "edad": 25 }
```  

### 1.2. **Colección**

Agrupa documentos, pero **no impone estructura.** No equivale a una tabla SQL, ya que no define relaciones ni esquemas.  

### 1.3. **Base de datos**

Contiene múltiples colecciones y permite gestionar permisos de usuarios.  

## 2. MongoDB  

Sistema de código abierto, escalable y orientado a documentos. Usa BSON (Binary JSON) internamente para eficiencia.  

### 2.1. **Características principales**

| Característica          | Descripción                                                                 |  
|-------------------------|-----------------------------------------------------------------------------|  
| **Consultas *ad hoc***  | Búsquedas por campos, rangos o regex.                                       |  
| **Indexación**          | Cualquier campo puede indexarse.                                            |  
| **Replicación**         | Soporta réplicas primario-secundario.                                       |  
| **Balanceo de carga**   | Distribuye colecciones en múltiples servidores.                             |  
| **Agregación**          | Framework para operaciones similares a *GROUP BY* en SQL.                   |  

### 2.2. **Problemas principales**
- **No cumple ACID.** Puede haber inconsistencias en consultas concurrentes.  
- **Bloqueos limitados.** Solo permite escrituras concurrentes en documentos distintos.  

## 3. Operaciones básicas  

### 3.1. **Consultas**
- `show databases`: Lista bases de datos.  
- `db`: Muestra la base de datos actual.  
- `show collections`: Lista colecciones en la base actual.  
- `use <BD>`: Cambia de base de datos.  

### 3.2. **Creación**
- **Base de datos.**  

  ```javascript
  use nuevaBD  // Se crea al insertar el primer documento.
  ```  

- **Colección.**  

  ```javascript
  db.nuevaColeccion.insertOne({ "nombre": "Ejemplo" })
  ```  

### 3.3. **Documentos  **
- **Insertar.**  

  ```javascript
  db.alumnos.insertOne({ "_id": 1, "notas": [85, 90] })  // _id opcional
  ```  

- **Consultar.**  

  ```javascript
  db.alumnos.find({ "nombre": "Joan" })  // Filtro básico
  ```  

## 4. Operadores  

### 4.1. **Relacionales**

| Operador | Ejemplo                          |  
|----------|----------------------------------|  
| `$eq`    | `db.alumnos.find({ nota: {$eq: 6} })` |  
| `$gt`    | `db.alumnos.find({ nota: {$gt: 5} })` |  
| `$in`    | `db.alumnos.find({ nota: {$in: [1, 2]} })` |  

### 4.2. **Lógicos  **
- `$and`: Implícito en múltiples condiciones.  
- `$or`:  

  ```javascript
  db.alumnos.find({ $or: [{ nota: 6 }, { curso: "S1W" }] })
  ```  

### 4.3. **Proyecciones**

Limitan campos devueltos:  

```javascript
db.alumnos.find({}, { nombre: 1, _id: 0 })  // Solo muestra "nombre"
```  

## 5. Modificación y eliminación  

### 5.1. **Actualizar**
- `updateOne`: Modifica el primer documento que cumple el filtro.  

  ```javascript
  db.alumnos.updateOne(
    { _id: 1 },
    { $set: { "nota": 10 } }  // Operador $set
  )
  ```  

### 5.2. **Eliminar**
- `deleteMany`:  

  ```javascript
  db.alumnos.deleteMany({ _id: { $gte: 1 } })
  ```  

## 6. Aggregation Pipeline  

Procesa documentos en etapas (*stages*):  

### 6.1. **Etapas comunes**
1. **`$match`.** Filtra documentos.  

   ```javascript
   { $match: { size: "medium" } }
   ```  

2. **`$group`.** Agrupa y calcula agregados.  

   ```javascript
   { $group: { _id: "$name", total: { $sum: "$quantity" } } }
   ```  

3. **`$sort`.** Ordena resultados.  

### 6.2. **Funciones de agregación**
- **Aritméticas.** `$sum`, `$avg`.  
- **Cadenas.** `$concat`, `$toUpper`.  
- **Fechas.** `$year`, `$month`.  

Ejemplo completo:  

```javascript
db.orders.aggregate([
  { $match: { size: "medium" } },
  { $group: { _id: "$name", total: { $sum: "$quantity" } } },
  { $sort: { total: -1 } }
])
```  

## 7. Clientes recomendados  
- **MongoDB Compass.** Interfaz gráfica oficial.  
- **mongosh.** Consola interactiva.  

Conexión típica:  

```plaintext
mongodb://usuario:contraseña@servidor:27017
```
