Here's a **README.md** for your Flask Blog API project:  

---

# 📜 Flask Blog API  

A simple RESTful API for managing blog posts, built with Flask. The API supports **listing, searching, sorting, adding, updating, and deleting** blog posts.

---

## 🚀 Features  

✔ **List all posts** (`GET /api/posts`)  
✔ **Search posts by title or content** (`GET /api/posts/search?title=...&content=...`)  
✔ **Sort posts** (`GET /api/posts?sort=title&direction=asc`)  
✔ **Add a new post** (`POST /api/posts`)  
✔ **Update an existing post** (`PUT /api/posts/<id>`)  
✔ **Delete a post** (`DELETE /api/posts/<id>`)  
✔ **CORS enabled** for frontend compatibility  

---

## 🛠 Installation & Setup  

### 1️⃣ **Clone the Repository**  
```sh
git clone https://github.com/prismspecs/masterblog-api.git
cd masterblog-api
```

### 2️⃣ **Create a Virtual Environment**  
```sh
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3️⃣ **Install Dependencies**  
```sh
pip install flask flask-cors
```

### 4️⃣ **Run the API**  
```sh
python3 backend/backend_app.py
```
The API will be available at **http://127.0.0.1:5002/**.

---

## 🏗 API Endpoints  

### 📌 **List All Posts**  
- **GET** `/api/posts`  
- **Query Parameters (optional)**:  
  - `sort` → `"title"` or `"content"`  
  - `direction` → `"asc"` or `"desc"`  
- **Example**:  
  ```
  GET /api/posts?sort=title&direction=desc
  ```
- **Response (JSON)**:  
  ```json
  [
      {"id": 1, "title": "First post", "content": "This is the first post."},
      {"id": 2, "title": "Second post", "content": "This is the second post about Flask."}
  ]
  ```

---

### 🔍 **Search Posts**  
- **GET** `/api/posts/search?title=flask&content=guide`  
- **Response (JSON)**:  
  ```json
  [
      {"id": 3, "title": "Flask Guide", "content": "A beginner's guide to Flask API development."}
  ]
  ```

---

### ➕ **Add a New Post**  
- **POST** `/api/posts`  
- **Request Body (JSON)**:  
  ```json
  {
      "title": "New Blog Post",
      "content": "This is the content of the new post."
  }
  ```
- **Response (201 Created)**:  
  ```json
  {
      "id": 4,
      "title": "New Blog Post",
      "content": "This is the content of the new post."
  }
  ```

---

### ✏ **Update an Existing Post**  
- **PUT** `/api/posts/<id>`  
- **Request Body (JSON) - Only provide fields to update**:  
  ```json
  {
      "title": "Updated Blog Post"
  }
  ```
- **Response (200 OK)**:  
  ```json
  {
      "id": 2,
      "title": "Updated Blog Post",
      "content": "This is the second post about Flask."
  }
  ```

---

### ❌ **Delete a Post**  
- **DELETE** `/api/posts/<id>`  
- **Response (200 OK)**:  
  ```json
  {
      "message": "Post with id 2 has been deleted successfully."
  }
  ```

---

## 🧪 Testing with Postman  

1️⃣ **Start the API**  
```sh
python3 backend/backend_app.py
```
2️⃣ **Open Postman**  
3️⃣ **Test each endpoint** using **GET, POST, PUT, DELETE**  

---

## 🎨 Frontend Integration  

You can connect this API to a frontend (React, Vue, or a simple HTML+JS app).  
For example, with **fetch API** in JavaScript:  

```js
fetch("http://127.0.0.1:5002/api/posts")
    .then(response => response.json())
    .then(posts => console.log(posts))
    .catch(error => console.error("Error fetching posts:", error));
```

---

## 📜 License  
This project is open-source. Feel free to modify and use it as needed!  
 if you need any improvements! 😊