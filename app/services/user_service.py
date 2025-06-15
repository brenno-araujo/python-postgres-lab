from typing import List, Dict, Optional
import psycopg2
from psycopg2.extras import RealDictCursor
from fastapi import HTTPException
from ..repositories.sql_loader import SQLLoader
import os

class UserService:
    
    @staticmethod
    def _get_db_connection():
        """Cria conexão com o banco de dados"""
        try:
            conn = psycopg2.connect(
                host=os.getenv("DB_HOST", "db"),
                database=os.getenv("DB_NAME", "studydb"),
                user=os.getenv("DB_USER", "postgres"),
                password=os.getenv("DB_PASS", "postgres"),
                port=5432
            )
            return conn
        except psycopg2.OperationalError as e:
            raise HTTPException(status_code=500, detail=f"Erro de conexão com o banco: {e}")
    
    @staticmethod
    def get_all_users() -> List[Dict]:
        """Busca todos os usuários"""
        conn = UserService._get_db_connection()
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        
        try:
            query = SQLLoader.load_sql("users", "get_all_users")
            cursor.execute(query)
            users = cursor.fetchall()
            return [dict(user) for user in users]
        finally:
            cursor.close()
            conn.close()
    
    @staticmethod
    def get_user_by_id(user_id: int) -> Optional[Dict]:
        """Busca um usuário por ID"""
        conn = UserService._get_db_connection()
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        
        try:
            query = SQLLoader.load_sql("users", "get_user_by_id")
            cursor.execute(query, (user_id,))
            user = cursor.fetchone()
            return dict(user) if user else None
        finally:
            cursor.close()
            conn.close()
    
    @staticmethod
    def create_user(full_name: str) -> Dict:
        """Cria um novo usuário"""
        conn = UserService._get_db_connection()
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        
        try:
            query = SQLLoader.load_sql("users", "create_user")
            cursor.execute(query, (full_name,))
            user = cursor.fetchone()
            conn.commit()
            return dict(user)
        except Exception as e:
            conn.rollback()
            raise HTTPException(status_code=500, detail=f"Erro ao criar usuário: {e}")
        finally:
            cursor.close()
            conn.close()
    
    @staticmethod
    def update_user(user_id: int, full_name: str) -> Optional[Dict]:
        """Atualiza um usuário"""
        conn = UserService._get_db_connection()
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        
        try:
            query = SQLLoader.load_sql("users", "update_user")
            cursor.execute(query, (full_name, user_id))
            user = cursor.fetchone()
            conn.commit()
            return dict(user) if user else None
        except Exception as e:
            conn.rollback()
            raise HTTPException(status_code=500, detail=f"Erro ao atualizar usuário: {e}")
        finally:
            cursor.close()
            conn.close()
    
    @staticmethod
    def delete_user(user_id: int) -> bool:
        """Deleta um usuário"""
        conn = UserService._get_db_connection()
        cursor = conn.cursor()
        
        try:
            query = SQLLoader.load_sql("users", "delete_user")
            cursor.execute(query, (user_id,))
            deleted_rows = cursor.rowcount
            conn.commit()
            return deleted_rows > 0
        except Exception as e:
            conn.rollback()
            raise HTTPException(status_code=500, detail=f"Erro ao deletar usuário: {e}")
        finally:
            cursor.close()
            conn.close() 