#SQL-Statments are private and doesn`t exist a set function

# a  private (SQL statment) query for creating table block --> contains generel information of the blockchain blocks
# block_number - the blocknumber 
# created date of corresponding block

__create_table_qy = """CREATE TABLE if not exists block ( 
    block_nummber INTEGER PRIMARY KEY, 
    create_date DATE
);"""

# a private (SQL statment) query for creating table tx --> contains information of corresponding transaction with columns 
# version integer - version number of transaction
# tx_size integer - size of transaction in byte
# vin_size integer - number of elements in vin
# vout_size integer - number of elements in vout
# op_return text - additional information in a transaction and need not be specified
# block_number - block number where the corresponding transaction is save
#
# block_number column referes to the column  block_number of table block

__create_tx_table_qy = """CREATE TABLE IF NOT EXISTS tx (
	transaction_id text INTEGER PRIMARY KEY,
	version integer,
	tx_size integer,
	vin_size integer,
	vout_size integer,
	op_return text,
	block_number integer,
	FOREIGN KEY (block_number) REFERENCES block (block_number)
);"""


# SQL statment to add corresponding block information in table-block 
__add_block_qy = """INSERT INTO block 
    (block_nummber, create_date) 
    VALUES 
    ({block_number},"{create_date}")
;"""

# SQL statment to add corresponding transaction information in table-tx 
__add_tx_qy = """INSERT INTO tx 
    (transaction_id, version, tx_size ,vin_size, vout_size, op_return, block_number) 
    VALUES 
    ("{transaction_id}", {version}, {tx_size}, {vin_size}, {vout_size}, "{op_return}", {block_number})
;"""


# Returns the query to generate the table
def get_create_table_query():
    return __create_table_qy

# Returns the query to add a block and create date to the table-block
def get_add_block_query(bn,cd):
    return __add_block_qy.format(block_number=bn,create_date=cd) 

# Returns the query to generate the table transcation
def get_create_tx_table_query():
    return __create_tx_table_qy

# Returns the query to add a transaction and the information of it to the table-tx
def get_add_tx_query(tx_id, tx_v, tx_s ,tx_vin_size, tx_vout_size, tx_op_return, tx_block_id):
    return __add_tx_qy.format(transaction_id=tx_id, version=tx_v, tx_size=tx_s, vin_size=tx_vin_size, vout_size=tx_vout_size, op_return=tx_op_return, block_number=tx_block_id) 
