from SQL import querys as qy
import sqlite3

# initialise the two tables for database 
def initTabel(connection):
    cursor = connection.cursor()
    __execute_command(cursor,qy.get_create_table_query())
    __execute_command(cursor,qy.get_create_tx_table_query())
    __execute_command(cursor,qy.get_create_filtered_OP())
    # never forget this, if you want that the changes are saved
    connection.commit()


# adding a block to table-block with corresponding information
def addBlock(connection, block_number, create_date):
    cursor = connection.cursor()
    print("Add block to table")
    __execute_command(cursor,qy.get_add_block_query(block_number,create_date))
    # never forget this, if you want that the changes are saved
    connection.commit() 


# adding a transaction to table-tx with corresponding information
def addTrans(connection,  block_number, transaction_id, version, tx_size ,vin_size, vout_size, tx_time, tx_value, op_return):
    cursor = connection.cursor()
    print("Add trans to table")
    __execute_command(cursor,qy.get_add_tx_query(transaction_id, version, tx_size ,vin_size, vout_size, tx_time, tx_value, op_return, block_number))
    # never forget this, if you want that the changes are saved
    connection.commit()

# adding a op_return field that is undefinable
def addOP(connection, block_number, transaction_id, prev_tx, tx_value, op_return, op_length, s_address, r_address, address_number, tx_time):
    cursor = connection.cursor()
    print("Add trans to table")
    __execute_command(cursor,qy.get_add_filtered_OP( transaction_id, block_number, prev_tx, tx_value, op_return, op_length, s_address, r_address, address_number, tx_time))
    # never forget this, if you want that the changes are saved
    connection.commit()


# catch error if a block was added in table-block before
# catch error if a transaction was added in table-tx with corresponding information before
def __execute_command(cursor, sql_command):
    try:
        sql_command = str(sql_command)
        cursor.execute(sql_command)
    except sqlite3.IntegrityError:
        print('Oops!  That was no valid number: '+ str(sql_command) + 'Maybe the PRIMARY KEY exist!')

