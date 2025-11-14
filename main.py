from website import create_app
from dotenv import load_dotenv

secret_key = os.getenv("SECRET_KEY")
db_uri = os.getenv("DATABASE_URI")

app = create_app(secret_key=secret_key, db_uri=db_uri)

if __name__ == "__main__":
    app.run(debug=True)