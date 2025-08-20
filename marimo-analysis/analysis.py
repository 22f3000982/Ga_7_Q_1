# Email: 22f3000982@ds.study.iitm.ac.in
import marimo

__generated_with = "0.14.17"
app = marimo.App(width="medium")

# Cell 1: Import marimo
@app.cell
def _():
    import marimo as mo
    import numpy as np
    import matplotlib.pyplot as plt
    return mo, np, plt

# Cell 2: Show email in notebook (Markdown)
@app.cell(hide_code=True)
def _(mo):
    mo.md("**Email:** 22f3000982@ds.study.iitm.ac.in")
    return
