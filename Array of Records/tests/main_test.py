'''
testing the functionality of main.py
'''

from batch_creator import make_batches


def main():
    records = ['record1', 'record2', 'record3', 'record4', 'record5', 'record6',
               'record7', 'record8', '99r99r', 'record9', 'record10', 'record11', 'record12', 'record13',
               'record14', 'record15', 'record16', 'record17', 'record18', '9999999999999', 'record19', 'record20']
    print(make_batches(records))


if __name__ == '__main__':
    main()
