
# Python API Development with FastAPI

A streamlined introduction to building APIs using FastAPI, perfect for developers looking to create fast and efficient web APIs in Python.

## Project Overview

This project provides a basic structure for developing APIs with FastAPI, covering setup, virtual environment management, and running the API. Ideal for developers interested in a minimal, high-performance Python API framework.

## Quick Start Example

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

```

## Installation Guide

#### 1. Install Python and Set Up a Virtual Environment
Using a virtual environment is essential for managing project dependencies effectively.

```bash
$ python -m venv .venv
```

#### 2. Activate the Virtual Environment
Activate the environment to use it for installing packages.

```bash
$ source .venv/bin/activate
```

Verify that the virtual environment is active by running:

```bash
$ which python

/home/user/code/awesome-project/.venv/bin/python
```

#### 3. Upgrade pip

Upgrading pip can help avoid unexpected issues when installing packages.

```bash
$ python -m pip install --upgrade pip
```

#### 4. Add .gitignore

If you're using Git, add .gitignore to prevent tracking virtual environment files.

```bash
$ echo "*" > .venv/.gitignore
```

#### 5. Install Packages Directly

To install FastAPI directly:

```bash
$ pip install "fastapi[standard]"
```

Alternatively, if you have a requirements.txt file:

```bash
$ pip install -r requirements.txt
```

## Running the Application

Once your virtual environment is set up and activated, start the FastAPI application with:

```bash
$ uvicorn main:app --reload
```
