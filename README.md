# water-refilling-system

**Water Refilling Station Management System**.

We'll use:

- **Backend:** Python + FastAPI
- **Frontend:** React + TypeScript + Vite
- **Database:** PostgreSQL
- **IDE:** VS Code

---

# Step 1: Install Python

Download the latest stable version of Python 3.12 or newer from:

- [Python Downloads](https://www.python.org/downloads/?utm_source=chatgpt.com)

After installation, verify it:

```bash
python --version
```

or

```bash
py --version
```

Expected output:

```text
Python 3.12.x
```

---

# Step 2: Install PostgreSQL

Download PostgreSQL:

- [PostgreSQL Downloads](https://www.postgresql.org/download/?utm_source=chatgpt.com)

During installation, remember:

- Username (commonly `postgres`)
- Password
- Port (default `5432`)

Verify:

```bash
psql --version
```

---

# Step 3: Install VS Code

Download:

- [Visual Studio Code](https://code.visualstudio.com/?utm_source=chatgpt.com)

Recommended extensions:

- Python
- Pylance
- Ruff
- PostgreSQL
- Docker
- GitLens
- Thunder Client (or REST Client)
- Prisma (optional if you want to explore it later)

---

# Step 4: Install Git

Download:

- [Git](https://git-scm.com/downloads?utm_source=chatgpt.com)

Verify:

```bash
git --version
```

---

# Step 5: Install Node.js

React requires Node.js.

Download the current LTS version:

- [Node.js](https://nodejs.org/?utm_source=chatgpt.com)

Verify:

```bash
node -v

npm -v
```

---

# Step 6: Create the Project Folder

```bash
mkdir water-refilling-system

cd water-refilling-system
```

Your project will look like:

```text
water-refilling-system/
    backend/
    frontend/
```

---

# Step 7: Create the Backend

Create the folder:

```bash
mkdir backend

cd backend
```

Create a virtual environment:

**Windows**

```bash
python -m venv .venv
```

or

```bash
py -m venv .venv
```

Activate it:

**PowerShell**

```powershell
.venv\Scripts\Activate.ps1
```

**Command Prompt**

```cmd
.venv\Scripts\activate
```

You'll know it's active when you see:

```text
(.venv)
```

---

# Step 8: Install Backend Packages

Run:

```bash
pip install fastapi
```

Then:

```bash
pip install uvicorn
```

Install the database-related packages:

```bash
pip install sqlalchemy
```

```bash
pip install psycopg2-binary
```

```bash
pip install alembic
```

For data validation:

```bash
pip install pydantic-settings
```

Authentication:

```bash
pip install python-jose[cryptography]
```

Password hashing:

```bash
pip install passlib[bcrypt]
```

Environment variables:

```bash
pip install python-dotenv
```

Testing:

```bash
pip install pytest
```

A simpler alternative is to install everything at once:

```bash
pip install fastapi uvicorn sqlalchemy psycopg2-binary alembic python-jose[cryptography] passlib[bcrypt] python-dotenv pydantic-settings pytest
```

---

# Step 9: Save Dependencies

```bash
pip freeze > requirements.txt
```

---

# Step 10: Run the backend project

`uvicorn app.main:app --reload`

---

# Step 11: Create the Frontend

Go back to the project root:

```bash
cd ..
```

Create the React app:

```bash
npm create vite@latest frontend
```

Choose:

```text
React

TypeScript
```

Install dependencies:

```bash
cd frontend

npm install
```

Install additional packages:

```bash
npm install react-router-dom axios @tanstack/react-query
```

Optional styling:

```bash
npm install -D tailwindcss @tailwindcss/vite
```

---

# Step 12: Open the Whole Project

```bash
code .
```

You should have:

```text
water-refilling-system/
│
├── backend/
│
└── frontend/
```

---

# Step 13: Backend Folder Structure

Inside `backend`:

```text
backend/
│
├── app/
│   ├── api/
│   ├── core/
│   ├── database/
│   ├── models/
│   ├── schemas/
│   ├── services/
│   ├── repositories/
│   ├── middleware/
│   ├── utils/
│   └── main.py
│
├── tests/
├── .env
├── requirements.txt
└── alembic/
```

---

# Step 14: Frontend Folder Structure

```text
frontend/
│
├── src/
│   ├── pages/
│   ├── layouts/
│   ├── components/
│   ├── hooks/
│   ├── services/
│   ├── routes/
│   ├── types/
│   └── App.tsx
```

---

## Next Step

Once you've completed these installations and the project structure is ready, we can move on to **Phase 2: Building the FastAPI backend**, where we'll:

1. Configure PostgreSQL.
2. Set up SQLAlchemy.
3. Configure Alembic migrations.
4. Create the first API endpoint.
5. Connect the React frontend to the FastAPI backend.

We'll build it using production-ready practices from the beginning so the project can become a strong portfolio piece.
