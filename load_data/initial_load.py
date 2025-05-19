from repositories.termo_repository import TermoRepository
from functions.extrair_texto import extrair_texto_pdf
from functions.obter_registros import identificar_termos_traducao_descricao_codigo
    

nome_arquivo_pdf = 'docs/dic1.pdf'
pagina_inicial = 12
pagina_final = 523
nome_arquivo_csv = 'dicionario_informatica.csv'
linhas_header_footer = 1 


def carga_inicial():
    """
    Carregar os dados do PDF e processá-los.
    """
    print(f"Extraindo texto das páginas {pagina_inicial} a {pagina_final} do arquivo '{nome_arquivo_pdf}' (removendo {linhas_header_footer} linhas de header/footer)...")
    texto = extrair_texto_pdf(nome_arquivo_pdf, pagina_inicial, pagina_final, linhas_header_footer)

    if texto:
        print("Identificando termos, traduções, descrições e códigos...")
        registros_encontrados = identificar_termos_traducao_descricao_codigo(texto)

        print(f"Encontrados {len(registros_encontrados)} registros.")
        for reg in registros_encontrados[:5]:
            print(reg)
        termo_repo = TermoRepository()
    return termo_repo, registros_encontrados