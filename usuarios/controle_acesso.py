
# controle_acesso.py
# A classe ControleAcesso guarda os usuários e cuida do login.
import secrets
import hashlib
from usuarios.papeis import papeis_validos

CREDENCIAL_INVALIDA = "Matrícula ou senha inválida."

class ControleAcesso:

    # Construtor
    def __init__(self):
        self.usuarios = []
        self.sessoes = {}

    # Busca um usuário pela matrícula
    def buscar(self, matricula):
        for u in self.usuarios:
            if u.matricula == matricula:
                return u
        return None

    # Cadastra um usuário novo
    def cadastrar(self, usuario):
        achado = self.buscar(usuario.matricula)

        if achado is not None:
            return False

        self.usuarios.append(usuario)
        return True

    # Realiza o login
    def entrar(self, matricula, senha):
        usuario = self.buscar(matricula)
        if usuario is None:
            return None
        
        if not usuario.conferir_senha(senha) or usuario.situacao != "ativo":
            return None

        token = secrets.token_hex(16)
        self.sessoes[token] = matricula
        return token

    # Verifica quem está logado
    def usuario_logado(self, token):
        matricula = self.sessoes.get(token)
        if matricula is None:
            return None

        return self.buscar(matricula)

    # Encerra a sessão
    def sair(self, token):
        if token not in self.sessoes:
            return False

        del self.sessoes[token]
        return True

    # Altera os papéis de um usuário
    def mudar_papeis(self, quem, matricula, papeis):
        if not quem.pode("mudar_papeis"):
            return "Você não tem permissão para mudar papéis."
        
        usuario = self.buscar(matricula)

        if usuario is None:
            return "Usuário não encontrado."

        if not papeis:
            return "Escolha pelo menos um papel."

        for papel in papeis:
            if papel not in papeis_validos():
                return "Papel inválido: " + papel
        usuario.papeis = papeis
        return None

    def listar_usuarios(self):
        users = []
        for u in self.usuarios:
            users.append({
                "matricula": u.matricula,
                "nome": u.nome,
                "papeis": u.papeis,
                "supervisor": u.supervisor,
                "situacao": u.situacao
            })
        return users