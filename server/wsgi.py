from app import create_app, db
import os

env = os.getenv("ENVIRONMENT", "development")

app = create_app(env)

if __name__ == "__main__":
    app.run(debug=True if env != "production" else False)
