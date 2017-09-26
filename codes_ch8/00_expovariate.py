#00_expovariate.py

from random import expovariate

'''We added a basis time of 0.5 to prevent
time 0 returned by the distribution.'''

client_arrival_time = round(expovariate(1/20) + 0.5)
server_time_1 = round(expovariate(1/50) + 0.5)
server_time_2 = round(expovariate(1/50) + 0.5)

print(client_arrival_time)
print(server_time_1)
print(server_time_2)
