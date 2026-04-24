import os
import mysql.connector
from pymongo import MongoClient
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

conn = mysql.connector.connect(
    database=os.getenv("MYSQL_DATABASE"),
    user=os.getenv("MYSQL_USER"),
    password=os.getenv("MYSQL_PASSWORD"),
    port=3306,
    host=os.getenv("MYSQL_HOST")
)

mongo_client = MongoClient(
    host=os.getenv("MONGO_HOST"),
    port=int(os.getenv("MONGO_PORT")),
    username=os.getenv("MONGO_USER"),
    password=os.getenv("MONGO_PASSWORD"),
    authSource=os.getenv("MONGO_DB")
)

mongo_db = mongo_client[os.getenv("MONGO_DB")]

@app.get("/")
async def home():
    return {"message": "API Python connectée à MySQL et MongoDB"}

@app.get("/users")
async def get_users():
    cursor = conn.cursor()
    sql_select_Query = "select * from utilisateur"
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    print("Total number of rows in table: ", cursor.rowcount)
    return {'utilisateurs': records}

@app.get("/posts")
async def get_posts():
    posts = list(mongo_db.posts.find({}, {"_id": 0}))
    return {'posts': posts}

@app.get("/health")
def health_check():
    try:
        # test mysql
        cursor = conn.cursor()
        cursor.execute("select count(*) from utilisateur")
        mysql_count = cursor.fetchone()[0]

        # test mongo
        mongo_count = mongo_db.posts.count_documents({})

        if mysql_count == 4 and mongo_count == 5:
            return {"status": "healthy"}

        return {
            "status": "unhealthy",
            "mysql_users": mysql_count,
            "mongo_posts": mongo_count
        }

    except Exception as e:
        return {"status": "unhealthy", "error": str(e)}
