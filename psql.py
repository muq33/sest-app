import psycopg2

class psql():
    def __init__(self, host, database, username, password):
        self.host = host
        self.database = database
        self.username = username
        self.password = password
    
    def connect_db(self):
        try:
            con = psycopg2.connect(host = self.host,database = self.database,
                               user = self.username,password = self.password)
            con.autocommit = True
            return con
    
        except:
            return None
    def insert_db(self,relation, attributes, values):
        connection = self.connect_db()
        cursor = connection.cursor()
        try:
            cursor.execute(f'INSERT INTO {relation} {attributes} VALUES {values}')
            cursor.close()
            
        except:
            return None
        
        finally:
            connection.close()
        return True

    def select_db(self, schema, table, values):
        connection = self.connect_db()
        cursor = connection.cursor()
        values_keys = list(values.keys())
        values_contents = list(values.values())
        query_string = 'SELECT *' + f' FROM {schema}.{table}' + ' WHERE'
        for i in range(len(values)):
            if i >= 1:
                query_string += f" AND {values_keys[i]} = " + f"'{values_contents[i]}'"
            else:
                query_string += f" {values_keys[i]} = " + f"'{values_contents[i]}'"
        try:
            cursor.execute(query_string)
            fetch = cursor.fetchall()
            colnames = [desc[0] for desc in cursor.description]
        except:
            return None
        finally:
            connection.close()
            cursor.close()
        if fetch:
            zip_obj = zip(colnames,fetch[0])
            fetch_dict = dict(zip_obj)
            return fetch_dict
        else:
            return None