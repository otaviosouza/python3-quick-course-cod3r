#!python3

# import package.sub.module
# print('Package :', package.sub.module.package)
# print('Module name : ', package.sub.module.module)

# import data_types.variables
# from data_types import variables, basic
# from data_types import basic, lists, tuplas
# from data_types import conjuntos, dictionary
# from operator import unary

# print(variables.a + variables.b)

# radius = float(input('Enter radius value: '))

# print('circumference length:', 2 * variables.PI * radius)
# print('circle area:', variables.PI * radius**2)
# print('circle area:', variables.PI * pow(radius, 2))

# # basic types
# print(f'Variable value: {basic.n_integer}',
#       f'Variable type: {type(basic.n_integer)}', sep='\t')
# print(f'Variable value: {basic.n_float}',
#       f'Variable type: {type(basic.n_float)}', sep='\t')
# print(f'Variable value: {basic.s_string}',
#       f'Variable type: {type(basic.s_string)}', sep='\t')
# print(f'Variable value: {basic.b_bool_f}',
#       f'Variable type: {type(basic.b_bool_f)}', sep='\t')
# print(f'Variable value: {basic.b_bool_t}',
#       f'Variable type: {type(basic.b_bool_t)}', sep='\t')

# # list type
# print(f'Variable value: {lists.nums}',
#       f'Variable type: {type(lists.nums)}', sep='\t')
# print(len(lists.nums))
# lists.nums.append(4)
# print(lists.nums)
# print(len(lists.nums))
# print(lists.nums[-3:])

# # tuples type
# print(f'Variable value: {tuplas.names}',
#       f'Variable type: {type(tuplas.names)}', sep='\t')
# print('Bia' in tuplas.names)
# print('bia' in tuplas.names)

# # set type
# print(f'Variable value: {conjuntos.conj}',
#       f'Variable type: {type(conjuntos.conj)}', sep='\t')
# print(len(conjuntos.conj))

# # set dictionary
# print(f'Variable value: {dictionary.student}',
#       f'Variable type: {type(dictionary.student)}', sep='\t')
# print(len(dictionary.student))
# print(dictionary.student['name'])
# print(dictionary.student['enrolled'])
# print(dictionary.student['grade'])

# import operators.unary
# import operators.arithmetic
# import operators.relational
# from operators import ternary

# # arithmetic operators
# print(f'x: {operators.arithmetic.x} and y: {operators.arithmetic.y}')
# print(f'x + y = {operators.arithmetic.x + operators.arithmetic.y}')
# print(f'x - y = {operators.arithmetic.x - operators.arithmetic.y}')
# print(f'x * y = {operators.arithmetic.x * operators.arithmetic.y}')
# print(f'x / y = {operators.arithmetic.x / operators.arithmetic.y}')
# print(f'x // y = {operators.arithmetic.x // operators.arithmetic.y}')
# print(f'x % 2 = {operators.arithmetic.x % 2}')
# print(f'x % 7 = {operators.arithmetic.x % 7}')
# print(f'x // 7 = {operators.arithmetic.x // 7}')

# # relational operators
# print(f'x: {operators.relational.x} and y: {operators.relational.y}')
# print(f'x > y = {operators.relational.x > operators.relational.y}')
# print(f'x >= y = {operators.relational.x >= operators.relational.y}')
# print(f'x < y = {operators.relational.x < operators.relational.y}')
# print(f'x <= y = {operators.relational.x <= operators.relational.y}')
# print(f'x == y = {operators.relational.x == operators.relational.y}')
# print(f'x != y = {operators.relational.x != operators.relational.y}')
# print(f'7 != x = {operators.relational.ch != operators.relational.x}')
# print(f'7 == x = {operators.relational.ch == operators.relational.x}')

# # ternary operation
# print(ternary.status)

# import conditional.if_1
# import conditional.if_2


# from data_types import dictionary
# print('for atrib, val in dictionary.student.items')
# for atrib, val in dictionary.student.items():
#     print(atrib, ':', val)
# print('\nfor val in dictionary.student.values')
# for val in dictionary.student.values():
#     print(val)
# print('\nfor atrib in dictionary.student.keys')
# for atrib in dictionary.student.keys():
#     print(atrib)

# from conditional import while_1

from function import basic
print(f'module: {basic.module}')
basic.greeting()
basic.greeting('John Doe')
print('greeting_2 will not be executed')
basic.greeting_2()

result = basic.sum_tim(8, 2, 5)
print(result)

result_2 = basic.sum_tim(c=5, a=8, b=2)
print(result_2)
