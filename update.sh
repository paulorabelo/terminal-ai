#!/bin/bash

echo "🔄 Iniciando atualização do Terminal AI..."

# 1. Baixa as novidades do GitHub
git pull

# 2. Verifica se o venv existe
if [ ! -d "venv" ]; then
    echo "⚠️  Ambiente virtual não encontrado. Criando um novo..."
    python3 -m venv venv
fi

# 3. Instala/Atualiza as dependências (Usando o pip DO VENV diretamente)
# O segredo é chamar ./venv/bin/pip em vez de apenas pip
echo "📦 Atualizando bibliotecas..."
./venv/bin/pip install -r requirements.txt

echo "✅ Tudo pronto! Seu assistente está atualizado."