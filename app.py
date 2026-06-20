from flask import Flask, jsonify, request

app = Flask(__name__)

# Simulated "business application" user database
users = {
    "1001": {"id": "1001", "username": "jsmith", "email": "jsmith@company.com", "status": "active"},
    "1002": {"id": "1002", "username": "asharma", "email": "asharma@company.com", "status": "active"}
}

# Health check endpoint - connectors usually ping this first
@app.route("/health", methods=["GET"])
def health_check():
    return jsonify({"status": "ok"}), 200

# Get all users - mimics a connector's "account aggregation" call
@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(list(users.values())), 200

# Get single user by ID
@app.route("/users/<user_id>", methods=["GET"])
def get_user(user_id):
    user = users.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user), 200

# Create user - mimics a connector's "provisioning" call
@app.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()
    new_id = str(1000 + len(users) + 1)
    users[new_id] = {
        "id": new_id,
        "username": data.get("username"),
        "email": data.get("email"),
        "status": "active"
    }
    return jsonify(users[new_id]), 201

# Disable user - mimics a connector's "deprovisioning" call
@app.route("/users/<user_id>/disable", methods=["POST"])
def disable_user(user_id):
    user = users.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    user["status"] = "disabled"
    return jsonify(user), 200

if __name__ == "__main__":
    app.run(debug=True, port=5000)