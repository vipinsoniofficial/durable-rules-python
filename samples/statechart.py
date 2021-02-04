"""from durable.lang import *

with statechart('expense'):
    # initial state 'input' with two triggers
    with state('input'):
        # trigger to move to 'denied' given a condition
        @to('denied')
        @when_all((m.subject == 'approve') & (m.amount > 1000))
        # action executed before state change
        def denied(c):
            print('denied amount {0}'.format(c.m.amount))


        @to('pending')
        @when_all((m.subject == 'approve') & (m.amount <= 1000))
        def request(c):
            print('requesting approve amount {0}'.format(c.m.amount))

    # intermediate state 'pending' with two triggers
    with state('pending'):
        @to('approved')
        @when_all(m.subject == 'approved')
        def approved(c):
            print('expense approved')


        @to('denied')
        @when_all(m.subject == 'denied')
        def denied(c):
            print('expense denied')

    # 'denied' and 'approved' are final states
    state('denied')
    state('approved')

# events directed to default statechart instance
post('expense', {'subject': 'approve', 'amount': 100})
post('expense', {'subject': 'approved'})

# events directed to statechart instance with id '1'
post('expense', {'sid': 1, 'subject': 'approve', 'amount': 100})
post('expense', {'sid': 1, 'subject': 'denied'})

# events directed to statechart instance with id '2'
post('expense', {'sid': 2, 'subject': 'approve', 'amount': 10000})"""

from durable.lang import *

with statechart('workers'):
    # super-state 'work' has two states and one trigger
    with state('aaa'):
        # sub-state 'enter' has only one trigger
        with state('enters'):
            @to('process')
            @when_all(m.subject == 'enter')
            def continue_process(c):
                print('start process')

        with state('process'):
            @to('process')
            @when_all(m.subject == 'continue')
            def continue_process(c):
                print('continue processing')


        # the super-state trigger will be evaluated for all sub-state triggers
        @to('canceled')
        @when_all(m.subject == 'cancel')
        def cancel(c):
            print('cancel process')

    state('canceled')

# will move the statechart to the 'work.process' sub-state
post('workers', {'subject': 'enter'})

# will keep the statechart to the 'work.process' sub-state
post('workers', {'subject': 'continue'})
post('workers', {'subject': 'continue'})

# will move the statechart out of the work state
post('workers', {'subject': 'cancel'})