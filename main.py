print ('Olá, seja bem vindo a sua calculadora inteligente!')

while True:

    num1 = input('Digite o seu primeiro número: ')
    num2 = input('Digite o seu segundo número: ')

    num_perms1 = None
    num_perms2 = None

    try:
        num1float = float(num1)
        num_perms1 = True
    except:
        num_perms1 = None

    if num_perms1 is None:
        print('Seu primeiro numero esta errado!')
        continue

    try:
        num2float = float(num2)
        num_perms2 = True
    except:
        num_perms2 = None

    if num_perms2 is None:
        print('Seu segundo numero esta errado!')
        continue



    operador = input('Agora escolha seu operador "+" "-" "*" "/" ')
    operadores_perms = '+-*/'

    if operador not in operadores_perms:
        print('Digite apenas um operador valido! ')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador!')
        continue

    soma = num1float + num2float
    sub = num1float - num2float
    mult = num1float * num2float
    div = num1float / num2float

    if operador == '+':
        print(f'Sua soma deu {soma}')
    elif operador == '-':
        print(f'Sua subtração deu {sub}')
    elif operador == '*':
        print(f'Sua multiplicação deu {mult}')
    else:
        print(f'Sua divisão deu {div}')


    
    
    continuar = input('Você que continuar ? [s]im [n]ão ')
    if continuar == 's':
        continue
    elif continuar == 'n':
       print('Você saiu da calculadora!')
       break 
    else:
        print ('Digite apenas "s" ou "n"! ')


