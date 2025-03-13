# 🖋️ ScribbleNsense

ScribbleNsense is an intelligent platform that allows users to **draw handwritten math expressions** on a canvas and instantly see the **LaTeX-rendered output**. It uses a React-based frontend for drawing and a FastAPI backend for image processing and recognition.

---

## 🚀 Project Goals

- Enable freehand drawing of equations and symbols
- Convert drawn input into LaTeX format
- Display rendered LaTeX visually
- Maintain a clean and responsive UI
- Integrate a scalable backend for expression interpretation

---

## 🛠️ Tech Stack

| Layer     | Tools                          |
|-----------|--------------------------------|
| Frontend  | React, Vite, Tailwind CSS      |
| Backend   | FastAPI, Python, PIL           |
| Drawing   | HTML5 Canvas                   |
| Rendering | MathJax                        |
| Hosting   | Vercel (Frontend), Render (Backend) |

---

## 📁 Folder Structure

```plaintext
scribbleNsense/
├── scribbleNsense-frontend/      # React + Vite frontend
└── scribbleNsense-backend/       # FastAPI backend
