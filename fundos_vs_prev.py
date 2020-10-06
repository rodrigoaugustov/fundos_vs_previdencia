def comecotas(capital,prazo,taxaAno):
    taxaMes = ((1+taxaAno/100)**(1/12))-1
    juros = 0
    jurosAcumulado = 0
    for i in range(1,prazo+1):
        if i % 6 != 0:
            juros = (taxaMes * capital)
            capital += juros
            jurosAcumulado += juros
        else:
            juros = (taxaMes * capital)
            jurosAcumulado += juros
            capital = capital + juros - (jurosAcumulado * 0.15)
            jurosAcumulado = 0
    return capital

def previdencia(capital,prazo,taxaAno):
    taxaMes = ((1+taxaAno/100)**(1/12))-1
    juros = 0
    capital_inicial = capital
    for i in range(1,prazo+1):
        juros = (taxaMes * capital)
        capital += juros
    if prazo < 24:
        capital = (capital - capital_inicial) * 0.65 + capital_inicial
    elif prazo < 48:
        capital = (capital - capital_inicial) * 0.7 + capital_inicial
    elif prazo < 72:
        capital = (capital - capital_inicial) * 0.75 + capital_inicial
    elif prazo < 96:
        capital = (capital - capital_inicial) * 0.80 + capital_inicial
    elif prazo < 120:
        capital = (capital - capital_inicial) * 0.85 + capital_inicial
    else:
        capital = (capital - capital_inicial) * 0.90 + capital_inicial

    return capital

def compara(capital, prazo,taxaAno):
    rendimentos = [comecotas(capital, prazo,taxaAno)-capital,previdencia(capital, prazo,taxaAno)-capital]
    rendimentoMesFundos = (((1+((rendimentos[0] - capital)/capital))**(1/prazo))-1)*100
    rendimentoMesPrevi = (((1+((rendimentos[1] - capital)/capital))**(1/prazo))-1)*100
    vantagem = 0

    print("O rendimento líquido total do Fundo seria de R$",round(rendimentos[0],2))
    print("O rendimento líquido total da Previdência seria de R$",round(rendimentos[1],2))
    if rendimentoMesFundos > rendimentoMesPrevi:
        vantagem = (((rendimentos[0]) / (rendimentos[1]))-1)*100
        print("Esse investimento teria um rendimento",round(vantagem,2),"% maior no fundo")
    else:
        vantagem = (((rendimentos[1]) / (rendimentos[0]))-1)*100
        print("Esse investimento teria um rendimento",round(vantagem,2),"% maior na previdência")

capital = float(input("Digite o valor do capital a ser aplicado: R$ "))
prazo = int(input("Digite o prazo da aplicação em meses: "))
taxaAno = float(input("Digite o rendimento médio anual: "))

compara(capital,prazo,taxaAno)

def main():
    capital = float(input("Digite o valor do capital a ser aplicado: R$ "))
    prazo = int(input("Digite o prazo da aplicação em meses: "))
    taxaAno = float(input("Digite o rendimento médio anual: "))

    compara(capital,prazo,taxaAno)
