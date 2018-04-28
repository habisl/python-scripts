# Array of data

A python3 based library which takes in an array of records of variable size and splits the input to batches of records (array of arrays) suitably sized for delivery to a system.

### Primary requirements

* Maximum size of output record is 1 MB
* Larger records should be discarded
* Maximum size of output batch is 5 MB 
* Maximum number of records in an output batch is 500 
* Sample Input for the library is: [< record1 >, < record2 >, < record3 >, … , < recordn >] and Output is: [< batch1 >, < batch2 >, …, < batchn >] 
Each batch is an array of records just like in the input. The records can be assumed to be strings of variable length and they have to pass intact through the system and records should stay in the order that they arrive.

### Further Scope

The library would be useful in an application which continuously reads large numbers of records from a data source and writes them to an AWS Kinesis Data stream. The library could be used to create optimum batches for sending data to the Kinesis stream. However, the library doesn’t need to contain any AWS related code.


### Prerequisites

Python3 requires in order to run the program.

### Running the tests

Program can be run from command line. Main files are in src folder. main.py can be executed from 'src' folder.
Tests folder can be ignored or was used during development. 
```
python3 main.py
```

### About Amazon Kinesis

What is a record?

A record is the unit of data stored in an Amazon Kinesis data stream. A record is composed of a sequence number, partition key, and data blob. Data blob is the data of interest your data producer adds to a data stream. The maximum size of a data blob (the data payload before Base64-encoding) is 1 megabyte (MB).

### Built With

* PyCharm 

### Authors

* **Habibul Islam** 

### Acknowledgments

* stackoverflow for giving me some idea.

