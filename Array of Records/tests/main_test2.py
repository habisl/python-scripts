#! /usr/bin/python3
"""
Main file to execute records to batches
"""
from batch_creator_test import RecordsBuilder


def main():
    """
    Testset of an array. It can be also implemented by reading from an external file.
    For example: record_file = open("filename.dat", "r")
    """
    records = ['record1', 'record2', 'record3', 'record4', 'record5', 'record6',
               'record7', 'record8', '99r99r', 'record9', 'record10', 'record11', 'record12', 'record13',
               'record14', 'record15', 'record16', 'record17', 'record18', '9999999999999', 'record19', 'record20']

    rb = RecordsBuilder()
    print(rb.make_batches(records))


if __name__ == '__main__':
    main()
