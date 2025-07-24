# 📋 API de RH - Validação de Atestados Médicos (CID)

Esta API é um modelo simples para **gestão de RH**, permitindo validar e registrar atestados médicos com **CID (Código Internacional de Doenças)**. Ideal para integrar em sistemas de folha de pagamento ou aplicativos de gestão de funcionários.

## ✨ Funcionalidades
- ✅ **Validação automática de CIDs** (base oficial da OMS)
- 📅 Registro de atestados (funcionário, data, CID, observação)
- 🔍 Consulta por funcionário ou CID
- 🚀 **Pronta para produção** (FastAPI + Uvicorn)

## 🛠️ Como Usar
1. **Instale as dependências**:
   ```bash
   pip install -r requirements.txt

uvicorn main:app --reload

Swagger UI: http://localhost:8000/docs

Redoc: http://localhost:8000/redoc

Testes: Render.com (free)

Produção: AWS Lightsail ou Docker + VPS