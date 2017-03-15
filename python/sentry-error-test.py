from raven import Client

client = Client('http://395f5c80b0a948f7acae201285c15a7a:c5074aa9132e4fa580fed276c338b72f@localhost:8080/2')

try:
    1 / 0
except ZeroDivisionError:
    client.captureException()

with client.context:
    client.context.merge({'extra': {'item1': 'more info here'}})
    client.captureMessage('Middle of program')
    client.context.clear()


client.captureMessage('End of program')
