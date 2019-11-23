def get_summ(one, two, delimiter='&'):
   return str(one)+delimiter+str(two)
     

result = get_summ('Learn', 'Python')
print(result)
print(result.upper())

result = get_summ(123, 'Python')
print(result)
print(result.upper())