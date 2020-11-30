def get_clients():
    with open("./data/clients.txt") as clients_file:
        from_file = clients_file.readlines()

    clients_list = []
    for line in from_file:
        line_list = line.split(';')
        clients_list.append(line_list)

    return clients_list
def get_orders():
    with open('./data/orders.txt') as orders_file:
        from_file = orders_file.readlines()

    
    # розбити строку на реквізити та перетворити формати (при потребі)
    
    # список-накопичувач
    orders_list = []    
    
    for line in from_file:
        line_list = line.split(';')
        line_list[3] = int(line_list[3])
        line_list[4] = int(line_list[4])
        orders_list.append(line_list)

    return orders_list  

def show_clients(clients):
    # задати інтервал виводу
    client_code_from = input("З якого клієнта? ")
    client_code_to   = input("По який клієнта? ")

    lines_found = 0

    for client in clients:
        if client_code_from <= client[0] <= client_code_to:
            print ("клієнт: {:5} номер: {:15} код товара: {:25} кількість: {40}".format(*client))
            lines_found += 1

    if lines_found == 0:
        print("Клієнтів по Вашому запиту не знайдено")  

def show_orders(orders):
    for order in orders:
        print("код товару: {:3} найменування товару {:4} ціна: {:20} "
            .format(order[0], order[1], order[2],))