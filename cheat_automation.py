import pydirectinput  # Biblioteca para simular entradas de teclado
import time  # Biblioteca para adicionar delays entre os comandos
import pygetwindow as gw  # Biblioteca para interagir com janelas abertas

# Função para focar e maximizar a janela do jogo (PCSX2)
def focar_janela_pcsx2():
    try:
        # Encontra a janela do PCSX2 pelo nome
        janela = gw.getWindowsWithTitle("Scarface - The World is Yours")[0]
        janela.activate()  # Ativa a janela (traz a janela para frente)
        janela.maximize()  # Maximiza a janela
        time.sleep(1)  # Espera 1 segundo para garantir que a janela está ativa
    except IndexError:
        print("Não foi possível encontrar a janela do PCSX2!")
        exit()  # Se não encontrar a janela, sai do programa

# Função para executar os comandos do cheat
def ativar_cheat():
    # Focar na janela do PCSX2 antes de enviar os comandos
    focar_janela_pcsx2()

    # Pressiona Enter (Start) e espera 3 segundos
    pydirectinput.press('enter')  # Simula a tecla Enter (equivalente ao Start no controle)
    time.sleep(3)  # Espera 3 segundos para garantir que o menu foi aberto

    # Pressiona para baixo duas vezes para chegar em "CHEATS"
    pydirectinput.press('down')  # Desce uma vez
    time.sleep(0.3)  # Espera um pouco para garantir que o comando foi executado
    pydirectinput.press('down')  # Desce outra vez para a opção "CHEATS"
    time.sleep(0.3)  # Espera um pouco para garantir que o comando foi executado

    # Pressiona 'K' para selecionar "CHEATS"
    pydirectinput.press('k')  
    time.sleep(0.3)  # Espera um pouco para garantir que o comando foi executado

    # Desce mais uma vez para a opção "GILL BALLS METER"
    pydirectinput.press('down')  
    time.sleep(0.3)  # Espera um pouco para garantir que o comando foi executado

    # Pressiona 'K' novamente para confirmar a seleção de "GILL BALLS METER"
    pydirectinput.press('k')
    time.sleep(1)  # Espera 1 segundo para garantir que a ação foi registrada

    # Pressiona 'I' para ativar o cheat
    pydirectinput.press('i')
    time.sleep(1)  # Aguarda 1 segundo após ativar o cheat

# Repetir o processo indefinidamente
while True:
    ativar_cheat()  # Executa a função de ativar o cheat
    time.sleep(2)  # Tempo entre ativações (2 segundos)
