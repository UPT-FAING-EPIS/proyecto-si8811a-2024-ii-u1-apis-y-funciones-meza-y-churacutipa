from flask import Flask, redirect, url_for, session, request
from msal import ConfidentialClientApplication
import os

app = Flask(__name__)
app.secret_key = ''

CLIENT_ID = ""
CLIENT_SECRET = ""
AUTHORITY = ""
REDIRECT_PATH = "/getAToken"  
SCOPE = ["User.Read"]  

app_msal = ConfidentialClientApplication(
    CLIENT_ID,
    authority=AUTHORITY,
    client_credential=CLIENT_SECRET,
)

@app.route('/')
def index():
    if not session.get("user"):
        return redirect(url_for("login"))
    return f"Hello, {session['user']['name']}!"
# Funcion Login
@app.route('/login')
def login():
    
    auth_url = app_msal.get_authorization_request_url(
        SCOPE,
        redirect_uri=url_for("authorized", _external=True)
    )
    print(f"Auth URL: {auth_url}")  
    return redirect(auth_url)

@app.route(REDIRECT_PATH)
def authorized():
    code = request.args.get('code')
    if not code:
        return "Error al obtener el código de autorización", 400

    result = app_msal.acquire_token_by_authorization_code(
        code,
        scopes=SCOPE,
        redirect_uri=url_for("authorized", _external=True)
    )

    if "access_token" in result:
        access_token = result['access_token']
        print(f"Access Token: {access_token}")  
        session["user"] = result.get("id_token_claims")
        return redirect(url_for("index"))
    else:
        print(f"Error: {result.get('error')}, Description: {result.get('error_description')}")  
        return "Error al obtener el token de acceso", 400

@app.route('/logout')
def logout():
    session.clear()
    return redirect(
        AUTHORITY + "/oauth2/v2.0/logout" +
        "?post_logout_redirect_uri=" + url_for("index", _external=True)
    )

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
