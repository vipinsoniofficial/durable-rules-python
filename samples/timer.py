from durable.lang import *

with ruleset('timer'):
    @when_all(m.subject == 'start')
    def start(c):
        print('Mytimer')
        c.start_timer('MyTimer', 5)


    @when_all(timeout('MyTimer'))
    def timer(c):
        print('timer timeout')

post('timer', {'subject': 'start'})