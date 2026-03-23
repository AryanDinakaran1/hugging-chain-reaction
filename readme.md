# HuggingFace1

A minimal Hugging Face demo repository showcasing summarization and text generation with `transformers` pipelines in Python.

![Python](https://img.shields.io/badge/python-3.8%2B-blue.svg) ![Transformers](https://img.shields.io/badge/transformers-4.x-orange.svg) ![License](https://img.shields.io/badge/license-MIT-green.svg)

## 🚀 Project Overview

This repository contains a simple script:

- `Main.py`
  - `summarize()` uses `facebook/bart-large-cnn`
  - `text_generation()` uses `gpt2`
  - `main()` prints a sample summary

## 🛠️ Setup

1. Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the script:

```bash
python Main.py
```

## 🧪 Usage

- Summarize custom text:

```python
from Main import summarize
print(summarize("Your long paragraph here"))
```

- Generate text from a prompt:

```python
from Main import text_generation
print(text_generation("Once upon a time"))
```

## ✨ Customization

- Change the default `model` in each function to your preferred HF checkpoint.
- Add `device=0` to `pipeline(...)` to run on GPU (if available).
- Expand the script with input CLI parsing or a web UI.

## 📌 Notes

- `transformers` downloads models the first time it runs, so ensure network access.
- Keep `torch` and `transformers` versions aligned in `requirements.txt`.

## 📜 License

MIT License
