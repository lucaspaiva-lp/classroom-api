from domain.usuario import Usuario
from domain.sala import Sala
from domain.reserva import Reserva
from repositories.memory import db


def criar_usuario(nome: str, email: str):
    if any(u.email == email for u in db['usuarios']):
        return None
    
    novo_id = len(db['usuarios']) + 1
    usuario = Usuario(id=novo_id, nome=nome, email=email)
    db['usuarios'].append(usuario)
    return usuario


def listar_usuarios():
    return db['usuarios']


def criar_sala(nome: str, capacidade: int, bloco: str):
    novo_id = len(db['salas']) + 1
    sala = Sala(id=novo_id, nome=nome, capacidade=capacidade, bloco=bloco)
    db['salas'].append(sala)
    return sala


def listar_salas():
    return db['salas']


def criar_reserva(usuario_id: int, sala_id: int, data: str, hora_inicio: str, hora_fim: str):
    novo_id = len(db['reservas']) + 1
    reserva = Reserva(
        id=novo_id, 
        usuario_id=usuario_id, 
        sala_id=sala_id, 
        data=data, 
        hora_inicio=hora_inicio, 
        hora_fim=hora_fim
    )
    db['reservas'].append(reserva)
    return reserva


def listar_reservas():
    return db['reservas']


def listar_reservas_usuario(usuario_id: int):
    return [r for r in db['reservas'] if r.usuario_id == usuario_id]


def buscar_reserva(reserva_id: int):
    for r in db['reservas']:
        if r.id == reserva_id:
            return r
    return None


def cancelar_reserva(reserva_id: int):
    reserva = buscar_reserva(reserva_id)
    if reserva:
        db['reservas'].remove(reserva)
        return True
    return False


def finalizar_reserva(reserva_id: int, hora_atual: str):
    reserva = buscar_reserva(reserva_id)
    if reserva:
        reserva.hora_fim = hora_atual
        return reserva
    return None