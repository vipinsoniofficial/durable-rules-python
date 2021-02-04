"""from durable.lang import *

with ruleset('expense'):
    # this rule will trigger as soon as three events match the condition
    @when_all(count(3), m.amount < 100)
    def approve(c):
        print('approved {0}'.format(c.m))


    # this rule will be triggered when 'expense' is asserted batching at most two results
    @when_all(cap(2), c.expense << m.amount >= 100, c.approval << m.review == True)
    def reject(c):
        print('rejected {0}'.format(c.m))

post_batch('expense', [{'amount': 10},
                       {'amount': 20},
                       {'amount': 16},
                       {'amount': 300},
                       {'amount': 28},
                       {'amount': 400}])

assert_fact('expense', {'review': True})
"""

from durable.lang import *

with ruleset('flow'):
    @when_all(m.action == 'start')
    def first(c):
        raise Exception('Unhandled Exception!')


    # when the exception property exists
    @when_all(+s.exception)
    def second(c):
        print(c.s.exception)
        c.s.exception = None

post('flow', {'action': 'start'})