from durable.lang import *

with ruleset('flow'):
    # state condition uses 's'
    @when_all(s.status == 'start')
    def start(c):
        # state update on 's'
        c.s.status = 'next'
        print('start')


    @when_all(s.status == 'next')
    def next(c):
        c.s.status = 'last'
        print('next')


    @when_all(s.status == 'last')
    def last(c):
        c.s.status = 'end'
        print('last')
        # deletes state at the end
        c.delete_state()

update_state('flow', {'status': 'start'})

"""
from durable.lang import *

with ruleset('test'):
    @when_all(m.subject.matches('3[47][0-9]{13}'))
    def amex(c):
        print('Amex detected {0}'.format(c.m.subject))


    @when_all(m.subject.matches('4[0-9]{12}([0-9]{3})?'))
    def visa(c):
        print('Visa detected {0}'.format(c.m.subject))


    @when_all(m.subject.matches('(5[1-5][0-9]{2}|222[1-9]|22[3-9][0-9]|2[3-6][0-9]{2}|2720)[0-9]{12}'))
    def mastercard(c):
        print('Mastercard detected {0}'.format(c.m.subject))

assert_fact('test', {'subject': '375678956789765'})
assert_fact('test', {'subject': '4345634566789888'})
assert_fact('test', {'subject': '2228345634567898'}) """