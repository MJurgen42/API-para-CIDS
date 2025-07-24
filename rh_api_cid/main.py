from fastapi import FastAPI

app = FastAPI()  # Esta variável DEVE se chamar 'app'

# Rota raiz OBRIGATÓRIA
@app.get("/")
def home():
    return {"message": "API de RH - Validação de CIDs"}

# Rota de exemplo para atestados
@app.get("/atestados/")
def listar_atestados():
    return {"dados": "Lista de atestados virá aqui"}