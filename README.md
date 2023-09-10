# Tech Condomínio - Email API

Este projeto é a entrega do MVP da disciplina Arquitetura de Software do curso de pós-graduação de Engenharia de Software na PUC RIO

---

## Requisitos para utilizar a aplicação ##

Por segurança, é necessário adicionar o email e senha de aplicativos do gmail nas variáveis de ambiente com o seguinte valor:

Email:

```
Nome: TECH_CONDOMINIO_MAIL
Valor: endereço de email
```

Senha:

```
Nome: TECH_CONDOMINIO_MAIL_PASSWORD
Valor: senha de app do email
```

Também é preciso criar um arquivo de nome .env caso essa aplicação seja dockerizada.

O arquivo deverá conter as duas variáveis previamente adicionadas às variáveis de ambiente do sistema:

```
TECH_CONDOMINIO_MAIL=endereço_de_email
TECH_CONDOMINIO_MAIL_PASSWORD=senha_de_app_do_email
```

Dessa forma a senha não fica visível no código.

## Dockerização da aplicação

Faça o download e instale o Docker Desktop na versão mais recente e compatível com seu PC.

Crie uma imagem para essa aplicação rodando o seguinte comando, chamaremos esta imagem de componente-a:

```
docker build -t componente-c:latest .
```

Depois da imagem criada, iniciaremos o container com o seguinte comando:

```
docker run --env-file .env -d -p 8000:8000 --name container-c componente-c:latest
```

Note que estamos passando o arquivo .env criado contendo o email e senha do remetente.