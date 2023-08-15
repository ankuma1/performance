import random

from register_runner_script import util
import sys

sys.path.append("/Users/anilkumar/PycharmProjects/Demo_Locust_Project")

read_data = util.read_csv_file("/Users/anilkumar/PycharmProjects/Demo_Locust_Project/data/credential.csv")
print(read_data)
value = read_data.pop()
print(value.get("username"))
print(value.get("password"))

read_data = util.read_csv_file("/Users/anilkumar/PycharmProjects/Demo_Locust_Project/data/credential.csv")
print(read_data)
value = random.choice(read_data)
print(value.get("username"))
print(value.get("password"))