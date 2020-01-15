import sys


class RecordsBuilder(object):
    """
    This class creates the batches with suitable delivery size
    to a system in a form of an array.
    """
    def make_batches(self, records):
        batch = []
        temp_array = []
        for record in records:
            if (sys.getsizeof(record)) >= 35:  # 1MB = 1000000.
                continue
            else:
                if len(temp_array) < 5 and sys.getsizeof(temp_array) <= 80:  # I tested with <5 and <=80
                    temp_array.append(record)
                else:
                    batch.append(temp_array)
                    temp_array = []
                    temp_array.append(record)

        batch.append(temp_array)
        return batch
