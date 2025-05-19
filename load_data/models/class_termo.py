class Termo:
    def __init__(self, termo: str = None, traducao: str = None, descricao: str = None, codigo: str = None):
        self.termo = termo
        self.traducao = traducao
        self.descricao = descricao
        self.codigo = codigo

    def __repr__(self):
        return f"Termo(termo='{self.termo}', traducao='{self.traducao}', descricao='{self.descricao}', codigo='{self.codigo}')"

    def to_dict(self):
        return self.__dict__

    @classmethod
    def from_dict(cls, data: dict):
        return cls(**data)