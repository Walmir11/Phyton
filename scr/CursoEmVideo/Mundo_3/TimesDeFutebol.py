times = ('Flamengo','Palmeiras','Cruzeiro','Corinthias', 'Grêmio','Atlético-MG','Botafogo','Bragantino','Fluminense',
         'Athletico-PR','Internacional','Fortaleza','São Paulo','Cuiabá','Vasco','Bahia','Santos','Goiás','Coritiba',
         'América-MG')

print(f'Os cinco primeiros times são {times[0:5]}')
print('-'*100)
print(f'Os quatro últimos times são {times[17:]}')
print('-'*100)
print(sorted(times))
print('-'*100)
indice = times.index('Bragantino')
print(f'A posição do Bragantino é {indice+1}')