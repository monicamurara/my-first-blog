print('ciao, Django girls!') 

if 3>2:
    print('Funziona!')

if 5>2:
	print('5 infatti è maggiore di 2')
else:
	('5 non è maggiore di 2')

volume=57
if volume<20:
	print('piuttosto basso')
elif 20< (volume) <40:
	print('adatto per musica di sottofondo')
elif 40<(volume)<60:
	print('perfetto!')
elif 60<(volume)<80:
	print('ideale per le feste')
elif 80<(volume)<100:
	print('un po\' altino')
else:
	print('oddio le mie orecchie!')

def ciao():
	print('ciao!')
	print('come stai?')
ciao()

def ciao(nome):
	print('ciao '+nome+'!')

ragazze = ['rachel','monica','phoebe','tu']
for nome in ragazze:
	ciao(nome)
	print('prossima ragazza')

