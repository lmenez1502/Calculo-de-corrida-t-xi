import tkinter as tk
from tkinter import messagebox

# Função para calcular o valor da corrida
def calcular_corrida():
    try:
        distancia_km = float(entry_distancia.get())
        tempo_minutos = float(entry_tempo.get())
        bandeira = int(entry_bandeira.get())
        
        taxa_fixa = 6.00
        tarifa_km_bandeira1 = 4.20
        tarifa_minuto_bandeira1 = 0.25
        tarifa_km_bandeira2 = tarifa_km_bandeira1 * 1.30
        tarifa_minuto_bandeira2 = tarifa_minuto_bandeira1 * 1.30
        
        if bandeira == 1:
            custo_km = tarifa_km_bandeira1 * distancia_km
            custo_minutos = tarifa_minuto_bandeira1 * tempo_minutos
        elif bandeira == 2:
            custo_km = tarifa_km_bandeira2 * distancia_km
            custo_minutos = tarifa_minuto_bandeira2 * tempo_minutos
        else:
            messagebox.showerror("Erro", "Bandeira inválida! Escolha 1 ou 2.")
            return
        
        valor_total = taxa_fixa + custo_km + custo_minutos
        label_resultado.config(text=f"O valor total da corrida é: R$ {valor_total:.2f}")
    
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores válidos.")

# Configuração da janela principal
janela = tk.Tk()
janela.title("Cálculo de Corrida de Táxi")

# Labels e Entradas
label_distancia = tk.Label(janela, text="Distância (km):")
label_distancia.pack()

entry_distancia = tk.Entry(janela)
entry_distancia.pack()

label_tempo = tk.Label(janela, text="Tempo (minutos):")
label_tempo.pack()

entry_tempo = tk.Entry(janela)
entry_tempo.pack()

label_bandeira = tk.Label(janela, text="Bandeira (1 ou 2):")
label_bandeira.pack()

entry_bandeira = tk.Entry(janela)
entry_bandeira.pack()

# Botão para calcular
botao_calcular = tk.Button(janela, text="Calcular", command=calcular_corrida)
botao_calcular.pack()

# Label para mostrar o resultado
label_resultado = tk.Label(janela, text="")
label_resultado.pack()

# Executar a interface gráfica
janela.mainloop()
