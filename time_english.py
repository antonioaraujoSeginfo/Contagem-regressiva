import time

tempo_em_struct = time.localtime()
tempo_formatado = time.strftime("%A, %d de %B de %Y, %H:%M", tempo_em_struct)

print(f"Data e hora atuais: {tempo_formatado}")

