import csv

filename = '/Users/aleksandrtimofeev/Desktop/learn_python/1201741.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    del header_row[0]
    print(header_row)

    for index, column_header in enumerate(header_row):
        print(index, column_header)


    device_type_id_create = []
    is_approve = []
    device_approve1 = []
    device_approve2 = []
    summa_device_approve1 = []
    summa_device_approve2 = []
    summa = ''
    for i in reader:
        device_type = int(i[7])
        device_type_id_create.append(device_type)
        approve = int(i[8])
        is_approve.append(approve)

    for j in range(len(device_type_id_create)):
        if device_type_id_create[j] == 1:
            device_approve1.append(1)
            if device_type_id_create[j] == 1 and is_approve[j] == 1:
                summa_device_approve1.append(1)
        elif device_type_id_create[j] == 2:
            device_approve2.append(1)
            if device_type_id_create[j] == 2 and is_approve[j] == 1:
                summa_device_approve2.append(1)
    summa = round(sum(is_approve) / sum(device_type_id_create) * 100, 2)
    print('Всего заявок на кредит:', sum(device_type_id_create))
    print('Всего одобренно заявок на кредит:', sum(is_approve))
    print('Процент одобренных заявок из общего числа заявок на кредит:', summa)
    print('Всего подано заявок с 1 дивайса:', sum(device_approve1))
    print('Всего одобрено заявок с 1 дивайса:', sum(summa_device_approve1), 'или', round(sum(summa_device_approve1) / sum(device_approve1) * 100, 2), '%')
    print('Всего подано заявок с 2 дивайса:', sum(device_approve2))
    print('Всего одобрено заявок с 2 дивайса:', sum(summa_device_approve2), 'или', round(sum(summa_device_approve2) / sum(device_approve2) * 100, 2), '%')