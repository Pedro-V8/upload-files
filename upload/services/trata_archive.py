def retorna_data(transacao):
    transacao_str = str(transacao).split(',')
    date = transacao_str[7][0:10]
    return date
