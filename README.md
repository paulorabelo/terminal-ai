# 🐧 Terminal AI Assistant

Um assistente de linha de comando (CLI) inteligente para Linux, turbinado pela API do Google Gemini ou Gemma.

Transforme seu terminal em uma ferramenta capaz de diagnosticar erros, explicar comandos e analisar logs complexos usando Inteligência Artificial, tudo sem sair da tela preta.

![Terminal AI em ação](/gemini-3-flash.webp)
*(Ex: Saída com o novo Gemini 3 Flash (preview))*

![Terminal AI em ação](/ajuda.webp)
*(Ex: Uso com Gemma, erro por excesso de token e uso com Gemini 2.5 flash)*

## 🚀 Novidades da Versão 2.1

- **Novo Motor (SDK v1.0):** Código migrado para a nova biblioteca `google-genai` (Google Gen AI SDK), garantindo compatibilidade futura e maior performance.
- **Atualizador Automático:** Novo script `update.sh` para facilitar a vida de quem usa.

## 🚀 Novidades da Versão 2.01

- **Modo Híbrido Inteligente:**
  - 🛡️ **Padrão (Gemma 3):** Usa o modelo `gemma-3-27b-it` para alta disponibilidade (aprox. 14.000 requisições/dia). Ideal para tarefas rotineiras.
  - 🚀 **Modo PRO (Gemini 3-flash-preview):** Ative o modelo `gemini-3-flash-preview` para raciocínio complexo usando a flag `pro` ou `turbo`.
- **Contador de Cota Local:** Monitora seu uso diário do modo PRO para você não estourar o limite do plano gratuito.
- **Diagnóstico de Erros:** Detecta automaticamente se o input é grande demais e sugere o uso de filtros (`grep`, `head`).

---

## 🛠️ Instalação

### 1. Clone o repositório
Bash
```bash
git clone [https://github.com/paulorabelo/terminal-ai.git](https://github.com/paulorabelo/terminal-ai.git)
cd terminal-ai
```

### 2. Prepare o Ambiente Python

Recomendamos usar um ambiente virtual (`venv`) para isolar as dependências.

⚠️ **Usuários Ubuntu/Debian/Mint:** Instale o pacote venv antes:

Bash

```bash
sudo apt update && sudo apt install python3-venv -y
```

Crie e ative o ambiente:

Bash

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instale as dependências

Bash

```bash
pip install -r requirements.txt
```
---
🔄 Como Atualizar
Lançamos atualizações frequentes! Para atualizar seu assistente sem dor de cabeça (baixar código novo e atualizar bibliotecas automaticamente), basta rodar:

Bash
```bash
bash update.sh
```
(O script detecta se você precisa de novas bibliotecas e ajusta o ambiente virtual automaticamente).
---

## 🔐 Configuração (Uma única vez)

Para que o assistente funcione sempre, configure sua chave de API e o atalho no seu shell (`.bashrc` ou `.zshrc`).

1. **Obtenha sua Chave:** Crie uma API Key gratuita no [Google AI Studio](https://aistudio.google.com/).
    
2. **Edite seu arquivo de configuração:**
    
    Bash
    
    ```bash
    nano ~/.zshrc   # Se usa Zsh (padrão em muitas distros modernas)
    # OU
    nano ~/.bashrc  # Se usa Bash (padrão Ubuntu/Server)
    ```
    
3. **Adicione ao final do arquivo:**
    
    Bash
    
    ```bash
    # --- Configuração Terminal AI ---
    export GEMINI_API_KEY="SUA_CHAVE_AQUI_COLE_SEM_ASPAS_EXTRAS"
    alias ajuda='~/caminho/para/terminal-ai/venv/bin/python ~/caminho/para/terminal-ai/assistant.py'
    ```
    
4. **Recarregue:**
    
    Bash
    
    ```bash
    source ~/.zshrc  # ou source ~/.bashrc
    ```
    

---

## 🏃‍♂️ Como Usar

### Uso Básico (Modelo Gemma - "quase" Ilimitado 😂🙈)

Ótimo para perguntas rápidas e explicações simples.

Bash

```bash
ajuda "Como listo apenas pastas no Linux?"
```

### Uso PRO (Modelo Gemini 3-flash-preview - Mais Inteligente)

Use quando precisar de uma análise profunda. Consome sua cota diária limitada (aprox. 20 req/dia).

Bash

```bash
ajuda pro "Crie um script Python complexo para backup incremental"
# ou
ajuda turbo "Explique este erro de kernel panic"
```

### O Poder do Pipe (`|`)

Analise saídas de outros comandos diretamente.

**Analisar Logs de Erro:**

Bash

```bash
# O script detecta se o log for muito grande e avisa!
cat /var/log/syslog | grep "error" | ajuda "Qual a causa raiz?"
```

**Entender Processos:**

Bash

```bash
ps aux --sort=-%mem | head -n 5 | ajuda "Quem está consumindo minha memória?"
```

---

## 📊 Telemetria Local

O script cria um arquivo oculto `~/.gemini_usage.json` para contar quantas vezes você usou o modo PRO no dia, ajudando a gerenciar seus recursos gratuitos. 

---

## 🤝 Contribuições

Sinta-se livre para abrir Issues ou PRs. Projeto ideal para estudantes de Engenharia de Computação e entusiastas de DevOps.

---

Feito com 🐍 Python e 🤖 Google AI por [Paulo Rabelo](https://paulorabelo.dev.br/).
