# oval-vs-round-chainring
Numerical and experimental study of pedalling torque to compare oval and round bicycle chainrings. Includes a force–angle biomechanical model, torque simulation over one cycle, and experimental measurements.

## Prerequisites
You need:

- **Python 3.10+**
- **uv** installed on your system

### Install uv
Cas général: 
```bash 
pip install uv
```

#### macOS (recommended)
```bash
brew install uv
```

#### Linux
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

#### Windows (Powershell)
```bash
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### Verify installation
```bash
uv --version
```
## Environment Setup

Once `uv` is installed, create the virtual environment and install all project dependencies.

### 1. Install dependencies and create the environment
```bash
uv sync
```

### Activate the environment

#### macOS / Linux
```bash
source .venv/bin/activate
```
#### Windows
```bash
.venv\Scripts\activate
```

## 3. Run the Dashboard

To launch the Streamlit dashboard, run the following command from the project root:

```bash
uv run python main.py
```





