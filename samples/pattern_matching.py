from durable.lang import *

with ruleset('match'):
    @when_all(m.url.matches('(https?://)?([0-9a-z.-]+)%.[a-z]{2,6}(/[A-z0-9_.-]+/?)*'))
    def approved(c):
        print('match-> url {0}'.format(c.m.url))


def match_complete_callback(e, state):
    print('match -> expected {0}'.format(e.message))


post('match', {'url': 'https://github.com'})
post('match', {'url': 'http://github.com/jruizgit/rul!es'}, match_complete_callback)
post('match', {'url': 'https://github.com/jruizgit/rules/reference.md'})
post('match', {'url': '//rules'}, match_complete_callback)
post('match', {'url': 'https://github.c/jruizgit/rules'}, match_complete_callback)
