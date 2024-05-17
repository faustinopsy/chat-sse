# Chat em Tempo Real com PHP e FastAPI
Este projeto implementa um sistema de chat em tempo real utilizando PHP e FastAPI. Ele inclui a integração do padrão Observer com Server-Sent Events (SSE) para notificação em tempo real e permite a interação com um banco de dados compartilhado entre as duas tecnologias.

## Tecnologias Utilizadas
- PHP
- FastAPI (Python)
- Server-Sent Events (SSE)
- MySQL (ou outro banco de dados relacional)
- JavaScript
## Estrutura do Projeto
```
/appphp
    /src
        Chat.php
        Database.php
    send_message.php
    sse.php
/apppython
    /app
        main.py
        routes/
            message_routes.py
        models/
            message.py
        database/
            database.py
    requirements.txt
```
## Padrão Observer e Server-Sent Events
- Padrão Observer
O padrão Observer é um padrão de design comportamental que define uma dependência um-para-muitos entre objetos, permitindo que quando um objeto muda de estado, todos os seus dependentes sejam notificados e atualizados automaticamente. Neste projeto, usamos o padrão Observer para notificar os usuários do chat sobre novas mensagens.

- Server-Sent Events (SSE)
SSE é uma tecnologia que permite que o servidor envie atualizações automáticas para o navegador. Utilizamos SSE para implementar a comunicação em tempo real entre o servidor e o cliente, enviando mensagens do servidor para o navegador assim que elas são adicionadas ao banco de dados.
https://developer.mozilla.org/pt-BR/docs/Web/API/Server-sent_events/Using_server-sent_events
## Configuração do Projeto
- Configuração do PHP
Instalação das Dependências
Certifique-se de ter o Composer instalado e execute:

```
composer install
```
Configuração do Banco de Dados
Crie o banco de dados e a tabela de mensagens:

```
CREATE TABLE messages (
    id INT AUTO_INCREMENT PRIMARY KEY,
    message TEXT NOT NULL,
    usuario VARCHAR(50) NOT NULL
);

```
## executar o servidor python
na pasta do projeto
```
pip install -r requeriments.txt

python main.py

````
