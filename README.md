# Adam Scriveyn

[But after my makyng thow wryte more trewe](https://faculty.goucher.edu/eng330/chaucers_wordes_unto_adam_his_own_scriveyn.htm)

## Prerequisites

- python >=3.13
- [pyenv](https://github.com/pyenv/pyenv)
- [pipx](https://github.com/pypa/pipx)
- [poetry](https://python-poetry.org/docs/)

## Development

### Install and run the linter

- [ruff](https://github.com/astral-sh/ruff)

```bash
  pipx install ruff
```

```bash
ruff check
```

### Run the program

```bash
poetry run adam-scriveyn
```

### Run the tests

- Run the entire test suite

```bash
poetry run pytest
```

- Run a single test file

```bash
poetry run pytest tests/test_transfer_service.py
```

- Run a single test

```bash
poetry run pytest tests/test_transfer_service.py::TestTransferService::test_initialization
```
