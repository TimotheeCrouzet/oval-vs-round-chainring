# oval-vs-round-chainring
Numerical and experimental study of pedalling torque to compare oval and round bicycle chainrings. Includes a force–angle biomechanical model, torque simulation over one cycle, and experimental measurements.

## 1. Clone the repository

Start by cloning the project to your local machine:

```bash
git clone https://github.com/TimotheeCrouzet/oval-vs-round-chainring.git
```
## Prerequisites
You need:

- **Python 3.12**
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
### Install Python 3.12 for this project
```bash
uv python install 3.12
uv python pin 3.12
```
## Environment Setup

Once `uv` and `python 3.12` are installed, create the virtual environment and install all project dependencies.

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
### Install the project in editable mode

After activating the virtual environment, install the project locally using:

```bash
uv pip install -e .
```

## 3. Run the Dashboard

To launch the Streamlit dashboard, run the following command from the project root:

```bash
uv run python main.py
```





