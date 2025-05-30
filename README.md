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
    Função Lambda que:
    - Lê `input` quer seja enviado direto (evento de teste) 
      ou via HTTP (Function URL/API Gateway).
    - Converte para maiúsculas.
    - Retorna JSON apropriado.
    """

    # Detecta payload HTTP vs. evento direto
    if "body" in event:
        # HTTP via Function URL ou API Gateway
        try:
            payload = event["body"]
            if isinstance(payload, str):
                data = json.loads(payload)
            else:
                data = payload
        except Exception:
            data = {}
    else:
        # Evento de teste no console
        data = event

    input_data = data.get("input", "")
    output_data = input_data.upper()

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"  # importante para navegadores/clients
        },
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
