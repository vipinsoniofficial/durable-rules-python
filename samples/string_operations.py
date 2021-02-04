from durable.lang import *

with ruleset('strings'):
    @when_all(m.subject.matches('hello.*'))
    def starts_with(c):
        print('string starts with hello -> {0}'.format(c.m.subject))


    @when_all(m.subject.matches('.*hello'))
    def ends_with(c):
        print('string ends with hello -> {0}'.format(c.m.subject))


    @when_all(m.subject.imatches('.*hello.*'))
    def contains(c):
        print('string contains hello (case insensitive) -> {0}'.format(c.m.subject))

assert_fact('strings', {'subject': 'HELLO world'})
assert_fact('strings', {'subject': 'world hello'})
assert_fact('strings', {'subject': 'hello hi'})
assert_fact('strings', {'subject': 'has Hello string'})
assert_fact('strings', {'subject': 'does not match'})