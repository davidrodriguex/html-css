print(' {0} Validação de Maioridade {0} '.format(10 * '-='))
nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))
print('Olá {}, prazer em conhecer você, vós tem {} anos'.format(nome, idade))
if(idade >= 18):
    print('Você é maior de idade.')
elif( 3 <= idade <= 14):
    print('Você é criança, saia daqui.')
else:
    print('Você provavelmente está mentindo ou é bebê.')
    