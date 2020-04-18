import pandas as pd
import matplotlib.pyplot as plt
from numpy import float64

df = pd.read_excel(r"C:\Users\leand\Desktop\python\dadosemergentes\paisesemergentes2.xlsx")

gdp = df['Brazil [BRA]']      # Pega todos dados de uma coluna e bota em uma variavel
gdpBrazil = gdp.iloc[1:34]
print(gdpBrazil)
print(type(gdpBrazil))      # Mostra que o tipo da variavel é séries
print(gdpBrazil.shape)

gdp = df['Indonesia [IDN]']      # Pega todos dados de uma coluna e bota em uma variavel
gdpIndonesia = gdp.iloc[1:34]
print(gdpIndonesia)

gdp = df['China [CHN]']      # Pega todos dados de uma coluna e bota em uma variavel
gdpChina = gdp.iloc[1:34]
print(gdpChina)

gdp = df['India [IND]']      # Pega todos dados de uma coluna e bota em uma variavel
gdpIndia = gdp.iloc[1:34]
print(gdpIndia)

gdp = df['Hong Kong SAR, China [HKG]']      # Pega todos dados de uma coluna e bota em uma variavel
gdpHong = gdp.iloc[1:34]
print(gdpHong)

gdp = df['Mexico [MEX]']      # Pega todos dados de uma coluna e bota em uma variavel
gdpMexico = gdp.iloc[1:34]
print(gdpMexico)

gdp = df['Colombia [COL]']      # Pega todos dados de uma coluna e bota em uma variavel
gdpColombia = gdp.iloc[1:34]
print(gdpColombia)

gdp = df['Peru [PER]']      # Pega todos dados de uma coluna e bota em uma variavel
gdpPeru = gdp.iloc[1:34]
print(gdpPeru)

gdp = df['Turkey [TUR]']      # Pega todos dados de uma coluna e bota em uma variavel
gdpTurquia = gdp.iloc[1:34]
print(gdpTurquia)

gdp = df['Morocco [MAR]']      # Pega todos dados de uma coluna e bota em uma variavel
gdpMarroco = gdp.iloc[1:34]
print(gdpMarroco)

gdp = df['Nigeria [NGA]']      # Pega todos dados de uma coluna e bota em uma variavel
gdpNigeria = gdp.iloc[1:34]
print(gdpNigeria)

gdp = df['South Africa [ZAF]']      # Pega todos dados de uma coluna e bota em uma variavel
gdpAfrica = gdp.iloc[1:34]
print(gdpAfrica)




time = df['Time']           # Pega todos dados da coluna ANO
anos = time.iloc[1:34]       # Exclui os dados que não são anos
print(anos)
print(anos.shape)

numeroElemntosLista = len(gdpBrazil)
somaValoresGdpBra = 0
somaValoresGdpIndo = 0
somaValoresGdpChi = 0
somaValoresGdpInd = 0
somaValoresGdpHon = 0
somaValoresGdpMex = 0
somaValoresGdpCol = 0
somaValoresGdpPer = 0
somaValoresGdpTur = 0
somaValoresGdpMar = 0
somaValoresGdpNig = 0
somaValoresGdpAfr = 0


somaValoresBra = []
somaValoresIndo = []
somaValoresChi = []
somaValoresInd = []
somaValoresHon = []
somaValoresMex = []
somaValoresCol = []
somaValoresPer = []
somaValoresTur = []
somaValoresMar = []
somaValoresNig = []
somaValoresAfr = []



for item in gdpBrazil:
    somaValoresGdpBra = somaValoresGdpBra + item
    somaValoresBra.append(somaValoresGdpBra)   # Append adiciona valor na lista

for item in gdpIndonesia:
    somaValoresGdpIndo = somaValoresGdpIndo + item
    somaValoresIndo.append(somaValoresGdpIndo)   # Append adiciona valor na lista

for item in gdpChina:
    somaValoresGdpChi = somaValoresGdpChi + item
    somaValoresChi.append(somaValoresGdpChi)   # Append adiciona valor na lista

for item in gdpIndia:
    somaValoresGdpInd = somaValoresGdpInd + item
    somaValoresInd.append(somaValoresGdpInd)   # Append adiciona valor na lista

for item in gdpHong:
    somaValoresGdpHon = somaValoresGdpHon + item
    somaValoresHon.append(somaValoresGdpHon)   # Append adiciona valor na lista

for item in gdpMexico:
    somaValoresGdpMex = somaValoresGdpMex + item
    somaValoresMex.append(somaValoresGdpMex)   # Append adiciona valor na lista

for item in gdpColombia:
    somaValoresGdpCol = somaValoresGdpCol + item
    somaValoresCol.append(somaValoresGdpCol)   # Append adiciona valor na lista

for item in gdpPeru:
    somaValoresGdpPer = somaValoresGdpPer + item
    somaValoresPer.append(somaValoresGdpPer)   # Append adiciona valor na lista

for item in gdpTurquia:
    somaValoresGdpTur = somaValoresGdpTur + item
    somaValoresTur.append(somaValoresGdpTur)   # Append adiciona valor na lista

for item in gdpMarroco:
    somaValoresGdpMar = somaValoresGdpMar + item
    somaValoresMar.append(somaValoresGdpMar)   # Append adiciona valor na lista

for item in gdpNigeria:
    somaValoresGdpNig = somaValoresGdpNig + item
    somaValoresNig.append(somaValoresGdpNig)   # Append adiciona valor na lista

for item in gdpAfrica:
    somaValoresGdpAfr = somaValoresGdpAfr + item
    somaValoresAfr.append(somaValoresGdpAfr)   # Append adiciona valor na lista

plt.plot(anos,somaValoresBra,'r--')
plt.plot(anos,somaValoresIndo,'b--')
plt.plot(anos,somaValoresChi,'y--')
plt.plot(anos,somaValoresInd,'g--')
plt.plot(anos,somaValoresHon,'r^')
plt.plot(anos,somaValoresMex,'b^')
plt.plot(anos,somaValoresCol,'y^')
plt.plot(anos,somaValoresPer,'g^')
plt.plot(anos,somaValoresTur,'bs')
plt.plot(anos,somaValoresMar,'ys')
plt.plot(anos,somaValoresNig,'gs')
plt.plot(anos,somaValoresAfr,'rs')


plt.legend(['Brazil [BRA]',
       'Indonesia [IDN]','China [CHN]', 'India [IND]', 'Hong Kong SAR, China [HKG]',
       'Mexico [MEX]', 'Colombia [COL]', 'Peru [PER]', 'Turkey [TUR]', 'Morocco [MAR]',
       'Nigeria [NGA]', 'South Africa [ZAF]'])

plt.title('GDP per capita growth x Years')
plt.grid(color='silver', linestyle='-', linewidth=0.5)
plt.xlabel('Years')
plt.ylabel('GDP per capita growth (%)')
plt.show()


