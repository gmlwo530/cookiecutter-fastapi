
# Cookiecutter-FastAPI

Cookiecutter FastAPI template


## Usage

First, you should have cookiecutter in your machine. If you don't have, install it.
- Installation: [https://cookiecutter.readthedocs.io/en/1.7.2/installation.html](https://cookiecutter.readthedocs.io/en/1.7.2/installation.html)

Then, Generate FastAPI project.

```bash
$ cookiecutter https://github.com/gmlwo530/cookiecutter-fastapi.git
```

  
## Run FastAPI Project

Install pacakages

```bash
  # Using pip
  $ pip install -r requirements/local.txt

  # Using poetry
  $ poetry install
```

```bash
  # Using pip
  $ uvicorn app.main:app --reload

  # Using poetry
  $ poetry run start
```

  
## Roadmap

- [ ] Test
- [ ] CI


## License

[MIT](https://choosealicense.com/licenses/mit/)

  
## Authors

- [@gmlwo530](https://github.com/gmlwo530)

  