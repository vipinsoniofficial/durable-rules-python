"""from durable.lang import *

with ruleset('expense'):
    @when_any(all(c.first << m.subject == 'approve',
                  c.second << m.amount == 1000),
              all(c.third << m.subject == 'jumbo',
                  c.fourth << m.amount == 10000))
    def action(c):
        if c.first:
            print('Approved {0} {1}'.format(c.first.subject, c.second.amount))
        else:
            print('Approved {0} {1}'.format(c.third.subject, c.fourth.amount))

post('expense', {'subject': 'approve'})
post('expense', {'amount': 1000})
post('expense', {'subject': 'jumbo'})
post('expense', {'amount': 10000})"""

from durable.lang import *

with ruleset('risk'):
    @when_all(c.first << m.t == 'deposit',
              none(m.t == 'balance'),
              c.third << m.t == 'withdrawal',
              c.fourth << m.t == 'chargeback')
    def detected(c):
        print('fraud detected {0} {1} {2}'.format(c.first.t, c.third.t, c.fourth.t))

assert_fact('risk', {'t': 'deposit'})
assert_fact('risk', {'t': 'withdrawal'})
assert_fact('risk', {'t': 'chargeback'})

assert_fact('risk', {'sid': 1, 't': 'balance'})
assert_fact('risk', {'sid': 1, 't': 'deposit'})
assert_fact('risk', {'sid': 1, 't': 'withdrawal'})
assert_fact('risk', {'sid': 1, 't': 'chargeback'})
retract_fact('risk', {'sid': 1, 't': 'balance'})