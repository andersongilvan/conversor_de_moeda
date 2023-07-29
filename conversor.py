# Faça um programa que pergunte ao usuário quanto ele tem na carteira R$ e conver em dólar e depois em euros #

din = float(input("Quanto você tem em reais na carteira? "))

dolar = din / 4.72
print ('Com R${:.2f} você pode comprar U$ {:.2f}'.format(din, dolar))


euros = din / 5.37

print ('Com R${:.2f} você pode comprar £ {:.2f}'.format(din, euros))
