#Regex
import re

#CEP
from pycep_correios import get_address_from_cep, WebService


def none(arg):
    return True

def validate_cpf(sequence):
    fiscalCodes = {
    1: ('DF', 'GO', 'MT', 'MS', 'TO'),
    2: ('AC', 'AP', 'AM', 'PA', 'RO', 'RR'),
    3: ('CE', 'MA', 'PI'),
    4: ('AL', 'PB', 'PE', 'RN'),
    5: ('BA', 'SE'),
    6: 'MG',
    7: ('ES', 'RJ'),
    8: 'SP',
    9: ('PR', 'SC'),
    0: 'RS'}
    cpf = [int(char) for char in sequence if char.isdigit()]

    if len(cpf) != 11:
        return False

    if cpf == cpf[::-1]:
        return False
    
    for i in range(9, 11):
        value = sum((cpf[num] * ((i+1) - num) for num in range(0, i)))
        digit = ((value * 10) % 11) % 10
        if digit != cpf[i]:
            return False

    return True

def validate_cep(cep):
    try:
        address = get_address_from_cep(f'{cep}', webservice=WebService.APICEP)
        return True
    except:
        return False
    
def validate_name(name):
    check = any(char.isdigit() for char in name)
    return False if check == True else True

def validate_email(email):
    regex = '^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$'
    if re.match(regex,email):
        return True
    return False

def validate_fields(screen, functions: tuple):
    validate_matrix = functions
    validated_matrix = []
    i = 0
    for j in screen.ids:
        validated_matrix.append(validate_matrix[i](screen.ids[j].text))
        i = i + 1
    return True if all(validated_matrix) == True else False