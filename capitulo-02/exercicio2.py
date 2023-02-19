#1. O volume de uma esfera com raio r é (4/3.π.r³). Qual é o volume de uma esfera com raio 5?

pi = 3.14
raio = 5
def volume_esfera(pi,raio):
    total = (4*pi*(raio**3))/3
    print(f"O volume da esfera é de {total:.1f}")

#R: 0 volume da esfera é de 523.3

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#2. Suponha que o preço de capa de um livro seja R$ 24,95, mas as livrarias recebem um desconto de 40%. O transporte custa R$ 3,00 para o primeiro exemplar e 75 centavos
# para cada exemplar adicional. Qual é o custo total de atacado para 60 cópias?

quantidade = 60

def custo_atacado(quantidade):
    livro = 24.95
    desconto_livraria = 0.40
    transporte_primeiro_exemplar = 3
    transporte_apos_o_primeiro_exemplar = 0.75

    valor_transporte = transporte_primeiro_exemplar + (transporte_apos_o_primeiro_exemplar*(quantidade-1))
    total = (livro*desconto_livraria) + valor_transporte

    print(f"O custo total de atacado é de R${total:.2f}")

#R: O custo total de atacado é de R$57.23

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#3. Se eu sair da minha casa às 6:52 e correr 1 quilômetro a um certo passo (8min15s por quilômetro), então 3 quilômetros a um passo mais rápido (7min12s por quilômetro) e
# 1 quilômetro no mesmo passo usado em primeiro lugar, que horas chego em casa para o café da manhã?

HORA_SAIDA = 6.52
QUANTIDADE_KM_PASSO_NORMAL = 2
QUANTIDADE_KM_PASSO_RAPIDO = 3


def tempo_de_chegada(HORA_SAIDA,QUANTIDADE_KM_PASSO_NORMAL, QUANTIDADE_KM_PASSO_RAPIDO):
    VELOCIDADE_PASSO_NORMAL = 8.15 # KM/min
    VELOCIDADE_PASSO_RAPIDO = 7.12 # KM/min

    total_tempo_passos_normal = VELOCIDADE_PASSO_NORMAL*QUANTIDADE_KM_PASSO_NORMAL/60 # tempo em horas
    total_tempo_passos_rapido = VELOCIDADE_PASSO_RAPIDO*QUANTIDADE_KM_PASSO_RAPIDO/60 # tempo em horas

    total_tempo_de_chegada = HORA_SAIDA+total_tempo_passos_normal+total_tempo_passos_rapido

    print(f"O horário de chegada para o café da manhã foi {total_tempo_de_chegada:.2f}h")

#R: O horário de chegada para o café da manhã foi 7.20h
