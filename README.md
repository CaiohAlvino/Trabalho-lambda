## Estrutura do Projeto

```
lambda_api_python/
├── lambda_function.py
└── README.md
```

---

### 1. `lambda_function.py`
```python
import json

def lambda_handler(event, context):
    """
    Função Lambda simples que recebe um JSON com chave "input"
    e retorna um JSON com chave "output".
    Exemplo de evento de entrada:
    {
        "input": "Olá, Lambda!"
    }
    """
    # Obtém o dado de entrada
    input_data = event.get("input", "")

    # Processamento: converte para maiúsculas
    output_data = input_data.upper()

    # Formata a resposta como API
    return {
        "statusCode": 200,
        "body": json.dumps({"output": output_data})
    }
```

---

### 2. `requirements.txt`
```text
# Nenhuma dependência externa além do SDK da AWS
# Se precisar de pacotes extras, liste aqui
```

---

### 3. `README.md`
```markdown
# Lambda API em Python

Este repositório contém uma função AWS Lambda escrita em Python, que atua como uma API muito simples:
- Recebe um JSON via evento com a chave `input`
- Retorna um JSON com a chave `output` com o texto em maiúsculas

## Como implantar

1. Faça login na AWS CLI:
   ```bash
   aws configure
   ```
2. Empacote o código:
   ```bash
   zip function.zip lambda_function.py
   ```
3. Crie ou atualize a função Lambda:
   ```bash
   aws lambda create-function \
     --function-name LambdaAPI \
     --runtime python3.9 \
     --handler lambda_function.lambda_handler \
     --zip-file fileb://function.zip \
     --role arn:aws:iam::123456789012:role/SeuRoleLambda
   # ou, se já existir:
   aws lambda update-function-code \
     --function-name LambdaAPI \
     --zip-file fileb://function.zip
   ```
4. Teste localmente via AWS CLI:
   ```bash
   aws lambda invoke \
     --function-name LambdaAPI \
     --payload '{"input":"Teste"}' \
     response.json
   cat response.json
   ```

## Evento de Exemplo
```json
{
  "input": "Hello, World!"
}
```

## Resposta Exemplo
```json
{
  "statusCode": 200,
  "body": "{\"output\": \"HELLO, WORLD!\"}"
}
```
