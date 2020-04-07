import sqlite3


def create_db_if_not_exist(data_base):
    conn = sqlite3.connect(data_base)
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS passes(  Name TEXT,'
                '                                       Surname TEXT,'
                '                                       Department_id INT,'
                '                                       id_type_of_passes INT)')
    cur.execute('CREATE TABLE IF NOT EXISTS type_of_pass(  responsible_person TEXT,'
                '                                       temporary FLOAT,'
                '                                       guard_space_id INT)')
    cur.execute('CREATE TABLE IF NOT EXISTS guard_space(  check_in_time TEXT,'
                '                                       check_out_time TEXT,'
                '                                       pass_id INT)')
    conn.commit()
    cur.close()
    conn.close()


def read_data_from_table(data_base, table, column_name = None):
    conn = sqlite3.connect(data_base)
    cur = conn.cursor()
    # querry_column =
    cur.execute('pragma table_info('+table+')')
    column_names = []
    for column in cur.fetchall():
        column_names.append(column[1])
    print(column_names)
    if (column_name is None) or (column_name not in column_names):
        cur.execute('SELECT * FROM '+table)
        data = cur.fetchall()
    else:
        cur.execute('SELECT '+column_name+' FROM ' + table)
        data = cur.fetchall()
    cur.close()
    conn.close()
    return data

def get_value_from_table(data_base, table, id_column, record_id):
    conn = sqlite3.connect(data_base)
    cur = conn.cursor()
    cur.execute('SELECT * FROM ' + table + ' WHERE ' + id_column + " = '" + str(record_id) + "'")
    data = cur.fetchall()
    cur.close()
    conn.close()
    return data

def get_column_name_from_table(data_base, table):
    conn = sqlite3.connect(data_base)
    cur = conn.cursor()
    cur.execute('pragma table_info(' + table + ')')
    column_names = []
    for column in cur.fetchall():
        column_names.append(column[1])
    cur.close()
    conn.close()
    return column_names


def add_data_in_table(data_base, table, data):
    conn = sqlite3.connect(data_base)
    cur = conn.cursor()
    # querry_column =
    cur.execute('INSERT INTO passes VALUES(?,?,?,?)', data)
    conn.commit()
    cur.close()
    conn.close()


def delete_data_in_table(data_base, table, id_column, record_id):
    conn = sqlite3.connect(data_base)
    cur = conn.cursor()
    cur.execute('DELETE FROM '+table+' WHERE '+id_column+" = '"+str(record_id)+"'")
    conn.commit()
    cur.close()
    conn.close()


def update_data_in_table(data_base, table, id_column, record_id, param_colomn, param_val):
    conn = sqlite3.connect(data_base)
    cur = conn.cursor()
    cur.execute('UPDATE '+table+' SET '+param_colomn+'='+str(param_val)+' WHERE '+id_column+" = '"+str(record_id)+"'")
    conn.commit()
    cur.close()
    conn.close()


def get_tables_name(data_base):
    conn = sqlite3.connect(data_base)
    cur = conn.cursor()
    cur.execute('SELECT name FROM sqlite_master'+" WHERE type='table'")
    data = cur.fetchall()
    cur.close()
    conn.close()
    return data


if __name__ == '__main__':
    data_base = './test_data/1st_db_test.db'
    table = 'passes'
    create_db_if_not_exist(data_base)
    get_tables_name(data_base)
    # persons_data = []
    # persons_data.append(["Mike", "Perin", 1, 2])
    # persons_data.append(["Ivan", "Van", 2, 6])
    # persons_data.append(["Kir9", "Sellton", 3, 16])
    #
    # for person_data in persons_data:
    #     add_data_in_table(data_base, table, person_data)
    # data = read_data_from_table(data_base, table)
    # print(data)
    # id_column = 'Name'
    # record_id = 'Kir9'
    # delete_data_in_table(data_base, table, id_column, record_id)
    # data = read_data_from_table(data_base, table)
    # print(data)
    #
    # persons_data = []
    # persons_data.append(["Tema", "Perin", 1, 2])
    # persons_data.append(["Kirill", "Perin", 2, 6])
    #
    # persons_data.append(["Kir9", "Redin", 3, 16])
    # for person_data in persons_data:
    #     add_data_in_table(data_base, table, person_data)
    # data = read_data_from_table(data_base, table)
    # print(data)
    # update_data_in_table(data_base, table, id_column, record_id,'Department_id', 4)
    # data = read_data_from_table(data_base, table)
    # print(data)
    #
    # data = read_data_from_table(data_base, 'guard_space')
    # print(data)
    # data = read_data_from_table(data_base, 'type_of_pass')
    # print(data)