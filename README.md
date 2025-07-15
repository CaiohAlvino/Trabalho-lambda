# IMPORTANT
This project is no longer functional as the AWS Lambda function has been deleted.

---

# Simple Lambda API in Python

This repository was created as a college project to demonstrate skills in connecting to and manipulating AWS resources using Python. It contains an AWS Lambda function that acts as a very simple API:
- Receives a JSON event with the key `input`
- Returns a JSON with the key `output` containing the uppercase version of the input text

## Example Event
```json
{
  "input": "Hello, World!"
}
```

## Example Response
```json
{
  "output": "HELLO, WORLD!"
}
```

---

## Project Structure

```
Trabalho-lambda/
├── 📄 main.py
└── 📚 README.md
```
