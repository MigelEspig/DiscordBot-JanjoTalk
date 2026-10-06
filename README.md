# BEM-VINDO À JANJOTALK

Bot destinado à transmitir audio do pc do usuário. Com o propósito de repor a função de transmitir tela com áudio.

## FUNÇÕES EXISTENTES:

 - `~odiar` = JanjoTALK retorna a mensagem: "Obrigado, {User}, por odiar a deturpadora da paz";
 - `~entrar` = Entra na chamada de voz que o remetente está;
 - `~sair` = Sai na chamada de voz que JanjoTALK está;
 - `~falar` = com o input do remetente, JanjoTALK "fala" através da narração do Google translate (biblioteca gTTS)

## EVENTOS EXISTENTES:

- `on_ready` = Retorna uma mensagem no terminal avisando que o bot ligou;
- `on_message` = Evento aletório de 5% de, a cada mensagem, JanjoTALK pode retornar uma frase ofendendo o remetente;

### REQUISITOS PARA RODAR:

Realizar instalação das bibliotecas:

- FFmpeg ('winget install Gyan.FFmpeg')
- PyNaCl ('pip intall PyNaCl')
- davey ('pip install davey')