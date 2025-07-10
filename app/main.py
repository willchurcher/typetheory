from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from starlette.requests import Request
import nbconvert
import nbformat
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
NOTEBOOKS_DIR = ROOT / "notebooks"
TEMPLATES_DIR = ROOT / "templates"

app = FastAPI()
app.mount("/static", StaticFiles(directory=NOTEBOOKS_DIR), name="static")
templates = Jinja2Templates(directory=str(TEMPLATES_DIR))


def list_notebooks():
    notebooks = []
    for path in NOTEBOOKS_DIR.iterdir():
        ipynb = path / f"{path.name}.ipynb"
        if ipynb.exists():
            notebooks.append(path.name)
    return notebooks


def render_notebook_html(name: str) -> str:
    ipynb_path = NOTEBOOKS_DIR / name / f"{name}.ipynb"
    if not ipynb_path.exists():
        return "Notebook not found"
    notebook = nbformat.read(ipynb_path, as_version=4)
    html_exporter = nbconvert.HTMLExporter()
    body, _ = html_exporter.from_notebook_node(notebook)
    return body


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    notebooks = list_notebooks()
    return templates.TemplateResponse("index.html", {"request": request, "notebooks": notebooks})


@app.get("/notebook/{name}", response_class=HTMLResponse)
async def view_notebook(name: str, request: Request):
    body = render_notebook_html(name)
    return templates.TemplateResponse("notebook.html", {"request": request, "body": body, "name": name})


@app.post("/api/notebooks")
async def upload_notebook(name: str = Form(...), file: UploadFile = File(...)):
    nb_dir = NOTEBOOKS_DIR / name
    nb_dir.mkdir(exist_ok=True, parents=True)
    ipynb_path = nb_dir / f"{name}.ipynb"
    content = await file.read()
    ipynb_path.write_bytes(content)
    return {"status": "saved", "path": str(ipynb_path)}
