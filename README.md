Automação para Scarface: The World is Yours

Este projeto é uma automação simples, desenvolvida em Python, para realizar ações repetitivas no menu do jogo Scarface: The World is Yours. A automação foi criada para facilitar o uso de cheats no jogo, automatizando alguns passos para ativar o cheat que preenche o BALLS necessário para trocar por dinheiro.
Descrição

A automação executa as seguintes ações:

Pressiona o botão Enter para abrir o menu principal do jogo.
Desce até a terceira opção do menu (CHEATS).
Pressiona a tecla K para selecionar CHEATS.
Desce até a segunda opção e seleciona novamente com K.
Após 1 segundo, pressiona a tecla I para ativar o cheat.
Esse processo é repetido em um loop até ser interrompido manualmente.
Como Funciona

Este código é relativamente simples e fácil de entender. Ele foi feito com a intenção de ser acessível a programadores iniciantes em Python. A lógica básica envolve o envio de comandos de teclado para o emulador PCSX2 com o uso da biblioteca PyAutoGUI.
Etapas Simples:

Instalar as Bibliotecas Necessárias:
O código utiliza apenas a biblioteca PyAutoGUI, que pode ser instalada facilmente com um simples comando pip.

Execução do Código:
A automação funciona enviando comandos de teclado (como Enter, K, I, etc.) para a janela do jogo, simulando as ações que o jogador faria manualmente.

Repetição Automática:
O código irá repetir o processo de ativação do cheat em loop até ser interrompido.
Bibliotecas Necessárias

Este código foi desenvolvido usando Python 3.13.2 e utiliza a seguinte biblioteca:

PyAutoGUI: Para simular os movimentos e cliques do teclado e mouse. Esta é a principal biblioteca responsável pela automação das ações no emulador PCSX2.
Comando para Instalar as Bibliotecas

Para instalar as bibliotecas necessárias, execute o seguinte comando:

pip install pyautogui

Caso ainda não tenha o pip instalado, você pode seguir as instruções de instalação do pip para a versão do Python que está utilizando: https://pip.pypa.io/en/stable/installation/
Habilitar a Jogabilidade com Teclado

Para que a automação funcione corretamente, o código foi desenvolvido para funcionar com jogabilidade via teclado. A automação não foi projetada para controle de Xbox.
Posicionar Tony Montana

Tony Montana precisa estar posicionado em frente ao trailer, localizado em um beco em Little Havana. A automação só irá funcionar se Tony estiver nesse local.

https://i.imgur.com/QNgwGlb.png

Em seguida, a automação entra no menu do jogo, seleciona a opção CHEATS e ativa o cheat FPATCH, que preenche o BALLS necessário para trocá-los por dinheiro no jogo.

https://i.imgur.com/0BawhlT.png

https://i.imgur.com/fHsyzbm.png

Cheats para Scarface: The World is Yours

    MEDIK: Restaura a saúde de Tony Montana.
    FPATCH: Concede 1.000 balas de precisão.
    AMMO: Restaura a munição de todas as armas.
    GOBALLS: Aumenta o nível de atividade da gangue (gang heat).
    NOBALLS: Diminui o nível de atividade da gangue.
    DONUT: Aumenta o nível de atenção policial (cop heat).
    FLYSTRT: Diminui o nível de atenção policial.
    MARTHA: Altera a hora do dia.
    RAINY: Ativa condições climáticas de chuva.
    SHAZAAM: Ativa efeitos climáticos de raios.
    BLACK: Altera o traje de Tony para uma roupa preta.
    WHITE: Altera o traje de Tony para uma roupa branca.
    GREY: Altera o traje de Tony para uma roupa cinza.
    TANSHRT: Altera o traje de Tony para uma camisa bege.
    TIGSHRT: Altera o traje de Tony para uma camisa de tigre.
    BLUESH: Altera o traje de Tony para um terno azul com óculos escuros.
    WHITESH: Altera o traje de Tony para um terno branco com óculos escuros.
    TBURGLR: Repara o veículo atual.
    OLDFAST: Altera o veículo atual para um modelo mais antigo.
    S13: Desbloqueia a missão "Babylon Club Redux".
    DW_FRON: Desbloqueia a missão "The Front".
    S12: Desbloqueia a missão "The Exchange".
    S07A: Desbloqueia a missão "The Chase".

Como Rodar o Código

Para executar o código, certifique-se de estar na pasta onde o arquivo .py está localizado. Caso contrário, o comando não funcionará.

Exemplo:

Abra o Prompt de Comando ou Terminal.

 Navegue até a pasta onde o código está salvo usando o comando cd:
```bash
cd caminho/para/a/pasta
```
Execute o código com o comando:
```bash
    python nome_do_arquivo.py
```