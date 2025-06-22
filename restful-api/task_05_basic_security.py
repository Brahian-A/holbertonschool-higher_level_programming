from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (
    JWTManager, create_access_token, get_jwt_identity, get_jwt,
    jwt_required, verify_jwt_in_request
)
from functools import wraps

# Inicializar la app Flask
app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "super_secret_key"  # Clave secreta para JWT

# Autenticadores
auth = HTTPBasicAuth()
jwt = JWTManager(app)

# Base de datos en memoria con usuarios y sus roles
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}


# Manejo de errores con JWT

@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401

@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401

@jwt.expired_token_loader
def handle_expired_token_error(err, payload):
    return jsonify({"error": "Token has expired"}), 401

@jwt.revoked_token_loader
def handle_revoked_token_error(jwt_header, jwt_payload):
    return jsonify({"error": "Token has been revoked"}), 401

@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(jwt_header, jwt_payload):
    return jsonify({"error": "Fresh token required"}), 401

# verificador de contraseña 

@auth.verify_password
def verify_password(username, password):
    user = users.get(username)
    if user and check_password_hash(user["password"], password):
        return user
    return None

# decorador para acecso de admin

def admin_required():
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            verify_jwt_in_request()
            claims = get_jwt()
            if claims.get("role") == "admin":
                return fn(*args, **kwargs)
            else:
                return jsonify({"error": "Admin access required"}), 403
        return decorator
    return wrapper

# rutas

# ruta protegida
@app.route('/basic-protected')
@auth.login_required
def basic_protected():
    return "Basic Auth: Access Granted", 200

# ruta para genrar token 
@app.route('/login', methods=['POST'])
def login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    user = verify_password(username, password)

    if not user:
        return jsonify({"msg": "Bad username or password"}), 401

    # Incluir el rol en el token
    additional_claims = {"role": user["role"]}
    access_token = create_access_token(identity=username, additional_claims=additional_claims)
    return jsonify(access_token=access_token), 200

# Ruta protegida con JWT
@app.route('/jwt-protected')
@jwt_required()
def jwt_protected():
    return "JWT Auth: Access Granted", 200

# Ruta solo para administradores
@app.route('/admin-only')
@admin_required()
def admin_only():
    return "Admin Access: Granted", 200

# Ejecutar la aplicación
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
