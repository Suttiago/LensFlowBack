from sqlalchemy import text
from database import engine

try:
    with engine.connect() as conn:
        conn.execute(text("SELECT 1"))
    print("✅ Banco conectado com sucesso")
except Exception as e:
    print("❌ Falha na conexão com o banco")
    print(repr(e))
