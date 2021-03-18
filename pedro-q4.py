from datetime import datetime

# Recebendo input do usuário (como string)
input_data_um = input('Data1:')
input_data_dois = input('Data2:')

# Convertendo input para datetime.datetime
data_um = datetime.strptime(input_data_um, "%d/%m/%y")
data_dois = datetime.strptime(input_data_dois, "%d/%m/%y")


if (data_um>data_dois):
    print('Data 1 maior que Data 2')
else:
    print('Data 2 maior que Data 1')
