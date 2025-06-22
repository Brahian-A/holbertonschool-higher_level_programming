from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    create_access_token, get_jwt_identity, get_jwt,
    jwt_required, JWTManager, verify_jwt_in_request
)
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "secret"  # Clave secreta para firmar tokens JWT

auth = HTTPBasicAuth()
jwt = JWTManager(app)

# Usuarios definidos con contraseña encriptada y rol
users = {
    "user1": {"username": "user1", "password": generate_password_hash("password"), "role": "user"},
    "admin1": {"username": "admin1", "password": generate_password_hash("password"), "role": "admin"}
}

# Manejadores personalizados para distintos errores con tokens JWT
@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Token faltante o inválido"}), 401

@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Token inválido"}), 401

@jwt.expired_token_loader
def handle_expired_token_error(err):
    return jsonify({"error": "Token expirado"}), 401

@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    return jsonify({"error": "Token revocado"}), 401

@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    return jsonify({"error": "Se requiere un token fresco"}), 401

# Decorador personalizado que permite el acceso solo a administradores
def admin_required():
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            verify_jwt_in_request()
            claims = get_jwt()
            if claims["role"] == 'admin':
                return fn(*args, **kwargs)
            else:
                return jsonify({"error": "Acceso solo para administradores"}), 403
        return decorator
    return wrapper

# Verificación de usuario y contraseña
@auth.verify_password
def verify_password(username, password):
    if username not in users:
        return None

    if check_password_hash(users[username]["password"], password):
        return users[username]

# Ruta protegida con autenticación básica
@app.route('/basic-protected')
@auth.login_required
def index():
    return "Autenticación Básica: Acceso permitido", 200

# Ruta para hacer login y obtener un token JWT
@app.route("/login", methods=["POST"])
def login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)

    user = verify_password(username, password)
    if not user:
        return jsonify({"msg": "Usuario o contraseña incorrectos"}), 401

    # Se agregan datos personalizados
    additional_claims = {"role": user["role"]}
    access_token = create_access_token(identity=username, additional_claims=additional_claims)
    return jsonify(access_token=access_token)

# Ruta protegida con token JWT válido
@app.route("/jwt-protected")
@jwt_required()
def protected():
    current_user = get_jwt_identity()  # Obtener el usuario del token
    return "Autenticación JWT: Acceso permitido", 200

# Ruta solo accesible para usuarios con rol "admin"
@app.route('/admin-only')
@admin_required()
def admins_only():
    current_user = get_jwt_identity()
    return "Acceso de administrador: permitido", 200

# Ejecutar la app
if __name__ == '__main__':
    app.run()
