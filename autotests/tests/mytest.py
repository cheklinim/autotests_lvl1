from autotests.autotests import capitalize

assert capitalize('hello') == 'Hello'
#    raise Exception('Функция работает неверно!')
assert capitalize('') == ''
#    raise Exception('Функция работает неверно!')

print('Все тесты пройдены!')

