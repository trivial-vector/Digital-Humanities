# Karika's Folder

## Goals for this folder:

This is where the backend will take shape: All the serverside wizardry that makes the world go 'round and the pages load. If you have a 404 error, turn your computer off and on again. It's not Karika's fault, it's the fact you're still using Internet Explorer.

## Rules for this folder:

```
mkdir project && cd project

git init

mkdir -p DB templates static/js static/css && touch __init__.py Procfile requirements.txt app.py templates/index.html static/js/main.js static/css/style.css

conda create -n project python=3.7 anaconda
pip install pymongo flask
source activate project

echo pip freeze > requirements.txt

git add -A && git commit -m "init commit-Karika =)"
git push

```

If the above doesn't make sense to you, turn back, this is probably not your folder. If it does, well then, hello Karika!
