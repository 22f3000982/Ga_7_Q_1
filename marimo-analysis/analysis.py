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

# Cell 2: Show email in notebook
@app.cell(hide_code=True)
def _(mo):
    mo.md("**Email:** 22f3000982@ds.study.iitm.ac.in")
    return

# Cell 3: Create interactive widget (slider)
@app.cell
def _(mo):
    # Slider to control sample size
    sample_size = mo.ui.slider(10, 500, value=100, label="Select sample size")
    sample_size
    return sample_size

# Cell 4: Generate data depending on slider
@app.cell
def _(np, sample_size):
    # Data generation depends on slider value
    data = np.random.normal(loc=50, scale=10, size=sample_size.value)
    return data

# Cell 5: Plot histogram (depends on generated data)
@app.cell
def _(plt, data):
    fig, ax = plt.subplots()
    ax.hist(data, bins=20, color="skyblue", edgecolor="black")
    ax.set_title("Histogram of Generated Data")
    ax.set_xlabel("Value")
    ax.set_ylabel("Frequency")
    fig
    return fig

# Cell 6: Dynamic Markdown (depends on slider + data)
@app.cell
def _(mo, data, sample_size, np):
    mean = np.mean(data)
    stddev = np.std(data)
    # Dynamic markdown shows stats and reacts to slider
    mo.md(f"""
    ## Data Summary  
    - Sample Size: **{sample_size.value}**  
    - Mean: **{mean:.2f}**  
    - Std Dev: **{stddev:.2f}**  

    {"🟢" * (sample_size.value // 20)}
    """)
    return

if __name__ == "__main__":
    app.run()
