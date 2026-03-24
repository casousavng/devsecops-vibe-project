from fastapi import FastAPI
import psycopg2

app = FastAPI()

@app.get("/produto/{id}")
def get_produto(id: str):
    # VULNERABILIDADE: SQL Injection via interpolação de strings (Vibe Coding)
    conn = psycopg2.connect("host=postgres dbname=loja user=admin password=pass")
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM produtos WHERE id = '{id}'") # PERIGO AQUI
    return {"dados": cur.fetchone()}