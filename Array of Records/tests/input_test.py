#a = [int(x) for x in input().split()]
#import array_functions


def main():
    records = []
    while True:
        entry = input('Enter your record (q to quit): ')
        if entry.lower() == 'q':
            break
        records.append(entry)

    if records:
        print(records)


if __name__ == '__main__':
    main()
