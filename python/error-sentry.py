from raven import Client


client = Client('http://89dd6d7f4a8e4c07b21dc8f38a8b39c6:063921ba4690414aa911ae939ac56b22@fefinance1-5810:8080/2')

try:
    1 / 0
except ZeroDivisionError:
    client.captureException()

with client.context:
    client.context.merge({'extra': {'item1': 'more info here'}})
    client.captureMessage('Middle of program')
    client.context.clear()


client.captureMessage('End of program')
