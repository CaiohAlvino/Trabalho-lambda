# IMPORTANTE
Não funciona mais, foi excluido a lambda da AWS.
---
# Lambda API em Python

Este repositório contém uma função AWS Lambda escrita em Python, que atua como uma API muito simples:
- Recebe um JSON via evento com a chave `input`
- Retorna um JSON com a chave `output` com o texto em maiúsculas

## Evento de Exemplo
```json
{
  "input": "Hello, World!"
}
```

## Resposta Exemplo
```json
{
  "output": "HELLO, WORLD!"
}
```
---
## Estrutura do Projeto

```
Trabalho-lambda/
├── main.py
└── README.md
```
