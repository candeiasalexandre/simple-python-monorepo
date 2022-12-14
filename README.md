#  (Simple) Python Monorepo

This repo contains an example on how to create a (simple) python monorepo containing:
- a shared lib (`libraries/library-example`)
- a project-1 using the shared library code (`projects/project-1`)
- a project-2 to test to install the artifact generated by project-1 (`projects/project-2`)

Both the projects and the shared library use poetry to manage their own dependencies.

To manage the build of the projects we use [poetry-multiproject-plugin](https://github.com/DavidVujic/poetry-multiproject-plugin).

This plugin makes it possible to include packages in the `pyproject.toml` that are not in the root of the package folder.
This means that we can distribute the project package (project + shared library) in a single `.whl`.

# How to test

- Install [poetry-multiproject-plugin](https://github.com/DavidVujic/poetry-multiproject-plugin). 
- Go to `projects/project-1` and build the project using `poetry build-project`
  - This will generate a `.whl` for the `project-1` package under `dist/`
- Go to `projects/project-2`, install `project-1` and run it:
  - `poetry run pip install ../project-1/dist/project_1-0.1.0-py3-none-any.whl --force-reinstall`
  - `poetry run project-1-cli`
    - It shoud print to the stdout:
        ```
        50
        30
        ```

# How to add libraries to projects

Check the `projects/project-1/pyproject.toml`.

```
...
[tool.poetry]
name = "project-1"
version = "0.1.0"
description = ""
authors = ["Alexandre Candeias"]
readme = "README.md"
packages = [
    {include = "project_1"},
    {include = "library_example", from="../../libraries/library-example"}
]
...
```

## How to have syntax highlighting on shared libs

You can add the library in the project venv in edit mode:
```
poetry run pip install -e ../../libraries/library-example/ --no-deps
```

# Improvement points

- Currently if you **add a dependency on the shared library the projects using it are not aware**.
  - If you have tests, it can be spotted because some imports will fail.



# Resources

https://github.com/DavidVujic/poetry-multiproject-plugin

https://github.com/DavidVujic/python-polylith