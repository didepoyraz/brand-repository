# Brand Repository

A stylish dashboard to browse and preview all your favorite fashion brand websites in one place. 📍️

---

## Project Setup

### Conda Environment
Create and activate a conda environment called `fashion`:

```bash
conda create -n fashion python=3.10
conda activate fashion
```

###  Install Requirements

```bash
pip install flask requests beautifulsoup4
```

---

## Run the App

Start the Flask server with:

```bash
python3 app.py
```

Then open your browser and go to:

👉 [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

---

## 🌐 What It Does

- Displays a visual feed of your favorite clothing brand homepages.
- Automatically generates live preview images using a screenshot API.
- Links directly to each brand’s site.
- Easily customizable brand list using a `brand_list.json` file.

---

## 📁 Project Structure

```
fashion/
├── app.py
├── brand_list.json
├── static/
│   ├── style.css
│   ├── background.jpeg
│   └── logo.png
├── templates/
│   └── index.html
```

## To-Do

- Add functionality for dynamically adding a new favorite brand
