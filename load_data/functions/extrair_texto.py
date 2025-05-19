from PyPDF2 import PdfReader

def extrair_texto_pdf(caminho_pdf, pagina_inicial, pagina_final, header_footer_lines=2):
    """Extrai o texto de um intervalo específico de páginas de um PDF,
    desprezando as primeiras e últimas 'header_footer_lines' linhas de cada página."""
    texto_completo = ""
    try:
        with open(caminho_pdf, 'rb') as arquivo_pdf:
            leitor_pdf = PdfReader(arquivo_pdf)
            num_paginas = len(leitor_pdf.pages)
            if pagina_inicial < 1 or pagina_final > num_paginas or pagina_inicial > pagina_final:
                raise ValueError(f"Intervalo de páginas inválido. O PDF tem {num_paginas} páginas.")

            for numero_pagina in range(pagina_inicial - 1, pagina_final):
                pagina = leitor_pdf.pages[numero_pagina]
                texto_pagina = pagina.extract_text().split('\n')
                if len(texto_pagina) > 2 * header_footer_lines:
                    texto_pagina_sem_header_footer = texto_pagina[header_footer_lines:-header_footer_lines]
                    texto_completo += "\n".join(texto_pagina_sem_header_footer) + "\n"
                elif len(texto_pagina) > header_footer_lines:
                    texto_pagina_sem_header_footer = texto_pagina[header_footer_lines:]
                    texto_completo += "\n".join(texto_pagina_sem_header_footer) + "\n"
                else:
                    # Página muito curta, considera todo o conteúdo
                    texto_completo += "\n".join(texto_pagina) + "\n"

    except FileNotFoundError:
        print(f"Erro: O arquivo PDF '{caminho_pdf}' não foi encontrado.")
        return None
    except Exception as e:
        print(f"Ocorreu um erro ao processar o PDF: {e}")
        return None
    return texto_completo