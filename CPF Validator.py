'''
0 -> 1 * 10 = 10           #    1 * 11 = 11 <-
1 -> 6 * 9  = 54           #    6 * 10 = 60
2 -> 8 * 8  = 64           #    8 * 9  = 72
3 -> 9 * 7  = 63           #    9 * 8  = 72
4 -> 9 * 6  = 54           #    9 * 7  = 63
5 -> 5 * 5  = 25           #    5 * 6  = 30
6 -> 3 * 4  = 12           #    3 * 5  = 15
7 -> 5 * 3  = 15           #    5 * 4  = 20
8 -> 0 * 2  = 0            #    0 * 3  = 0
                           # -> 0 * 2  = 0
'''

cpf = '168.995.350-09'
digits = cpf.split('-')
digits.pop()
temp_number = ''.join(digits)
cpf_digits = temp_number.split('.')
temp_digits = ''.join(cpf_digits)
multiplier = 10
final_result = 0

while multiplier <= 10 and multiplier > 1:
    for item in temp_digits:
        if item.isdigit():
            result = int(item) * multiplier
            final_result += result
        print(f'{item} * {multiplier} = {result}')
        multiplier -= 1

validation = 11 - (final_result % 11)
if validation > 9:
    validation = 0
else:
    validation


print(f'\n1st Digit: {validation}\n')

cpf_digits.append(str(validation))
temp_digits = ''.join(cpf_digits)

multiplier_2 = 11
final_result_2 = 0

while multiplier_2 <= 11 and multiplier_2 > 1:
    for item in temp_digits:
        if item.isdigit():
            result_2 = int(item) * multiplier_2
            final_result_2 += result_2
        print(f'{item} * {multiplier_2} = {result_2}')
        multiplier_2 -= 1

validation_2 = 11 - (final_result_2 % 11)

if validation_2 > 9:
    validation_2 = 0
else:
    validation_2


print(f'\n2nd Digit: {validation_2}')

cpf_digits.append(str(validation_2))
temp_digits = ''.join(cpf_digits)

validated_cpf = temp_digits

if validated_cpf:
    print('\nCPF Válido!')
else:
    print('\nCPF Inválido')
# validation = 'Valid CPF' if validated_cpf else 'Invalid CPF'
