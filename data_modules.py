import math
from math import *
from decimal import Decimal
import statistics
from collections import deque
import datetime

print(math.floor(5.5))

subtract_result = 5.6 - 1.4
print(subtract_result)

value1 = Decimal('5.6')
value2 = Decimal('1.4')

subtract_result_decimal = value1 - value2
print(subtract_result_decimal)

#STATISTICS

data = [1, 6, 9, 23, 24, 21]
print(statistics.mean(data))
print(statistics.median(data))
print(statistics.variance(data))

#DEQUEUE

queue = deque(["Eins", "Zwei", "Drei", "Vier", "Funf", "Sechs"])
print(queue.pop())
print(queue)
queue.appendleft("Zero")
print(queue.popleft()) #zero

#DATES

print(datetime.datetime.today())
today = datetime.datetime.today()
print(today)
print(today.year)
print(today.month)
print(today.minute)

created_date = datetime.datetime(2019, 1, 12)
print(created_date.month)
print(created_date) #2019-01-12 00:00:00

day = created_date
print(day + datetime.timedelta(days=20))
print(day + datetime.timedelta(weeks=4))