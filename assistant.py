import google.generativeai as genai
import sys
import os

# --- CONFIGURAÇÃO ---
api_key = os.environ.get("GEMINI_API_KEY")

if not api_key:
    print("❌ Erro: Variável de ambiente 'GEMINI_API_KEY' não configurada.")
    sys.exit(1)

genai.configure(api_key=api_key)

# Modelo configurado para velocidade e eficiência (Tier Gratuito)
model = genai.GenerativeModel(
    model_name="gemini-2.0-flash",
    system_instruction="""
    ATUAÇÃO: Você é um Engenheiro de Software Sênior e especialista em Linux.
    
    REGRAS DE ANÁLISE:
    1. SE receber uma lista de arquivos (stdin):
       - Identifique arquivos relevantes pelo nome/extensão.
       - Explique a função TÍPICA desses arquivos (ex: .py é script Python).
       - Não invente conteúdo que você não leu.
    
    2. SE receber conteúdo de texto/código (stdin):
       - Analise, encontre erros ou resuma o funcionamento.
    
    3. SE for uma pergunta direta (args):
       - Responda com o comando e uma explicação curta.
    
    FORMATO:
    - Respostas diretas.
    - Sem Markdown excessivo (evite blocos de código com crase tripla).
    - Use emojis para categorizar.
    """
)

def main():
    user_query = ""
    pipe_content = ""

    # 1. Lê argumentos da linha de comando
    if len(sys.argv) > 1:
        user_query = " ".join(sys.argv[1:])

    # 2. Lê dados vindos via Pipe (|), se houver
    if not sys.stdin.isatty():
        pipe_content = sys.stdin.read().strip()

    # Se não houver nada, mostra ajuda
    if not user_query and not pipe_content:
        print("🤔 Uso: ajuda 'pergunta' OU cat arquivo.txt | ajuda")
        return

    # Monta o prompt final
    final_prompt = f"""
    Contexto/Dados do sistema (STDIN):
    {pipe_content}
    
    Pergunta do usuário:
    {user_query}
    
    (Analise os dados acima com base na pergunta. Se não houver pergunta, explique os dados.)
    """

    print("🤖 Analisando...", end="\r")

    try:
        response = model.generate_content(final_prompt)
        print(" " * 20, end="\r") # Limpa a linha de carregamento
        print(response.text)
    except Exception as e:
        print(f"\n❌ Erro na API: {e}")

if __name__ == "__main__":
    main()