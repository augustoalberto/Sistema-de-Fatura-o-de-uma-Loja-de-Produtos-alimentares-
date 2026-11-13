while True:
    nomeCli = str(input('digite o nome do cliente: '))
    genero = str(input('informe o genero do cliente: ')).strip().upper()
    Valcompra = int(input('digite o valor total da compra (kz): '))
    if Valcompra > 100000:
        bonus = Valcompra * 0.10
    else:
        bonus = 0
    total_pagar = Valcompra - bonus
    print('=============== prioridade ==================\n')
    gravida = 'N'
    if genero == 'F':
        gravida = str(input('cliente está gravida? [S/N]: ')).strip().upper()
    idoso = str(input('cliente é idoso (60+ anos)? [S/N]: ')).strip().upper()
    dificiente = str(input('cliente é dificiente? [S/N]: ')).strip().upper()
    if gravida == 'S' or idoso == 'S' or dificiente == 'S':
        prioridade = 'SIM'
    else:
        prioridade = 'NÃO'
    print('============= Factura ================')
    print(f'O nome do cliente é: {nomeCli} o seu genero é {genero}')
    print(f'O valor da compra é: {Valcompra}(kz) e bonus da compra é: {bonus}(kz)')
    print(f'O total pago é: {total_pagar}(kz)')
    print(f'Tem prioridade no atendimento:  {prioridade}')

    if input('\nRegistar outro Cliente? [S/N]: ').upper() !='S':
        break





