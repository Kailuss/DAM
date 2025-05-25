import psycopg2
import matplotlib.pyplot as plt

# Conexión a la base de datos
conn = psycopg2.connect(
    host="192.168.0.191",
    database="odoodb",
    user="odoo",
    password="2992"
)
cur = conn.cursor()

# Consulta de productos
cur.execute("""
    SELECT pt.name, pt.list_price, pc.name 
    FROM product_template pt
    JOIN product_category pc ON pt.categ_id = pc.id
""")

rows = cur.fetchall()
conn.close()

# Procesamiento de datos
precios = []
conteo_categorias = {}

for nombre, precio, categoria in rows:
    if precio is not None:
        precios.append(precio)
    
    if categoria in conteo_categorias:
        conteo_categorias[categoria] += 1
    else:
        conteo_categorias[categoria] = 1

# Histograma: Número de productos por categoría
plt.figure(figsize=(10, 6))
plt.title('Número de productos por categoría')
plt.xlabel('Categorías')
plt.ylabel('Número de productos')
plt.grid(axis='y')
plt.bar(conteo_categorias.keys(), conteo_categorias.values(), color='skyblue')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("productos_por_categoria_comedor.png", dpi=200)
plt.show()

# Histograma: Distribución de precios
plt.figure(figsize=(10, 6))
plt.title('Histograma de precios de productos')
plt.xlabel('Precio')
plt.ylabel('Número de productos')
plt.grid(axis='y')
plt.hist(precios, bins=15, color='orange', edgecolor='white')
plt.tight_layout()
plt.savefig("histograma_precios_comedor.png", dpi=200)
plt.show()
