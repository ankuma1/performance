import csv


class ReadCsvFile:

    def __init__(self, filePath):
        self.csvPath = filePath

    def reader(self):
        reader = csv.DictReader(open(self.csvPath))
        data = []
        for element in reader:
            data.append(element)
        return data
