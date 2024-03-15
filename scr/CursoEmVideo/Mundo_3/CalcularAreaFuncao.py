print('    CALCULANDO ÁREA DO TERRENO')
largura = float(input('Informe a largura: '))
comprimento = float(input('Informe o comprimento: '))

def areaTerreno(larg,compri):
    area = (larg*compri)/2
    print(f'A área de um terreno {larg} X {compri} é de {area:.2f} m2')

areaTerreno(largura,comprimento)