# 🐧 Terminal AI Assistant

Um assistente de linha de comando (CLI) inteligente para Linux, turbinado pela API do Google Gemini e Gemma.

Transforme seu terminal em uma ferramenta capaz de diagnosticar erros, explicar comandos e analisar logs complexos usando Inteligência Artificial, tudo sem sair da tela preta.

![Terminal AI em ação](/gemini-3-flash.webp)
*(Ex: Saída com o Gemini Flash)*

![Terminal AI em ação](/ajuda.webp)
*(Ex: Uso com Gemma, tratamento de erro por excesso de token)*

## 🚀 Novidades da Versão 2.2

- **Resiliência com Fallback Automático (Graceful Degradation):** Se a infraestrutura do Google passar por instabilidades ou picos de demanda (Erros 500 ou 503), o assistente intercepta a falha e aciona silenciosamente um modelo de backup ultra-estável, garantindo que você nunca fique sem resposta.
- **Novo Motor (SDK v1.0):** Código migrado para a nova biblioteca `google-genai` (Google Gen AI SDK), garantindo compatibilidade futura e maior performance.
- **Atualizador Automático:** Script `update.sh` integrado para baixar novidades e gerenciar dependências com um único comando.

## 🧠 Modo Híbrido Inteligente

- 🛡️ **Padrão (Gemma 4):** Usa o avançado modelo `gemma-4-31b-it`. Capacidade gigantesca de leitura (TPM ilimitado), ideal para analisar logs massivos de uma só vez, com limite de 1.500 requisições/dia.
- 🚀 **Modo PRO (Gemini 3.1 Flash Lite):** Ative o modelo `gemini-3.1-flash-lite` para raciocínio analítico complexo usando a flag `pro` ou `turbo`. Limitado a aprox. 20 requisições/dia.
- 📉 **Controle de Cota Local:** Monitora seu uso diário do modo PRO no próprio terminal para evitar o bloqueio do plano gratuito.

---

## 🛠️ Instalação

### 1. Clone o repositório
```bash
git clone [https://github.com/paulorabelo/terminal-ai.git](https://github.com/paulorabelo/terminal-ai.git)
cd terminal-ai
````

### 2. Prepare o Ambiente Python

Recomendamos usar um ambiente virtual (`venv`) para isolar as dependências e manter o sistema operacional seguro.

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

## 🔄 Como Atualizar

Lançamos atualizações frequentes! Para atualizar seu assistente sem dor de cabeça (baixar código novo e atualizar bibliotecas automaticamente), basta entrar na pasta do projeto e rodar:

Bash

```bash
bash update.sh
```

_(O script detecta se você precisa de novas bibliotecas e ajusta o ambiente virtual automaticamente)._

---

## 🔐 Configuração (Uma única vez)

Para que o assistente funcione sempre, configure sua chave de API e o atalho no seu shell (`.bashrc` ou `.zshrc`).

1. **Obtenha sua Chave:** Crie uma API Key gratuita no [Google AI Studio](https://aistudio.google.com/).
    
2. **Edite seu arquivo de configuração:**
    
    Bash
    
    ```bash
    nano ~/.zshrc   # Se usa Zsh (padrão no macOS e distros modernas)
    # OU
    nano ~/.bashrc  # Se usa Bash (padrão Ubuntu/Server)
    ```
    
3. **Adicione ao final do arquivo:**
    
    Bash
    
    ```bash
    # --- Configuração Terminal AI ---
    export GEMINI_API_KEY="SUA_CHAVE_AQUI_COLE_SEM_ASPAS_EXTRAS"
    
    # O alias aponta direto para o Python DENTRO do venv
    alias ajuda='~/caminho/para/terminal-ai/venv/bin/python ~/caminho/para/terminal-ai/assistant.py'
    ```
    
    _(Atenção: Substitua `~/caminho/para/terminal-ai` pelo caminho real da sua pasta)._
    
4. **Recarregue o terminal:**
    
    Bash
    
    ```bash
    source ~/.zshrc  # ou source ~/.bashrc
    ```
    

---

## 🏃‍♂️ Como Usar

### Uso Básico (Modelo Gemma 4)

Ótimo para perguntas do dia a dia, explicações de comandos e análise de textos/logs gigantes.

Bash

```bash
ajuda "Como configuro um proxy reverso no Nginx?"
```

### Uso PRO (Modelo Gemini 3.1 Flash Lite)

Use quando precisar de uma análise estrutural profunda. Consome sua cota diária limitada.

Bash

```bash
ajuda pro "Crie um script de automação em Python para gerenciar docker-compose"
# ou
ajuda turbo "Faça o debug deste erro de Kernel Panic"
```

### O Poder do Pipe (`|`)

Analise saídas de outros comandos injetando os dados diretamente no assistente.

**Analisar Logs Extensos:**

Bash

```bash
# O modelo Gemma 4 consegue ler volumes altíssimos de dados de uma vez!
cat /var/log/syslog | ajuda "Qual a causa raiz dos erros nas últimas 2 horas?"
```

**Monitorar Processos:**

Bash

```bash
ps aux --sort=-%mem | head -n 10 | ajuda "Quem está consumindo minha memória e como resolvo?"
```

---

## 📊 Telemetria Local

O script cria um arquivo oculto `~/.gemini_usage.json` no seu diretório home para contar de forma privada quantas vezes você usou o modo PRO no dia. Isso ajuda a gerenciar seus recursos gratuitos e evita que você bata no teto da API sem aviso.

---

## 🤝 Contribuições

Sinta-se livre para abrir Issues ou PRs. Projeto ideal para estudantes de Engenharia de Computação, SysAdmins e entusiastas de DevOps.

---

Feito com 🐍 Python e 🤖 Google AI por [Paulo Rabelo](https://paulorabelo.dev.br/).