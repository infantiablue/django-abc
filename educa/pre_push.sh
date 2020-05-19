#!/bin/zsh
pip3 freeze > requirements.txt

#reset repo
git rm --cached -r .
git reset
git checkout .
