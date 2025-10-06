# simple_prj_on_api
# Fruit List App (FastAPI + HTML Frontend)

This is a simple demo application built with FastAPI and a minimal HTML frontend to showcase a basic fruit list API.  
The backend provides REST endpoints to get a list of fruits, add a new fruit, and a simple hello endpoint.  
The frontend is a minimal plain HTML+JavaScript page to interact with the backend visually.

---

## Features

- **FastAPI backend** with:
  - `GET /getlist/` - Returns the current fruit list.
  - `POST /postList/` - Adds a new fruit to the list.
  - `GET /Rehan/` - A simple hello endpoint.

- **Frontend** (`index.html`):
  - Displays the fruit list fetched from the backend.
  - Allows adding a new fruit using simple input and a button.
  - Uses pure HTML, minimal CSS, and vanilla JavaScript (`fetch` API).

---
## Usage

- Click **Get Fruit List** to load current fruits from the backend.  
- Enter a fruit name in the text box and press **Add Fruit** to add a new fruit to the list.
- The page will update automatically after adding a fruit.
- The backend logs requests in the console for debugging.

---
