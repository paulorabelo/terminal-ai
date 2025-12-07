# 🐧 Terminal AI Assistant

Um assistente de linha de comando (CLI) simples e poderoso para Linux, turbinado pela API do Google Gemini.

Este projeto conecta seu terminal diretamente à inteligência artificial, permitindo que você tire dúvidas de comandos, analise logs de erro e entenda códigos usando Pipes (`|`), tudo sem sair da tela preta.

![Terminal AI em ação](/ajuda.png)
*(Terminal com AI)*

## 🚀 Funcionalidades

- **Respostas Rápidas:** Pergunte diretamente: `ajuda "Como descompactar tar.gz?"`
- **Análise de Contexto (Pipes):** Use a saída de outros comandos como entrada para a IA.
  - Ex: `cat erro_servidor.log | ajuda "Explique a causa raiz deste erro"`
  - Ex: `ls -la | ajuda "Qual o maior arquivo e o que ele faz?"`
- **IA Avançada:** Utiliza o modelo **Gemini 2.0 Flash** do Google para respostas rápidas e precisas.

---

## 🛠️ Pré-requisitos

- Linux (Testado no Linux Mint/Ubuntu, mas deve funcionar na maioria das distros).
- Python 3.6 ou superior.
- Uma chave de API do Google AI Studio (Gratuita).

---

## ⚙️ Instalação Passo a Passo

### 1. Clone o repositório
Baixe o código para sua máquina:
```bash
git clone https://github.com/paulorabelo/terminal-ai.git
cd terminal-ai
````

### 2. Prepare o Ambiente Python

Para evitar conflitos com o sistema operacional, usaremos um ambiente virtual (`venv`).

⚠️ **Usuários de Ubuntu/Debian/Mint:** É necessário instalar o pacote do venv primeiro:

Bash

```
sudo apt update && sudo apt install python3-venv -y
```

Agora, crie e ative o ambiente isolado dentro da pasta do projeto:

Bash

```
python3 -m venv venv
source venv/bin/activate
```

_(Você verá `(venv)` no início da linha do terminal)._

### 3. Instale as dependências

Bash

```
pip install -r requirements.txt
```

---

## 🔐 Configuração

Para que o assistente funcione, você precisa configurar sua chave de API e criar o atalho (alias). Vamos fazer isso de forma **persistente**, para funcionar sempre que você abrir o terminal.

### 1. Obtenha sua Chave

Vá ao [Google AI Studio](https://aistudio.google.com/), crie um novo projeto e gere uma **API Key**.

### 2. Edite o arquivo de configuração do seu Shell

Identifique qual shell você usa (geralmente Bash ou Zsh).

- Se usa **Zsh** (comum no Mint/Manjaro com temas): edite `~/.zshrc`
    
- Se usa **Bash** (padrão do Ubuntu): edite `~/.bashrc`
    

Abra o arquivo no seu editor preferido (ex: `xed ~/.zshrc` ou `nano ~/.bashrc`) e **adicione estas linhas ao final do arquivo**:

Bash

```
# --- Configuração do Terminal AI ---
# Substitua pelo sua chave real (mantenha as aspas)
export GEMINI_API_KEY="COLE_SUA_CHAVE_AIza_AQUI"

# Cria o comando 'ajuda'. Ajuste o caminho se não clonou na pasta raiz.
alias ajuda='~/terminal-ai/venv/bin/python ~/terminal-ai/assistant.py'
```

### 3. Aplique as mudanças

Salve o arquivo, feche o editor e rode o comando abaixo para recarregar as configurações (ou feche e abra o terminal novamente):

Bash

```
source ~/.zshrc  # ou source ~/.bashrc
```

---

## 🏃‍♂️ Como Usar

Agora você tem o comando `ajuda` disponível em todo o sistema!

**Uso direto:**

Bash

```
ajuda "Qual a diferença entre apt e dpkg?"
```

**Uso com Pipes (O poder real):**

Bash

```
# Analisar um script
cat meu_script_antigo.py | ajuda "Resuma o que este código faz e sugira melhorias"

# Analisar logs do sistema
tail -n 20 /var/log/syslog | ajuda "Existem erros críticos nestas últimas linhas?"
```

## 🤝 Contribuições

Pull requests são bem-vindos! Para mudanças grandes, abra uma issue primeiro para discutir o que você gostaria de mudar.

---

Feito com 🐍 e 🤖 por [Paulo Rabelo](https://www.linkedin.com/in/paulorabelooficial/)