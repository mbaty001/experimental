from flask import Flask, make_response, request


app = Flask(__name__)

# API keys (in real applications, databases or environment variables are used)
api_keys = {
    "123456": "Application A",
    "abcdef": "Application B",
}

# Authentication decorator
def require_api_key(f):
    def decorated_function(*args, **kwargs):
        api_key = request.headers.get("x-api-key")  # Extract API key from headers
        if not api_key or api_key not in api_keys:
            # the request cannot be authenticated
            return make_response({"message": "Unauthorized"}, 401)
        return f(*args, **kwargs)
    return decorated_function


@app.route("/public")
def public_route():
    return make_response({"message": "No API key needed."}, 200)


@app.route("/private")
@require_api_key
def private_route():
    return make_response({"message": "Valid API key was provided."}, 200)


if __name__ == "__main__":
    app.run(debug=True)

