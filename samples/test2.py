from durable.lang import *

with ruleset('animal'):
    # will be triggered by 'Kermit eats flies'
    @when_all((m.predicate == 'eats') & (m.object == 'flies'))
    def frog(c):
        c.assert_fact({'subject': c.m.subject, 'predicate': 'is', 'object': 'frog'})


    @when_all((m.predicate == 'eats') & (m.object == 'worms'))
    def bird(c):
        c.assert_fact({'subject': c.m.subject, 'predicate': 'is', 'object': 'bird'})


    # will be chained after asserting 'Kermit is frog'
    @when_all((m.predicate == 'is') & (m.object == 'frog'))
    def green(c):
        c.assert_fact({'subject': c.m.subject, 'predicate': 'is', 'object': 'green'})


    @when_all((m.predicate == 'is') & (m.object == 'bird'))
    def black(c):
        c.assert_fact({'subject': c.m.subject, 'predicate': 'is', 'object': 'black'})


    @when_all(+m.subject)
    def output(c):
        print('Fact: {0} {1} {2}'.format(c.m.subject, c.m.predicate, c.m.object))

assert_fact('animal', {'subject': 'Kermit', 'predicate': 'eats', 'object': 'flies'})

"""
from durable.lang import *

with ruleset('risk'):
    @when_all(c.first << m.t == 'purchase',
              c.second << m.location != c.first.location)
    # the event pair will only be observed once
    def fraud(c):
        print('Fraud detected -> {0}, {1}'.format(c.first.location, c.second.location))

post('risk', {'t': 'purchase', 'location': 'US'})
post('risk', {'t': 'purchase', 'location': 'CA'})
"""