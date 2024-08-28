import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox

# Conectar ao banco de dados SQLite (ou criar se não existir)
conexao = sqlite3.connect('corridas.db')
cursor = conexao.cursor()

# Criar a tabela para armazenar as corridas (se não existir)
cursor.execute('''
CREATE TABLE IF NOT EXISTS corridas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    distancia REAL,
    tempo REAL,
    bandeira INTEGER,
    valor REAL
)
''')
conexao.commit()

class JanelaPrincipal(QWidget):
    def __init__(self):
        super().__init__()

        # Configuração da janela principal
        self.setWindowTitle("Cálculo de Corrida de Táxi")

        # Layout Vertical
        layout = QVBoxLayout()

        # Labels e Entradas
        self.label_distancia = QLabel("Distância (km):")
        layout.addWidget(self.label_distancia)

        self.entry_distancia = QLineEdit()  
        layout.addWidget(self.entry_distancia)

        self.label_tempo = QLabel("Tempo (minutos):")
        layout.addWidget(self.label_tempo)

        self.entry_tempo = QLineEdit() 
        layout.addWidget(self.entry_tempo)

        self.label_bandeira = QLabel("Bandeira (1 ou 2):")
        layout.addWidget(self.label_bandeira)

        self.entry_bandeira = QLineEdit()  
        layout.addWidget(self.entry_bandeira)

        # Botão para calcular
        self.botao_calcular = QPushButton("Calcular")
        self.botao_calcular.clicked.connect(self.calcular_corrida)
        layout.addWidget(self.botao_calcular)

        # Label para mostrar o resultado
        self.label_resultado = QLabel("")
        layout.addWidget(self.label_resultado)

        # Label para mostrar o total das últimas 10 corridas
        self.label_total_corridas = QLabel("Total das últimas 10 corridas: R$ 0.00")
        layout.addWidget(self.label_total_corridas)

        # Definir o layout na janela principal
        self.setLayout(layout)

    def calcular_corrida(self):
        try:
            distancia_km = float(self.entry_distancia.text())
            tempo_minutos = float(self.entry_tempo.text())
            bandeira = int(self.entry_bandeira.text())

            taxa_fixa = 6.00
            tarifa_km_bandeira1 = 4.25
            tarifa_horaria = 51.00  # Tarifa de 51 reais por hora
            tarifa_km_bandeira2 = tarifa_km_bandeira1 * 1.30
            
            # Cálculo da tarifa horária proporcional
            custo_tempo = (tempo_minutos / 60) * tarifa_horaria

            if bandeira == 1:
                custo_km = tarifa_km_bandeira1 * distancia_km
            elif bandeira == 2:
                custo_km = tarifa_km_bandeira2 * distancia_km
            else:
                QMessageBox.critical(self, "Erro", "Bandeira inválida! Escolha 1 ou 2.")
                return

            valor_total = taxa_fixa + custo_km + custo_tempo
            self.label_resultado.setText(f"O valor da corrida é: R$ {valor_total:.2f}")

            # Inserir a corrida no banco de dados
            cursor.execute('''
            INSERT INTO corridas (distancia, tempo, bandeira, valor)
            VALUES (?, ?, ?, ?)
            ''', (distancia_km, tempo_minutos, bandeira, valor_total))
            conexao.commit()

            # Limitar a 10 últimas corridas
            cursor.execute('DELETE FROM corridas WHERE id NOT IN (SELECT id FROM corridas ORDER BY id DESC LIMIT 10)')
            conexao.commit()

            # Calcular o total das últimas 10 corridas
            cursor.execute('SELECT SUM(valor) FROM corridas')
            total_corridas = cursor.fetchone()[0]
            self.label_total_corridas.setText(f"Total das últimas 10 corridas: R$ {total_corridas:.2f}")

        except ValueError:
            QMessageBox.critical(self, "Erro", "Por favor, insira valores válidos.")

# Execução da Aplicação PyQt5
app = QApplication(sys.argv)
janela = JanelaPrincipal()
janela.show()
sys.exit(app.exec_())

# Fechar a conexão com o banco de dados quando o programa terminar
conexao.close()
