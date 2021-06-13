import os
import shutil


def remove(filepath):
    if os.path.isfile(filepath):
        os.remove(filepath)
    elif os.path.isdir(filepath):
        shutil.rmtree(filepath)


if "{{ cookiecutter.package_management }}" == "pip":
    remove(os.path.join(os.getcwd(), "{{cookiecutter.project_slug}}", "pyproject.toml"))
elif "{{ cookiecutter.package_management }}" == "poetry":
    remove(os.path.join(os.getcwd(), "{{cookiecutter.project_slug}}", "requirements"))


print("Done!! Now, you can develop FastAPI project!!")