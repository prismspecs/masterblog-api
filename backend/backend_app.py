from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Hardcoded list of blog posts
POSTS = [
    {"id": 1, "title": "First post", "content": "This is the first post."},
    {"id": 2, "title": "Second post", "content": "This is the second post."},
]


@app.route('/api/posts', methods=['GET'])
def get_posts():
    """Retrieve all blog posts."""
    return jsonify(POSTS)


@app.route('/api/posts', methods=['POST'])
def add_post():
    """Add a new blog post."""
    data = request.get_json()

    # Validate input
    if not data or "title" not in data or "content" not in data:
        return jsonify({"error": "Title and content are required."}), 400

    # Generate a new unique ID
    new_id = max([post["id"] for post in POSTS], default=0) + 1
    new_post = {
        "id": new_id,
        "title": data["title"],
        "content": data["content"]
    }

    # Add the new post
    POSTS.append(new_post)

    return jsonify(new_post), 201  # 201 Created


@app.route('/api/posts/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    """Delete a blog post by ID."""
    global POSTS
    post = next((post for post in POSTS if post["id"] == post_id), None)

    if post is None:
        return jsonify({"error": f"Post with id {post_id} not found."}), 404

    # Remove the post
    POSTS = [post for post in POSTS if post["id"] != post_id]

    return jsonify({"message": f"Post with id {post_id} has been deleted successfully."}), 200


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5002, debug=True)
