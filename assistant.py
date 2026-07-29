from google import genai
from google.genai import types
import sys
import os
import json
from datetime import date

# --- CONFIGURAÇÃO ---
api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
    print("❌ Erro: Chave de API não encontrada.")
    sys.exit(1)

# JEITO NOVO: Instancia o cliente com a chave
client = genai.Client(api_key=api_key)

# --- CONFIGURAÇÃO DE LIMITES ---
LIMIT_PRO = 20 
USAGE_FILE = os.path.expanduser("~/.gemini_usage.json")

# --- SELETOR DE MODELO ---
model_name = "gemma-4-31b-it" # Padrão (Gemma)
user_args = sys.argv[1:]
is_pro_mode = False

if user_args and (user_args[0].lower() in ["pro", "turbo", "flash"]):
    model_name = "gemini-3.5-flash-lite"
    is_pro_mode = True
    user_args = user_args[1:]
    print(f"🚀 Modo PRO ({model_name}) ativado!")

# --- REMOVIDO: model = genai.GenerativeModel(...) ---
# No novo SDK, não instanciamos o modelo aqui. Usamos a string 'model_name' lá embaixo.

SYSTEM_PROMPT = """
    ATUAÇÃO: Você é um Engenheiro de Software Sênior e especialista em Linux (Mint/Ubuntu).
    
    REGRAS DE ANÁLISE DE DADOS (STDIN):
    1. SE receber uma lista de arquivos (saída de ls):
       - Identifique arquivos suspeitos, grandes ou relevantes baseando-se no nome/extensão.
       - Se o usuário perguntar "o que faz", explique a função TÍPICA daquele tipo de arquivo (ex: .py é script Python, .log é registro de eventos), mas deixe claro que você está vendo apenas a lista, não o conteúdo.
       - Sugira o comando 'cat nome_do_arquivo | ajuda' para ler o conteúdo real.
    
    2. SE receber conteúdo de texto (código, logs):
       - Analise, resuma ou explique o erro.
    
    FORMATO DE RESPOSTA:
    - Direto ao ponto.
    - Sem Markdown excessivo (evite blocos ```).
    - Use emojis para categorizar (📁 Arquivo, 🐍 Python, ⚙️ Config).
    """

def get_daily_usage():
    """Lê e gerencia a contagem diária localmente"""
    today_str = str(date.today())
    data = {"date": today_str, "count": 0}
    
    if os.path.exists(USAGE_FILE):
        try:
            with open(USAGE_FILE, 'r') as f:
                saved_data = json.load(f)
                if saved_data.get("date") == today_str:
                    data = saved_data
        except:
            pass 
    return data

def update_usage(current_count):
    """Salva a nova contagem"""
    with open(USAGE_FILE, 'w') as f:
        json.dump({"date": str(date.today()), "count": current_count + 1}, f)

def main():
    user_query = ""
    pipe_content = ""

    if user_args:
        user_query = " ".join(user_args)

    if not sys.stdin.isatty():
        try:
            pipe_content = sys.stdin.read().strip()
        except Exception:
            pass

    if not user_query and not pipe_content:
        print("🤔 Uso: ajuda 'pergunta' | ajuda pro 'pergunta'")
        return

    # --- CHECAGEM DE USO (Só no modo PRO) ---
    usage_data = get_daily_usage()
    if is_pro_mode:
        used = usage_data["count"]
        if used >= LIMIT_PRO:
            print(f"⚠️ Limite diário do modo PRO atingido ({used}/{LIMIT_PRO}).")
            print("💡 Dica: Use sem o 'pro' para usar o modelo Gemma quase \"ilimitado\".")
            sys.exit(0)

    # Monta o Prompt Único
    final_prompt = f"{SYSTEM_PROMPT}\n\n--- DADOS ---\n{pipe_content}\n\n--- PERGUNTA ---\n{user_query}"

    print("🤖 Analisando...", end="\r")

    # Define um modelo padrão para fallback
    FALLBACK_MODEL = "gemini-flash-latest"

    try:
        # --- A GRANDE MUDANÇA AQUI ---
        # Chamada usando o client e passando o nome do modelo como string
        response = client.models.generate_content(
            model=model_name,
            contents=final_prompt
        )
        
        print(" " * 20, end="\r")
        print(response.text)
        
        # --- ATUALIZA O CONTADOR SE DEU CERTO ---
        if is_pro_mode:
            update_usage(usage_data["count"])
            remaining = LIMIT_PRO - (usage_data["count"] + 1)
            print(f"\n📊 Cota PRO hoje: {usage_data['count'] + 1}/{LIMIT_PRO} (Restam: {remaining})")

    except Exception as e:
        error_msg = str(e)
        
        # Se o erro for de Servidor (500 ou 503), aciona o Plano B
        if "500" in error_msg or "503" in error_msg:
            print(f"⚠️ O servidor falhou com o modelo '{model_name}' (Erro de estabilidade/demanda).")
            print(f"🔄 Acionando Plano B (Fallback para {FALLBACK_MODEL})...")
            
            try:
                # Tentativa 2: Modelo de Segurança
                response_fallback = client.models.generate_content(
                    model=FALLBACK_MODEL,
                    contents=final_prompt
                )
                print(" " * 20, end="\r")
                print(response_fallback.text)
                print(f"\n(ℹ️ Resposta gerada pelo modelo de segurança: {FALLBACK_MODEL})")
                
            except Exception as fallback_error:
                print(f"\n❌ Falha Crítica: O modelo de segurança também falhou: {fallback_error}")
                
        # Tratamento de Erro de Cota (429)
        elif "429" in error_msg:
            print("❌ ERRO DE COTA (429): Limite excedido.")
            print("⚠️ Aguarde um pouco ou verifique se o arquivo de entrada é muito grande.")
            
        # Qualquer outro erro (como nome de modelo errado)
        else:
            print(f"\n❌ Erro na API: {error_msg}")
            if "404" in error_msg or "not found" in error_msg.lower():
                print(f"⚠️ DICA: O modelo '{model_name}' pode não estar disponível para sua chave.")

if __name__ == "__main__":
    main()