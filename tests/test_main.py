from fastapi.testclient import TestClient
from app.main import app
from pathlib import Path

client = TestClient(app)


def test_index():
    r = client.get('/')
    assert r.status_code == 200
    assert '<h1>Available Notebooks</h1>' in r.text


def test_upload_and_view(tmp_path, monkeypatch):
    # create a minimal notebook
    nb_content = '{"cells": [], "metadata": {}, "nbformat": 4, "nbformat_minor": 5}'
    file = tmp_path / 'sample.ipynb'
    file.write_text(nb_content)

    with open(file, 'rb') as f:
        r = client.post('/api/notebooks', data={'name': 'sample'}, files={'file': ('sample.ipynb', f, 'application/json')})
    assert r.status_code == 200
    r = client.get('/notebook/sample')
    assert r.status_code == 200
    assert 'sample' in r.text
