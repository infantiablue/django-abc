# django-abc

This repo is created to learn, explore and play around django framework 3.
Notes, useful tricks, links would be documented along the way.

## Setting Up Dev Environment

### 1. ZSH Shell

Begin with this nice [tutorial](https://www.freecodecamp.org/news/how-to-configure-your-macos-terminal-with-zsh-like-a-pro-c0ab3f3c1156/).

Then, we need to upgrade to [PowerLevel10k](https://github.com/romkatv/powerlevel10k) theme for ZSH shell.

### 2. Visual Code

Default `settings.json` file:

```
{
    "editor.formatOnSave": true,
    "files.exclude": {
        "**/.git": true,
        "**/.svn": true,
        "**/.hg": true,
        "**/CVS": true,
        "**/.DS_Store": true,
        ".vscode": true,
        "**/*.pyc": true,
        ".idea/": true,
        "**/__pycache__/": true,
         "**/venv/": true,
    },
    "workbench.editor.enablePreview": false,
    "editor.minimap.enabled": false,
    "python.linting.pylintArgs": [
        "--load-plugins",
        "pylint_django"
    ],
    "python.linting.enabled": false,
    "workbench.colorTheme": "Monokai",
    "git.autofetch": true,
}
```

VSCode Extension:
* Magic Python
* Beautify
* Markdown All In One
* Remote - WSL *(Windows Only)*

Open settings.json in current workspace then, update `"python.pythonPath": "Your_venv_path/bin/python"` under workspace settings. (For Windows): Update `"python.pythonPath": "Your_venv_path/Scripts/python.exe"` under workspace settings.

Create file `.vscode/launch.json` for debug:

```
{
    "configurations": [
        {
            "name": "Python: Django",
            "type": "python",
            "request": "launch",
            "program": "${workspaceFolder}/manage.py",
            "console": "integratedTerminal",
            "args": [
                "runserver",
            ],
            "django": true
        },
    ]
}
```


## Useful Links

Database

* [How to transfer data from SQLite to another database](https://medium.com/@kenyattaanthony88/django-transfer-data-from-sqlite-to-another-database-edab51d79dfc)

