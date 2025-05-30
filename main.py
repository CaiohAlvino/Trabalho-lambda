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
