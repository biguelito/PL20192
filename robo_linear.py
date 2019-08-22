x = input('insira os comandos: ').lower()

while 't' in x and 'f' in x:
    x = x.replace('tf', '')
    x = x.replace('ft', '')

if 'f' in x:
    print('o robo deu', len(x), 'passos pra frente')
else:
    print('o robo deu', len(x), 'passos pra tras')
