calls = 0

def count_calls():
  global calls
  calls += 1
  return calls

def string_info(string):
  b = ()
  b = (len(string), string.upper(), string.lower())
  count_calls()
  return (b)

def is_contains(string, list_to_search):
  count_calls()

  for i in list_to_search:
    if i.upper() in string.upper():
      return True
  return False

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycle', 'cyclic']))
print(calls)
