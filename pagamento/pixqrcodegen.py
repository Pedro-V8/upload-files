import crcmod
import qrcode
import os


class Payload():
    def __init__(self , nome , chavepix , valor , cidade , txtid , title_conta):
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

        self.payloadFormat = '000201'
        self.merchantAccount = f'26{len(self.merchantAccount_tam)}{self.merchantAccount_tam}'

        if self.valor_tam <= 9:
            self.transactionAmount_tam = f'0{self.valor_tam}{self.valor}'
        else:
            self.transactionAmount_tam = f'{self.valor_tam}{self.valor}'

        if self.txtid_tam <= 9:
            self.addDataField_tam = f'050{self.txtid_tam}{self.txtid}'
        else:
            self.addDataField_tam = f'05{self.txtid_tam}{self.txtid}'

        if self.nome_tam <= 9:
            self.nome_tam = f'0{self.nome_tam}'

        if self.cidade_tam <= 9:
            self.cidade_tam = f'0{self.cidade_tam}'


        self.merchantCategCode = '52040000'
        self.transactionCurrency = '5303986'
        self.transactionAmount = f'54{self.transactionAmount_tam}'
        self.countryCode = '5802BR'
        self.merchantName = f'59{self.nome_tam}{self.nome}'
        self.merchantCity = f'60{self.cidade_tam}{self.cidade}'
        self.addDataField = f'62{len(self.addDataField_tam)}{self.addDataField_tam}'
        self.crc16 = '6304'

    def gerarPayload(self):
        self.payload = f'{self.payloadFormat}{self.merchantAccount}{self.merchantCategCode}{self.transactionCurrency}{self.transactionAmount}{self.countryCode}{self.merchantName}{self.merchantCity}{self.addDataField}{self.crc16}'

        print(self.payload)

        self.gerarCrc16(self.payload)
    
    def gerarCrc16(self , payload):
        crc16 = crcmod.mkCrcFun(poly=0x11021 , initCrc=0xFFFF , rev=False , xorOut=0x0000)

        self.crc16Code = hex(crc16(str(payload).encode('utf-8')))
        
        self.crc16Code_formatado = str(self.crc16Code).replace('0x','').upper()

        self.payload_completa = f'{payload}{self.crc16Code_formatado}'

        print()
        print(self.payload_completa)

        self.gerarQrCode(self.payload_completa)

    def gerarQrCode(self , payload):
        self.qrCode = qrcode.make(payload)
        self.qrCode.save(f"../media/pixQrCode/{self.title_conta}QrCode.png")
        print("--QR Code gerado com sucesso --")




    def print_variaveis(self):
        print()
        print(self.valor_tam)


if __name__ == '__main__':
    p = Payload('PedroHenrique' , 'ed600435-a47e-4c6f-840b-916e9f2b3e40' , '1.0' , 'Brasila' , 'FamiliaVieira') 

    p.gerarPayload()