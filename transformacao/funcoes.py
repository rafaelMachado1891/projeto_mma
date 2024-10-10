import re

# Função para extrair o método da coluna 'round'
def extrair_metodo(round_text):
    if round_text and ' • ' in round_text:
        return round_text.split(' • ')[0]
    elif round_text == 'KO/TKO':
        return 'KO/TKO'
    elif round_text and 'Decision' in round_text:
        return 'Decision'
    return None

# Função para extrair informações do round ou detalhe da decisão da coluna 'round'
def extrair_detalhe(round_text):
    if round_text and ' • ' in round_text:
        round_info = round_text.split(' • ')[1]
        return round_info
    elif round_text and 'Decision' in round_text:
        detalhe = re.search(r'\((.*?)\)', round_text)
        if detalhe:
            return detalhe.group(1)
    return None

def extrair_win_or_loss_do_texto(resultado_text):
    if resultado_text:
        if "Win" in resultado_text:
            return "Win"
        elif "Loss" in resultado_text:
            return "Loss"
    return None
