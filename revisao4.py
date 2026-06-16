trafego_servico = {}

logs_rede = [
    "LOG_01//HTTP//2500000",
    "LOG_02//FTP//1200000",
    "LOG_03//HTTP//4300000",
    "LOG_04//SSH//500000",
    "LOG_05//FTP//800000",
    "LOG_06//DATABASE//9500000",  # Olha um serviço novo aqui!
]

for log in logs_rede:
    id_log, servico, bytes_texto = log.split("//")
    bytes_decimal = float(bytes_texto) / 1000000
    trafego_servico[servico] = trafego_servico.get(servico, 0.0) + bytes_decimal

for servico, total in trafego_servico.items():
    print(f"Serviço: {servico} | Total MegaBytes: {total:.2f}")
