# 🖋️ ScribbleNsense

> **Intelligent Handwritten Math Expression Recognition Platform**

ScribbleNsense is a cutting-edge web application that transforms handwritten mathematical expressions into beautifully rendered LaTeX equations. Draw your math expressions naturally on a digital canvas and watch them come to life with instant LaTeX conversion and rendering.

![Project Status](https://img.shields.io/badge/Status-Active-green)
![TypeScript](https://img.shields.io/badge/TypeScript-007ACC?logo=typescript&logoColor=white)
![React](https://img.shields.io/badge/React-20232A?logo=react&logoColor=61DAFB)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?logo=fastapi)
![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)

---

## ✨ Features

- 🎨 **Intuitive Canvas Drawing** - Natural freehand drawing experience with smooth brush strokes
- 🔍 **AI-Powered Recognition** - Advanced image processing to recognize mathematical symbols and expressions
- 📐 **LaTeX Conversion** - Instant conversion of drawings to proper LaTeX mathematical notation
- 🎯 **Real-time Rendering** - Live preview of rendered mathematical expressions using MathJax
- 📱 **Responsive Design** - Seamless experience across desktop. tablet, and mobile-- require improvements
- ⚡ **Fast Performance** - Optimized with Vite for lightning-fast development and production builds
- 🎨 **Modern UI** - Beautiful, accessible interface built with Tailwind CSS and shadcn/ui components

---

## 🛠️ Tech Stack

### Frontend
- **Framework**: React 18 with TypeScript
- **Build Tool**: Vite
- **Styling**: Tailwind CSS
- **UI Components**: shadcn/ui
- **Canvas**: HTML5 Canvas API
- **Math Rendering**: MathJax
- **HTTP Client**: Axios

### Backend
- **Framework**: FastAPI
- **Language**: Python 3.10+
- **Image Processing**: Pillow (PIL)
- **Data Validation**: Pydantic
- **CORS**: FastAPI CORS middleware

### Development & Deployment
- **Package Manager**: npm/yarn, pip
- **Linting**: ESLint
- **Code Formatting**: Prettier
- **Frontend Hosting**: Vercel
- **Backend Hosting**: Render
- **Version Control**: Git

---

## 📁 Project Structure

```plaintext
scribbleNsense/
├── 📂 scribbleNsense-frontend/          # React + TypeScript frontend
│   ├── 📂 public/                       # Static assets
│   ├── 📂 src/
│   │   ├── 📂 components/              # Reusable UI components
│   │   │   └── 📂 ui/                  # shadcn/ui components
│   │   ├── 📂 screens/                 # Main application screens
│   │   │   └── 📂 home/               # Home page with canvas
│   │   ├── 📂 lib/                     # Utility functions
│   │   ├── 📂 assets/                  # Images and icons
│   │   ├── 📄 App.tsx                  # Main app component
│   │   ├── 📄 main.tsx                 # React entry point
│   │   └── 📄 constants.ts             # App constants
│   ├── 📄 package.json                 # Dependencies and scripts
│   ├── 📄 vite.config.ts              # Vite configuration
│   ├── 📄 tailwind.config.js          # Tailwind CSS config
│   └── 📄 tsconfig.json               # TypeScript config
├── 📂 scribbleNsense-backend/           # FastAPI Python backend
│   ├── 📂 apps/
│   │   └── 📂 calculator/              # Calculator module
│   │       ├── 📄 route.py            # API routes
│   │       └── 📄 utils.py            # Utility functions
│   ├── 📄 main.py                      # FastAPI application
│   ├── 📄 schema.py                    # Pydantic models
│   ├── 📄 constants.py                 # Backend constants
│   ├── 📄 requirements.txt             # Python dependencies
│   └── 📄 .env                        # Environment variables
├── 📄 README.md                        # This file
└── 📄 .gitignore                       # Git ignore rules
```

---

## 🚀 Quick Start

### Prerequisites

- **Node.js** 18+ and npm/yarn
- **Python** 3.10+
- **Git**

### 1. Clone the Repository

```bash
git clone https://github.com/shailendra-iiitm/scribbleNsense
cd scribbleNsense
```

### 2. Backend Setup

```bash
# Navigate to backend directory
cd scribbleNsense-backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Edit .env with your configuration

# Run the backend server
python main.py
```

The backend will be available at `http://localhost:8000`

### 3. Frontend Setup

```bash
# Navigate to frontend directory (in a new terminal)
cd scribbleNsense-frontend

# Install dependencies
npm install

# Set up environment variables
cp .env.example .env
# Edit .env with your backend URL

# Start development server
npm run dev
```

The frontend will be available at `http://localhost:5173`

![O/P](image.png)

---

## 📖 API Documentation

### Base URL
- **Development**: `http://localhost:8000`
- **Production**: `https://your-backend-url.com`

### Endpoints

#### `POST /calculate`
Process handwritten mathematical expression

**Request Body:**
```json
{
  "image": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAA...",
  "dict_of_vars": {}
}
```

**Response:**
```json
{
  "expr": "x^2 + 2x + 1",
  "result": "LaTeX rendered result",
  "assign": false
}
```

### Data Models

#### ImageData
```python
class ImageData(BaseModel):
    image: str          # Base64 encoded image string
    dict_of_vars: dict  # Variable assignments
```

---

## 🎯 Usage

1. **Open the Application** - Navigate to the frontend URL in your browser
2. **Draw Your Expression** - Use your mouse or touch to draw mathematical expressions on the canvas
3. **Process** - Click the "RUN" button to send your drawing for recognition
4. **View Results** - See the recognized LaTeX expression and its rendered output
5. **Clear & Repeat** - Use the clear button to start over with a new expression

### Supported Mathematical Elements

- ✅ Basic arithmetic: `+`, `-`, `×`, `÷`
- ✅ Exponents and subscripts: `x²`, `a₁`
- ✅ Fractions: `1/2`, `(a+b)/c`
- ✅ Greek letters: `α`, `β`, `π`, `θ`
- ✅ Functions: `sin`, `cos`, `log`, `√`
- ✅ Parentheses and brackets
- ✅ Integrals and summations

---

## 🛠️ Development

### Available Scripts (Frontend)

```bash
npm run dev          # Start development server
npm run build        # Build for production
npm run preview      # Preview production build
npm run lint         # Run ESLint
npm run type-check   # Run TypeScript type checking
```

### Available Scripts (Backend)

```bash
python main.py       # Start development server
pip freeze > requirements.txt  # Update dependencies
pytest              # Run tests (if implemented)
```

### Environment Variables

#### Frontend (.env)
```env
VITE_API_BASE_URL=http://localhost:8000
VITE_APP_NAME=ScribbleNsense
```

#### Backend (.env)
```env
PORT=8000
ENVIRONMENT=development
CORS_ORIGINS=["http://localhost:5173"]
```

---

## 🚀 Deployment

### 🔧 Pre-deployment Checklist

Before deploying, ensure your project is ready:

```bash
# 1. Test locally first
cd scribbleNsense-backend && python main.py
cd ../scribbleNsense-frontend && npm run build

# 2. Commit all changes
git add .
git commit -m "Ready for deployment"
git push origin main
```

---

### 🎯 Frontend Deployment (Vercel)

#### Step 1: Prepare Your Frontend

1. **Update your frontend environment variables** in `scribbleNsense-frontend/.env`:
```env
VITE_API_BASE_URL=https://your-backend-url.onrender.com
VITE_APP_NAME=ScribbleNsense
```

2. **Ensure your build works locally**:
```bash
cd scribbleNsense-frontend
npm run build
npm run preview
```

#### Step 2: Deploy to Vercel

1. **Go to [Vercel Dashboard](https://vercel.com/dashboard)**
2. **Click "New Project"**
3. **Import from GitHub**:
   - Select your `scribbleNsense` repository
   - Choose "Import"

4. **Configure Project Settings**:
   ```
   Framework Preset: Vite
   Root Directory: scribbleNsense-frontend
   Build Command: npm run build
   Output Directory: dist
   Install Command: npm install
   ```

5. **Set Environment Variables**:
   - Go to Project Settings → Environment Variables
   - Add:
     ```
     VITE_API_BASE_URL = https://your-backend-url.onrender.com
     VITE_APP_NAME = ScribbleNsense
     ```

6. **Deploy**:
   - Click "Deploy"
   - Wait for deployment to complete
   - Your frontend will be available at `https://your-project-name.vercel.app`

#### Step 3: Auto-deployment Setup

- ✅ **Automatic deployments** are enabled by default
- ✅ **Every push to `main`** triggers a new deployment
- ✅ **Preview deployments** for pull requests

---

### ⚙️ Backend Deployment (Render)

#### Step 1: Prepare Your Backend

1. **Create a `render.yaml` file** in your project root (optional but recommended):
```yaml
services:
  - type: web
    name: scribblensense-backend
    env: python
    buildCommand: "cd scribbleNsense-backend && pip install -r requirements.txt"
    startCommand: "cd scribbleNsense-backend && python main.py"
    envVars:
      - key: PYTHON_VERSION
        value: 3.10.0
      - key: PORT
        value: 8000
```

2. **Update your backend for production** in `scribbleNsense-backend/main.py`:
```python
import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Update CORS for production
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://your-frontend-url.vercel.app",
        "http://localhost:5173"  # Keep for local development
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port)
```

#### Step 2: Deploy to Render

1. **Go to [Render Dashboard](https://render.com/dashboard)**
2. **Click "New +" → "Web Service"**
3. **Connect GitHub Repository**:
   - Select your `scribbleNsense` repository
   - Click "Connect"

4. **Configure Service Settings**:
   ```
   Name: scribblensense-backend
   Environment: Python 3
   Build Command: cd scribbleNsense-backend && pip install -r requirements.txt
   Start Command: cd scribbleNsense-backend && python main.py
   ```

5. **Set Environment Variables**:
   - Scroll down to "Environment Variables"
   - Add:
     ```
     PORT = 8000
     PYTHON_VERSION = 3.10.0
     ENVIRONMENT = production
     CORS_ORIGINS = ["https://your-frontend-url.vercel.app"]
     ```

6. **Deploy**:
   - Click "Create Web Service"
   - Wait for build and deployment (5-10 minutes)
   - Your backend will be available at `https://your-service-name.onrender.com`

#### Step 3: Update Frontend with Backend URL

Once your backend is deployed:

1. **Copy your Render backend URL** (e.g., `https://scribblensense-backend.onrender.com`)
2. **Update Vercel environment variables**:
   - Go to Vercel Dashboard → Your Project → Settings → Environment Variables
   - Update `VITE_API_BASE_URL` to your Render URL
3. **Redeploy frontend** (automatically triggers on environment variable change)

---

### 🔄 Complete Deployment Workflow

#### Initial Deployment:

```bash
# 1. Deploy backend first
# - Follow Render steps above
# - Note down your backend URL

# 2. Update frontend environment
# - Update VITE_API_BASE_URL in Vercel
# - Deploy frontend to Vercel

# 3. Update backend CORS
# - Add your Vercel URL to CORS origins
# - Redeploy backend on Render
```

#### For Updates:

```bash
# Simple workflow for updates
git add .
git commit -m "Your update message"
git push origin main

# Both services will auto-deploy! 🎉
```

---

### 🛠️ Troubleshooting Deployment

#### Common Issues:

**❌ CORS Errors:**
```python
# In main.py, ensure your frontend URL is in CORS origins
allow_origins=[
    "https://your-actual-vercel-url.vercel.app",
    "http://localhost:5173"
]
```

**❌ Build Failures on Render:**
```bash
# Check your requirements.txt has all dependencies
pip freeze > requirements.txt
```

**❌ Environment Variables Not Working:**
```bash
# Make sure environment variables are set in both:
# - Vercel (for frontend)
# - Render (for backend)
```

**❌ Port Issues on Render:**
```python
# Use environment PORT variable
port = int(os.environ.get("PORT", 8000))
uvicorn.run("main:app", host="0.0.0.0", port=port)
```

#### Health Check URLs:

- **Backend Health**: `https://your-backend.onrender.com/docs`
- **Frontend Health**: `https://your-frontend.vercel.app`

---

### 📱 Production URLs

After successful deployment:

- **🌐 Frontend**: `https://scribblensense.vercel.app`
- **⚙️ Backend**: `https://scribblensense-backend.onrender.com`
- **📚 API Docs**: `https://scribblensense-backend.onrender.com/docs`

### 💡 Pro Tips

- 🔄 **Auto-deployments** save time - every git push deploys automatically
- 🔍 **Monitor logs** in both Vercel and Render dashboards for issues
- ⚡ **Render free tier** may sleep after 15 minutes of inactivity
- 🚀 **Use custom domains** for professional URLs
- 🔒 **Set up HTTPS** automatically on both platforms

---

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. **Commit** your changes (`git commit -m 'Add amazing feature'`)
4. **Push** to the branch (`git push origin feature/amazing-feature`)
5. **Open** a Pull Request



## 📝 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

## 👥 Authors & Contributors

<table>
  <tr>
    <td align="center">
      <a href="https://github.com/Anisha1121">
        <img src="https://github.com/Anisha1121.png" width="100px;" alt="Anisha Dwivedi"/>
        <br />
        <sub><b>Anisha Dwivedi</b></sub>
      </a>
      <br />
      <span title="Code">💻</span> <span title="Frontend">🎨</span> <span title="UI/UX">🎯</span>
    </td>
    <td align="center">
      <a href="https://github.com/shailendra-iiitm">
        <img src="https://github.com/shailendra-iiitm.png" width="100px;" alt="Shailendra Shukla"/>
        <br />
        <sub><b>Shailendra Shukla</b></sub>
      </a>
      <br />
      <span title="Code">💻</span> <span title="Architecture">🏗️</span> <span title="Backend">⚙️</span>
    </td>
    
  </tr>
</table>

---

## 📞 Support & Contact

- 🐛 **Bug Reports**: [Create an Issue](https://github.com/shailendra-iiitm/scribbleNsense/issues)
- 💡 **Feature Requests**: [Create an Issue](https://github.com/shailendra-iitm/scribbleNsense/issues)
- 📧 **Email**: shailendraiiits@example.com ,anishas1121@gmail.co

---

## 🙏 Acknowledgments

- **MathJax** for mathematical rendering
- **shadcn/ui** for beautiful UI components  
- **FastAPI** for the excellent Python web framework
- **Vite** for blazing fast build tooling
- **Tailwind CSS** for utility-first styling
- All contributors and supporters of this project

---

<div align="center">
  <p>⭐ Star this repo if you find it helpful!</p>
</div>
index-BHlLN_0R.js:74 
 
 POST https://scribble-n-sense.vercel.app/undefined/calculate/upload-base64 404 (Not Found)
index-BHlLN_0R.js:74 
 Uncaught (in promise) 
Q {message: 'Request failed with status code 404', name: 'AxiosError', code: 'ERR_BAD_REQUEST', config: {…}, request: XMLHttpRequest, …}
code
: 
"ERR_BAD_REQUEST"
config
: 
{transitional: {…}, adapter: Array(3), transformRequest: Array(1), transformResponse: Array(1), timeout: 0, …}
message
: 
"Request failed with status code 404"
name
: 
"AxiosError"
request
: 
XMLHttpRequest
onabort
: 
ƒ ()
onerror
: 
ƒ ()
onload
: 
null
onloadend
: 
ƒ m()
onloadstart
: 
null
onprogress
: 
null
onreadystatechange
: 
null
ontimeout
: 
ƒ ()
readyState
: 
4
response
: 
"{\"error\": {\"code\": \"404\", \"message\": \"The page could not be found\"}}"
responseText
: 
"{\"error\": {\"code\": \"404\", \"message\": \"The page could not be found\"}}"
responseType
: 
""
responseURL
: 
"https://scribble-n-sense.vercel.app/undefined/calculate/upload-base64"
responseXML
: 
null
status
: 
404
statusText
: 
""
timeout
: 
0
upload
: 
XMLHttpRequestUpload {onloadstart: null, onprogress: null, onabort: null, onerror: null, onload: null, …}
withCredentials
: 
false
[[Prototype]]
: 
XMLHttpRequest
response
: 
{data: {…}, status: 404, statusText: '', headers: ut, config: {…}, …}
status
: 
404
stack
: 
"AxiosError: Request failed with status code 404\n    at yg (https://scribble-n-sense.vercel.app/assets/index-BHlLN_0R.js:74:1030)\n    at XMLHttpRequest.m (https://scribble-n-sense.vercel.app/assets/index-BHlLN_0R.js:74:6056)\n    at tr.request (https://scribble-n-sense.vercel.app/assets/index-BHlLN_0R.js:76:1952)\n    at async https://scribble-n-sense.vercel.app/assets/index-BHlLN_0R.js:79:15612"
[[Prototype]]
: 
Error