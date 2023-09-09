# Tech Condomínio - Email API

Este projeto é a entrega do MVP da disciplina Arquitetura de Software do curso de pós-graduação de Engenharia de Software na PUC RIO

---

## Requisitos para utilizar a aplicação ##

Por segurança, é necessário adicionar a senha de aplicativos do gmail nas variáveis de ambiente com o seguinte valor:

```
TECH_CONDOMINIO_MAIL_PASSWORD
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
docker run -d -p 8000:8000 --name container-c componente-c:latest
```
