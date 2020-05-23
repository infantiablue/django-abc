# About This Repo

This repo is created to learn, explore and play around django framework 3.
Notes, useful tricks, links would be documented along the way.

- [About This Repo](#about-this-repo)
  - [Setting Up Dev Environment](#setting-up-dev-environment)
    - [1. ZSH Shell](#1-zsh-shell)
    - [2. Visual Code](#2-visual-code)
  - [Github](#github)
  - [Useful Links](#useful-links)
  - [Azure Configuration](#azure)
  - [SAAS](#saas)

## Setting Up Dev Environment

### 1. ZSH Shell

Begin with this nice [tutorial](https://www.freecodecamp.org/news/how-to-configure-your-macos-terminal-with-zsh-like-a-pro-c0ab3f3c1156/).

Then, we need to upgrade to [PowerLevel10k](https://github.com/romkatv/powerlevel10k) theme for ZSH shell.

### 2. Visual Code

Default `settings.json` file:

```js
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

**VSCode Extension:**

- Magic Python
- Beautify
- Markdown All In One
- Remote - WSL *(Windows Only)*
- Markdownlint
- Django
- Visual IntelliCode

Open settings.json in current workspace then, update `"python.pythonPath": "Your_venv_path/bin/python"` under workspace settings. (For Windows): Update `"python.pythonPath": "Your_venv_path/Scripts/python.exe"` under workspace settings.

Create file `.vscode/launch.json` (in current workspace) for debug:

```js
{
    "configurations": [{
        "name": "Python: Django",
        "type": "python",
        "request": "launch",
        "program": "${workspaceFolder}/manage.py",
        "console": "integratedTerminal",
        "args": [
            "runserver",
            //change the settings between local and pro
            "--settings=bookmarks.settings.local",
        ],
        "django": true
    }, ]
}
```

and then add Python interpreter in `.vscode/settings.json` (in current workspace): 

```js
{
    "python.pythonPath": "env/bin/python",
}
```

## Github

[Use SSH keys to authenticate](https://help.github.com/en/github/authenticating-to-github/adding-a-new-ssh-key-to-your-github-account)

Re-Checkout:

```git
git rm --cached -r .
git reset
git checkout .
```
[Guide](https://rogerdudler.github.io/git-guide/index.vi.html)

Force Pull:

```git
git fetch --all
git reset --hard origin/master
```

## Useful Links

Database

- [How to transfer data from SQLite to another database](https://medium.com/@kenyattaanthony88/django-transfer-data-from-sqlite-to-another-database-edab51d79dfc)
- [11 rules to design database](https://www.codeproject.com/Articles/359654/11-important-database-designing-rules-which-I-fo-2)
- [How to design database](https://viblo.asia/p/lam-the-nao-de-thiet-ke-mot-co-so-du-lieu-phan-1-rYvGwavgKVw)

## Azure
- [Use SSH keys to connect VM server](https://docs.microsoft.com/en-us/azure/virtual-machines/linux/create-ssh-keys-detailed)

## SAAS
- [RabbitMQ](https://www.cloudamqp.com/plans.html)
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTA4MjY5MDg2MSwtOTYzMjg4MjRdfQ==
-->
