# ML Buddy

Experience the power of machine learning without any coding expertise with our all-in-one platform designed to provide
hands-on training and practice..

This project uses Poetry for package management and includes a pre-commit hook that enforces code quality and style
guidelines.

## Installation

1. Clone this repository: `git clone https://github.com/AsiriAmalk/ML_BUDDY.git`
2. Navigate to the project directory: `cd ML_BuDDY`
3. Create a virtual environment: `python -m venv .venv`
4. Activate the virtual environment:
    - On Windows: `.venv\Scripts\activate.bat`
    - On Unix or Linux: `source .venv/bin/activate`
5. Install Poetry (if not already
   installed): `curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -`
6. Install the required packages: `poetry install`
7. Run migrations: `python manage.py migrate`
8. Start the development server: `python manage.py runserver`

## Next, install the pre-commit hook:

```bash
pre-commit install
````

Now, whenever you make a commit, the pre-commit hook will automatically run and check your code for issues.

## Pre-Commit Hook

The pre-commit hook for this project includes the following checks:

1. flake8 (Python linter)
2. pylint (Python code analyzer)
3. black (Python code formatter)
4. isort (Python import sorter)

To modify the pre-commit hook or add additional checks, update the .pre-commit-config.yaml file in the root directory of
this project.

###### To manually run the pre-commit hook and check for any issues before committing, you can use the following command:

```bash
pre-commit run --all-files
```

###### Alternatively, you can run the pre-commit hook on specific files by specifying their paths:

```bash
pre-commit run --files path/to/file1.py path/to/file2.py
```

This will only run the pre-commit hook on file1.py and file2.py.

***Note that if the pre-commit hook fails, it will prevent you from committing your changes until you resolve the
issues.

## Usage

1. Open your web browser and go to http://localhost:8000/
2. [Insert usage instructions here]

## Credits

This project was created by [Asiri Amal](http://www.asiriamal.com/).

## License

[This is a Open Source Software, Updated 2023 March]
