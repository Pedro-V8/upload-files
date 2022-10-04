import crcmod
import qrcode


class Payload():
    def __init__(self , nome , chavepix , valor , cidade , txtid):
        self.nome = nome
        self.chavepix = chavepix
        self.valor = valor
        self.cidade = cidade
        self.txtid = txtid

        self.nome_tam = len(self.nome)
        self.chavepix_tam = len(self.chavepix)
        self.valor_tam = len(self.valor)
        self.cidade_tam = len(self.cidade)
        self.txtid_tam = len(self.txtid)

        self.merchantAccount_tam = f'0014BR.GOV.BCB.PIX01{self.chavepix_tam}{self.chavepix}'
        self.transactionAmount_tam = f'{self.valor_tam}{self.valor}'

        self.payloadFormat = '000201'
        self.merchantAccount = f'26{len(self.merchantAccount_tam)}{self.merchantAccount_tam}'
        self.merchantCategCode = '52040000'
        self.transactionCurrency = '5303986'
        self.transactionAmount = '54'
        self.countryCode = '5802BR'
        self.merchantName = '59'
        self.merchantCity = '60'
        self.addDataField = '62'
        self.crc16 = '6304'

    def print_variaveis(self):
        print(self.merchantAccount_tam)

if __name__ == '__main__':
    p = Payload('Pedro Henrique de Deus Vieira' , 'chave' , '1.00' , 'cidade' , 'FamiliaVieira') 

    p.print_variaveis()