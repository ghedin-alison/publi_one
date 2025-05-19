import re

def identificar_termos_traducao_descricao_codigo(texto):
    """Tenta identificar termos, traduções, descrições e códigos no texto extraído."""
    registros = []
    linhas = texto.strip().split('\n')
    i = 0
    id_termo = 0
    while i < len(linhas):
        linha = linhas[i].strip()
        if not linha:
            i += 1
            continue

        match_termo = re.match(r"([A-Z][a-zA-Z0-9\s'/\-]+|[A-Z0-9]+(?:-[A-Z0-9]+)*)\s*(?:–\s*|\-\s*|\s*\-\s*)?(.*)", linha)
        
        if match_termo:
            id_termo += 1

            traducao = None
            codigo = None
            descricao_completa = None
            inicio_traducao = None

            termo = match_termo.string.split(' – ')
            termo_principal = termo[0].strip()

            if termo_principal[-1] == '-':
                i += 1
                while i < len(linhas):
                    linha_composta = linhas[i].split(' – ')
                    complemento = linha_composta[0]
                    termo_principal = termo_principal[:-1] + complemento
                    # if len(linha_composta) > 1:
                    #     match_codigo = re.search(r"\((\w+-\d+)\)$", linha_composta[1])
                    #     if match_codigo:
                    #         codigo = match_codigo.group(1)
                    #         traducao = linha_composta[1][:match_codigo.start()]
                    #         registros.append({"id": id_termo, 'termo': termo_principal, 'traducao': traducao, 'descricao': descricao_completa, 'codigo': codigo})
                    #         i += 1
                    #         continue
                    #     inicio_traducao = linha_composta[1].strip()
                    break
            
            if len(termo) > 1:
                match_codigo = re.search(r"\((\w+-\d+)\)$", termo[1])
                if match_codigo:
                    codigo = match_codigo.group(1)
                    traducao = termo[1][:match_codigo.start()]
                    registros.append({"id": id_termo, 'termo': termo_principal, 'traducao': traducao, 'descricao': descricao_completa, 'codigo': codigo})
                    i += 1
                    continue
                else:
                    match termo[1][-1]:
                        case '.':
                            traducao = termo[1].strip()
                        case '_':
                            traducao = None

            j = i + 1
            while j < len(linhas):
                if inicio_traducao:
                    traducao = inicio_traducao + " " + linhas[j].strip()
                    inicio_traducao = None
                else:
                    linha_descricao = linhas[j].strip()
                match_codigo = re.search(r"\((\w+-\d+)\)$", linha_descricao)
                if match_codigo:
                    codigo = match_codigo.group(1)
                    linha_sem_codigo = linha_descricao[:match_codigo.start()].strip()
                    if linha_sem_codigo:
                        if descricao_completa:
                            descricao_completa += " " + linha_sem_codigo
                        else:
                            descricao_completa = linha_sem_codigo
                    break
                else:
                    if descricao_completa:
                        descricao_completa += " " + linha_descricao
                    else:
                        descricao_completa = linha_descricao
                    j += 1    


            registros.append({"id": id_termo, 'termo': termo_principal, 'traducao': traducao, 'descricao': descricao_completa, 'codigo': codigo})
            i = j + 1
        else:
            i += 1

    return registros
