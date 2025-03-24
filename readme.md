# Pub-Sub File Upload System

This project implements a **Pub-Sub mechanism** using a **queue** to manage file uploads and notify subscribers about the upload status.


## Tech Stack

* **Backend:** Flask 
* **Frontend:** React

## How It Works

1. The frontend allows users to upload files.
2. The backend processes the uploads using a queue.
3. Subscribers receive real-time updates on the file upload status.
4. The frontend displays the status to the user.



## 🚀 Getting Started

### 1️⃣ Start the Backend (Flask)

#### **Step 1: Navigate to the backend folder**

```sh
cd flask_pubsub
```

**Step 2: Create and activate a virtual environment (Optional)**

```sh

# Windows

python -m venv venv

venv\\Scripts\\activate

# macOS/Linux

python3 -m venv venv

source venv/bin/activate
```

**Step 3: Install dependencies**

```sh
pip install -r requirements.txt
```

**Step 4: Run the Flask server**

```sh
python app.py
```

By default, the backend runs on <http://localhost:5000>.

**If you want to use a different port, run:**

```sh
python app.py --port 8000
```

**2️⃣ Start the Frontend (React)**

**Step 1: Navigate to the frontend folder**

```sh
cd react_file_pubsub
```

**Step 2: Install dependencies (if not installed)**

```sh
npm install
```
**Step 3: Update the backend URL (if needed)**

If your backend is running on a port other than **5000**, update the backend URL in:  
react_file_pubsub/src/FileUpload.js

```js

const BACKEND_URL = "<http://localhost:5000>"; // Change 5000 to your backend port
```

**Step 4: Start the React server**

```sh
npm start
```

By default, the frontend runs on **<http://localhost:3000>**.


**🔍 Verify the Setup**

- Open **<http://localhost:3000>** in your browser.
- Upload a file and check if the **Flask backend** receives the request.
- If using a different backend port, ensure FileUpload.js is updated accordingly.

## Inspired By

This implementation was inspired by the blog post: 🔗 [**Flask SSE Without Dependencies**](https://maxhalford.github.io/blog/flask-sse-no-deps/) by Max Halford.

## Author

👨‍💻 **Pradip Waghela**  
📧 pradip.waghela787@gmail.com  
🔗 [GitHub](https://github.com/pradipwaghela)
