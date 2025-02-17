from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Hardcoded list of blog posts
POSTS = [
    {"id": 1, "title": "First post", "content": "This is the first post."},
    {"id": 2, "title": "Second post", "content": "This is the second post about Flask."},
    {"id": 3, "title": "Flask Guide", "content": "A beginner's guide to Flask API development."}
]


@app.route('/api/posts', methods=['GET'])
def get_posts():
    """Retrieve all blog posts, with optional sorting."""
    sort_by = request.args.get('sort')
    direction = request.args.get('direction', 'asc').lower()

    valid_sort_fields = {"title", "content"}
    valid_directions = {"asc", "desc"}

    if sort_by and sort_by not in valid_sort_fields:
        return jsonify({"error": f"Invalid sort field '{sort_by}'. Allowed values: 'title', 'content'."}), 400

    if direction not in valid_directions:
        return jsonify({"error": f"Invalid sort direction '{direction}'. Allowed values: 'asc', 'desc'."}), 400

    sorted_posts = POSTS[:]

    if sort_by:
        sorted_posts.sort(key=lambda post: post[sort_by], reverse=(direction == "desc"))

    return jsonify(sorted_posts), 200


@app.route('/api/posts/search', methods=['GET'])
def search_posts():
    """Search blog posts by title or content."""
    title_query = request.args.get('title', '').lower()
    content_query = request.args.get('content', '').lower()

    # Filter posts based on search parameters
    matching_posts = [
        post for post in POSTS
        if (title_query and title_query in post["title"].lower()) or
           (content_query and content_query in post["content"].lower())
    ]

    return jsonify(matching_posts), 200  # 200 OK


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


@app.route('/api/posts/<int:post_id>', methods=['PUT'])
def update_post(post_id):
    """Update a blog post by ID."""
    data = request.get_json()

    post = next((post for post in POSTS if post["id"] == post_id), None)

    if post is None:
        return jsonify({"error": f"Post with id {post_id} not found."}), 404

    # Update fields only if provided
    post["title"] = data.get("title", post["title"])
    post["content"] = data.get("content", post["content"])

    return jsonify(post), 200  # 200 OK


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5002, debug=True)
