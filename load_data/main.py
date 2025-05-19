from initial_load import carga_inicial

if __name__ == "__main__":

    print("\n--- MongoDB Operations using Repository ---")

    # Carregar os dados do PDF e processá-los
    termo_repo, registros_encontrados = carga_inicial()
    # Inserção de registros
    for registro in registros_encontrados:
        termo_repo.insert_one(registro)

    # # Consulta de todos os termos
    # todos_termos = termo_repo.find_all()
    # print("\nTodos os termos:")
    # for termo in todos_termos:
    #     print(termo)

    # # Consulta de um termo específico
    # termo_especifico = termo_repo.find_one({"termo": "ABC"})
    # print("\nTermo específico (ABC):")
    # print(termo_especifico)

    # # Atualização de um termo
    # atualizado = termo_repo.update_one({"termo": "A-Talk for Windows"}, {"descricao": "Software de comunicação para BBS (atualizado)."})
    # print(f"\nAtualização bem-sucedida: {atualizado}")

    # # Consulta após atualização
    # termo_atualizado = termo_repo.find_one({"termo": "A-Talk for Windows"})
    # print("\nTermo atualizado (A-Talk for Windows):")
    # print(termo_atualizado)

    # # Exclusão de um termo
    # excluido = termo_repo.delete_one({"termo": "A/B switch"})
    # print(f"\nExclusão bem-sucedida: {excluido}")

    # # Consulta após exclusão
    # todos_termos_pos_exclusao = termo_repo.find_all()
    # print("\nTermos após exclusão:")
    # for termo in todos_termos_pos_exclusao:
    #     print(termo)

    # # Close the MongoDB connection (optional, as the Singleton instance persists)
    # # MongoDBConnection().close()

    # print("\nProcesso concluído!")