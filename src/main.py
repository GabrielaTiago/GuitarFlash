from modules.pre_game import navega_para_site, clica_no_botao_jogar, seleciona_musica, desce_tela
from modules.temporizadores import aguarda_carregamento_rapido, aguarda_carregamento_medio

# Realiza a sequência de ações antes de iniciar o jogo (Navegação e seleção da música)
navega_para_site()

aguarda_carregamento_medio()

clica_no_botao_jogar()

aguarda_carregamento_rapido()

seleciona_musica()

aguarda_carregamento_rapido()

desce_tela()

aguarda_carregamento_medio()