# snowflake_service.py
from flask import Flask, jsonify
import snowflake.connector

app = Flask(__name__)

# Snowflake configuration (use environment variables in production)
SNOWFLAKE_ACCOUNT = 'your_account'
SNOWFLAKE_USER = 'your_user'
SNOWFLAKE_PASSWORD = 'your_password'
SNOWFLAKE_DATABASE = 'your_database'
SNOWFLAKE_SCHEMA = 'your_schema'
SNOWFLAKE_WAREHOUSE = 'your_warehouse'

@app.route('/get-data', methods=['GET'])
def get_data_from_snowflake():
    con = snowflake.connector.connect(
        user=SNOWFLAKE_USER,
        password=SNOWFLAKE_PASSWORD,
        account=SNOWFLAKE_ACCOUNT,
        warehouse=SNOWFLAKE_WAREHOUSE,
        database=SNOWFLAKE_DATABASE,
        schema=SNOWFLAKE_SCHEMA
    )
    cur = con.cursor()
    cur.execute("SELECT * FROM YOUR_TABLE LIMIT 10;")  # Adjust your query
    data = cur.fetchall()
    return jsonify(data)

if __name__ == '__main__':
    app.run(port=5000)
