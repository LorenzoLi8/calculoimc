print('-CALCULADORA DE IMC-')
altura = float(input('Digite sua altura: '))
peso = float(input('Digite seu peso: '))
imc = float(peso/(altura**2))   
if imc < 18.5:
    print('Você está abaixo do peso, seu IMC é de {:.2f}'.format(imc))
elif imc < 25.0:
  print('Você está com o peso normal, seu IMC é de {:.2f}'.format(imc))
elif imc < 30.0:
  print('Você tem sobre-peso, seu IMC é de {:.2f}'.format(imc))
else:
    print('Você tem Obesidade, seu IMC é de {:.2f}'.format(imc))
