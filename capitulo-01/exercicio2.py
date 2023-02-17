# Exercícios realizados no modo interativo

#1. Quantos segundos há em 42 minutos e 42 segundos? (sabendo que 1 minuto contém 60 segundos)

MINUTOS = 42
SEGUNDOS = 42
totalDeSegundos = (SEGUNDOS*MINUTOS) + 42
print(totalDeSegundos, 'segundos')

#R: 2562 segundos

#----------------------------------------------------------------------------------------------------------------

#2. Quantas milhas há em 10 quilômetros? Dica: uma milha equivale a 1,61 quilômetro.

MILHA = 1.61
QUILOMETROS = 10
totalDeMilhas = QUILOMETROS/MILHA
print(totalDeSegundos, 'milhas')
#R: 6.211180124223602 milhas

#----------------------------------------------------------------------------------------------------------------

#3. Se você correr 10 quilômetros em 42 minutos e 42 segundos, qual é o seu passo médio (tempo por milha em minutos e segundos)? Qual é a sua velocidade média em milhas por hora?

MINUTOS = 42
SEGUNDOS = 0.42
QUILOMETROS = 10
MILHA = 1.61

MILHAS = QUILOMETROS/MILHA
totalDeMinutos = MINUTOS+SEGUNDOS
passoMedio = (totalDeMinutos/MILHAS)
print('O passo médio é {:.2f}min/m'.format(passoMedio))
# O passo médio é 6.83min/m

horas = totalDeMinutos/60
velocidadeMedia = MILHAS/horas
print('A velocidade média é {:.2f}m/h'.format(velocidadeMedia))
# A velocidade média é 8.79m/h
