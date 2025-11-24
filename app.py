from flask import Flask, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from models import db
from routes.product_routes import products_bp
from routes.personalised_products_routes import personalised_products_bp
from routes.skin_analysis_routes import skin_analysis_bp
import os


load_dotenv()

def create_app():
    app = Flask(__name__)
    CORS(app, resources={r"/*": {"origins": "*"}})

    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
    db.init_app(app)

    app.register_blueprint(products_bp)
    
    app.register_blueprint(personalised_products_bp)

    app.register_blueprint(skin_analysis_bp)

    @app.route("/")
    def home():
        return("<h1>Backend Home Page</h1>")
    
    @app.route("/test-db")
    def test_db():
        try:
            db.session.execute("SELECT 1")
            return "DB connected!"
        except Exception as e:
            return str(e)
    
    return app

app = create_app()

if __name__=="__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)