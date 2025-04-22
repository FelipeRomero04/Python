# Função auxiliar
def converter_para_reais(valor_em_dolar, taxa_de_cambio):
    return valor_em_dolar * taxa_de_cambio

# Função principal
def valor_final_em_reais(dolar, taxa):
    reais = converter_para_reais(dolar, taxa)
    return reais
