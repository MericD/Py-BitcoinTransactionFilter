# Bitcoin-Transaction-Parser
A python3 script that searches the Bitcoin blockchain and filters the transactions which contains an OP_RETURN field.

## Motivation
This script was developed to analyze the op_return fields of bitcoin transactions on different contents and to find illegal activities.

## More Information

After the corresponding transactions have been filtered, the found transactions are saved in a SQLite Database with their corresponding information. Finally, the transactions can be graphically displayed with the seaborn library.

##  Installing
Further development requires python3 and pip3.

Instructions for installing Python3 for Linux and Mac OS operating systems:

https://realpython.com/installing-python/


Instructions for installing Pip3:

```
sudo apt-get install python3-pip
```

After installing/updating python and pip the following libraries are needed:

For displaying diagrams:
```
pip3 install seaborn
```

For used arrays:
```
pip3 install numpy
```

For plotting diagrams:
```
pip3 install -U matplotlib
```

For reading files:
```
pip3 install pandas
```

Conection to bitcoin server:
```
pip install python-bitcoinrpc
```

### Prerequisites

Befor running the script 

1. The blocks of the Bitcoin blockchain are needed. They can be download with:
* [Bitcoin-Core](https://bitcoin.org/de/download)
#the *.dat Files are not pushed to the git-repository because their size are bigger than 100mb!

2. Before running the script the parameters for a full node connection in config.py must be set
- Desired block range ('start_block' :xxx  and  'end_block':xxx) 

```
.../bitcoin-0.16.2/bin$ ./bitcoind 
```

or 

 run a Bitcoin Full Node with specific parameters in the downloaded file (here it is bitcoin-0.16.2):
 
```
.../bitcoin-0.16.2/bin$ ./bitcoind -server=1 -txindex=1 -rpcuser=rpc -rpcpassword=bitmaster -printtoconsole -testnet=0 
```
--> Attention the parameters for desired block range must be set in config.py

3. run the script in the file Python-Bitcoin-Transaction-Parser :
```
$ python3 main.py
```
- if you want to use multithreading run it as:
```
$ python3 process.py
```
4. #I am using the following Project: https://github.com/garethjns/PyBC to parse the .dat Files

##Befor Running

- VM and multithreading were used for faster execution. For a general run, modify the main.py file as follows:

```python

###Parameter
# name of the database 
__databaseFile = config.CONFIG['database_file_name']


# the first block to analyze
__start_block = config.CONFIG['start_block']

# the last block to analyze
__end_block = config.CONFIG['end_block']

# get all Blocks and transactions in range of __start_block to __end_block
block_trans = {}
while __start_block < __end_block + 1:
block_trans.update(rpc.get_transactions(__start_block)[0])
__start_block += 1

# filter all transactions that contain a field OP_RETURN 
find_block_trans = core.find_op_return(block_trans)

# save all transaction with a OP_RETURN field
core.save_result_in_database(__databaseFile, find_block_trans)

# create diagram by using created database (can be removed if diagrams are not desired)
diagram.create_diagrams()
```

### Example outputs
### Example outputs

- After running the script a database file is created that contains two tables. This file can be open with the tool [DB Browser for SQLite](https://sqlitebrowser.org)

- Table of found blocks:
![block](https://user-images.githubusercontent.com/23129546/46921075-15896e00-cff7-11e8-843c-01482e678674.png)

- Table of found trnsactions:
![tx](https://user-images.githubusercontent.com/23129546/46921206-b298d680-cff8-11e8-9786-33359748b376.png)

- and diagrams are builded as well. They contain the timeline of used OP_RETURN fields
![time](https://user-images.githubusercontent.com/23129546/46921217-cd6b4b00-cff8-11e8-9f83-60798e45db25.png)


 - and filter the content of these OP_RETURN fields by following contents:
![number](https://user-images.githubusercontent.com/23129546/46921220-dd832a80-cff8-11e8-908b-1aad67fa3213.png)



## Built With

* [Visual Studio Code](https://code.visualstudio.com) - Programming tool
* [DB Browser for SQLite](https://sqlitebrowser.org) - Showing Database



## Authors

* **Emine Saracoglu** - *Initial work* - [Python-Bitcoin-Transaction-Parser](https://github.com/MericD/Python-Bitcoin-Transaction-Parser.git)

## License

