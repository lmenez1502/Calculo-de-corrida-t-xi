#Definição das variaveis

taxa_fixa = 6.00
tarifa_km_bandeira1 = 4.25
tarifa_minuto_bandeira1 = 0.25

#Bandeira 2 é 30% mais cara

tarifa_km_bandeira2 = tarifa_km_bandeira1 * 1.30
tarifa_km_bandeira2 = tarifa_km_bandeira1 * 1.30

#Entrada de dados do usuário

distancia_km = float(input("Digite a distância percorrida em quilômetros: "))
tempo_minutos = float(input("Digite o tempo gasto na corrida em minutos: "))
bandeira = int(input("Digite a bandeira (1 ou 2): "))

# calculo do valor da corrida

if bandeira == 1:
    custo_km = tarifa_km_bandeira1 * distancia_km
    custo_minutos = tarifa_km_bandeira1 * distancia_km
elif bandeira == 2:
    custo_km = tarifa_km_bandeira2 * distancia_km
    custo_minutos = tarifa_km_bandeira2 * tempo_minutos
else:
    print("Bandeira Inválida! Por favor, escolha 1 ou 2.")
    exit()

# valor total da corrida
valor_total = taxa_fixa + custo_km + custo_minutos

print(f"O valor da corrida é: R$ {valor_total:.2f}")