#########################################
#             使用说明
# 1. connect_to_database函数中的host user password database修改为自己的mysql
# 2. 插入、查询、更新、删除函数中的表名也修改为自己实际的表名
#########################################



import mysql.connector

# 连接数据库（注意host user password database修改为你自己的mysql）
def connect_to_database():
    try:
        connection = mysql.connector.connect(
            host="your_host",
            user="your_username",
            password="your_password",
            database="your_database"
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

# 插入数据
def insert_product(connection, product):
    try:
        cursor = connection.cursor()
        query = "INSERT INTO products (ProductCode, ProductName, Price, ImageURL, Description, Specifications) VALUES (%s, %s, %s, %s, %s, %s)"
        cursor.execute(query, (product['ProductCode'], product['ProductName'], product['Price'], product['ImageURL'], product['Description'], product['Specifications']))
        connection.commit()
        print("Product inserted successfully.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")

# 查询数据
def get_product_by_code(connection, product_code):
    try:
        cursor = connection.cursor(dictionary=True)
        query = "SELECT * FROM products WHERE ProductCode = %s"
        cursor.execute(query, (product_code,))
        result = cursor.fetchone()
        return result
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

# 更新数据
def update_product_price(connection, product_code, new_price):
    try:
        cursor = connection.cursor()
        query = "UPDATE products SET Price = %s WHERE ProductCode = %s"
        cursor.execute(query, (new_price, product_code))
        connection.commit()
        print("Product price updated successfully.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")

# 删除数据
def delete_product(connection, product_code):
    try:
        cursor = connection.cursor()
        query = "DELETE FROM products WHERE ProductCode = %s"
        cursor.execute(query, (product_code,))
        connection.commit()
        print("Product deleted successfully.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")

# 关闭数据库连接
def close_connection(connection):
    if connection:
        connection.close()
        print("Connection closed.")

# 示例用法
if __name__ == "__main__":
    connection = connect_to_database()

    if connection:
        # 插入数据
        product_to_insert = {
            "ProductCode": "P001",
            "ProductName": "Example Product",
            "Price": 19.99,
            "ImageURL": "http://example.com/image.jpg",
            "Description": "A sample product description",
            "Specifications": "Sample specifications"
        }
        insert_product(connection, product_to_insert)

        # 查询数据
        product_code_to_query = "P001"
        result = get_product_by_code(connection, product_code_to_query)
        if result:
            print("Product found:")
            print(result)
        else:
            print("Product not found.")

        # 更新数据
        new_price = 24.99
        update_product_price(connection, product_code_to_query, new_price)

        # 删除数据
        delete_product(connection, product_code_to_query)

        close_connection(connection)
