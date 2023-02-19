#44. Usando a estrutura while, faça uma Calculadora simples, onde:
#Seu programa deverá ler 2 números inteiros, em seguida, apresente um menu:
#[1] soma
#[2] subtração
#[3] multiplicação
#[4] divisão
#[0] SAIR

#Faça uma leitura de qual opção foi digitada
#Por fim, realize e exiba a operação escolhida com os 2 números inteiros anteriormente lidos


modo = (input('''Escolha uma opcao:

[1] soma
[2] subtração
[3] multiplicação
[4] divisão
[0] SAIR

Digite sua escolha: '''))
resultado = ''

if (modo == '1'):
    print(f"\nVoce escolheu SOMA \n")
    numero1 = int(input("Digite 1° numero : "))
    print('+')
    numero2 = int(input("Digite 2° numero : "))
    print()
    print(f'\n{numero1} + {numero2} = {numero1+numero2} \n')


if (modo == '2'):
    print('\nVoce escolheu SUBTRAÇÃO \n')
    numero1 = int(input("Digite 1° numero : "))
    print('-')
    numero2 = int(input("Digite 2° numero : "))
    print()    
    print(f'\n{numero1} - {numero2} = {numero1-numero2} \n')


if (modo == '3'):
    print('\nVoce escolheu MULTIPLICAÇÃO \n')
    numero1 = int(input("Digite 1° numero : "))
    print('x')
    numero2 = int(input("Digite 2° numero : "))
    print()
    print(f'\n{numero1} x {numero2} = {numero1*numero2} \n')


if (modo == '4'):
    print('\nVoce escolheu DIVISAO \n')
    numero1 = int(input("Digite 1° numero : "))
    print('/')
    numero2 = int(input("Digite 2° numero : "))
    print()
    print(f'\n{numero1} / {numero2} = {numero1/numero2} \n')  


if (modo == '0'):
      print("Até mais...")




