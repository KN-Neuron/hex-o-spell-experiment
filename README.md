# Hex-O-Spell Experiment

A pygame-based experiment that integrates GUI, egg headset, and data management components for an immersive experience.

## Project Overview

This project combines three main components:
- **GUI**: Graphical user interface for interaction
- **Egg Headset**: EEG headset integration for brain-computer interface
- **Data Manager**: System for handling and processing data

## Prerequisites

- Python 3.13 or higher
- pip for package management

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd hex-o-spell-experiment
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -U pip
   pip install -e .
   ```

For development:
   ```bash
   pip install -e ".[dev]"
   ```

## Development Setup

1. Install pre-commit hooks:
   ```bash
   pre-commit install
   ```

2. Run tests:
   ```bash
   pytest
   ```

3. Run the application:
   ```bash
   python src/main.py
   ```

## Project Structure

```
hex-o-spell-experiment/
├── src/                    # Source code
│   ├── gui/                # GUI components
│   ├── egg_headset/        # EEG headset integration
│   └── data_manager/       # Data management system
├── tests/                  # Unit and integration tests
│   ├── unit/               # Unit tests
│   └── integration/        # Integration tests
├── pyproject.toml          # Project configuration
└── README.md               # This file
```

## Testing

Unit tests are located in `tests/unit/` and integration tests in `tests/integration/`.

Run all tests:
```bash
pytest
```

Run specific test category:
```bash
pytest -m unit      
pytest -m integration
```

## Linting and Formatting

Format code:
```bash
black src/ tests/
```

Check for linting issues:
```bash
flake8 src/ tests/
```

Check for type issues:
```bash
mypy src/
```
