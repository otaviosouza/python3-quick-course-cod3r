#!python3

# import package.sub.module
# import data_types.variables
# from data_types import variables, basic
from data_types import basic, lists, tuplas
from data_types import conjuntos, hashes

# print('Package :', package.sub.module.package)
# print('Module name : ', package.sub.module.module)

# print(variables.a + variables.b)

# radius = float(input('Enter radius value: '))

# print('circumference length:', 2 * variables.PI * radius)
# print('circle area:', variables.PI * radius**2)
# print('circle area:', variables.PI * pow(radius, 2))

# basic types
print(f'Variable value: {basic.n_integer}',
      f'Variable type: {type(basic.n_integer)}', sep='\t')
print(f'Variable value: {basic.n_float}',
      f'Variable type: {type(basic.n_float)}', sep='\t')
print(f'Variable value: {basic.s_string}',
      f'Variable type: {type(basic.s_string)}', sep='\t')
print(f'Variable value: {basic.b_bool_f}',
      f'Variable type: {type(basic.b_bool_f)}', sep='\t')
print(f'Variable value: {basic.b_bool_t}',
      f'Variable type: {type(basic.b_bool_t)}', sep='\t')

# list type
print(f'Variable value: {lists.nums}',
      f'Variable type: {type(lists.nums)}', sep='\t')
print(len(lists.nums))
lists.nums.append(4)
print(lists.nums)
print(len(lists.nums))
print(lists.nums[-3:])

# tuples type
print(f'Variable value: {tuplas.names}',
      f'Variable type: {type(tuplas.names)}', sep='\t')
print('Bia' in tuplas.names)
print('bia' in tuplas.names)

# set type
print(f'Variable value: {conjuntos.conj}',
      f'Variable type: {type(conjuntos.conj)}', sep='\t')
print(len(conjuntos.conj))

# set dictionary
print(f'Variable value: {dictionary.student}',
      f'Variable type: {type(dictionary.student)}', sep='\t')
print(len(dictionary.student))
print(dictionary.student['name'])
print(dictionary.student['enrolled'])
print(dictionary.student['grade'])
