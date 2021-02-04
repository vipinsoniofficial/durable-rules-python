from durable.lang import *

with ruleset('risk'):
    @when_all(  # distinct(True),
        c.first << m.amount > 10,
        c.second << m.amount > c.first.amount * 2,
        c.third << m.amount > (c.first.amount + c.second.amount) / 2)
    def detected(c):
        print('fraud detected -> {0}'.format(c.first.amount))
        print('               -> {0}'.format(c.second.amount))
        print('               -> {0}'.format(c.third.amount))

post('risk', {'amount': 50})
post('risk', {'amount': 200})
post('risk', {'amount': 251})