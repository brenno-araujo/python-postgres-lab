from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
from .services.user_service import UserService

app = FastAPI()

# Modelos Pydantic
class UserCreate(BaseModel):
    full_name: str

class UserUpdate(BaseModel):
    full_name: str

@app.get("/users")
def get_all_users():
    """Busca todos os usuários"""
    return UserService.get_all_users()

@app.get("/users/{user_id}")
def get_user(user_id: int):
    """Busca um usuário por ID"""
    user = UserService.get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return user

@app.post("/users")
def create_user(user: UserCreate):
    """Cria um novo usuário"""
    return UserService.create_user(user.full_name)

@app.put("/users/{user_id}")
def update_user(user_id: int, user: UserUpdate):
    """Atualiza um usuário"""
    updated_user = UserService.update_user(user_id, user.full_name)
    if not updated_user:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return updated_user

@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    """Deleta um usuário"""
    deleted = UserService.delete_user(user_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return {"message": "Usuário deletado com sucesso"}

