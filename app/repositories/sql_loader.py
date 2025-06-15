import os
from typing import Dict

class SQLLoader:
    _queries: Dict[str, str] = {}
    
    @classmethod
    def load_sql(cls, entity: str, query_name: str) -> str:
        """Carrega uma query SQL do arquivo correspondente"""
        key = f"{entity}_{query_name}"
        
        if key not in cls._queries:
            sql_path = os.path.join(
                os.path.dirname(__file__),
                entity,
                f"{query_name}.sql"
            )
            
            with open(sql_path, 'r', encoding='utf-8') as file:
                cls._queries[key] = file.read().strip()
        
        return cls._queries[key] 