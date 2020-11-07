# Randomizer
is just a tool that help you to generate four (4) types of printable random objects and store them in a single file, each object will be separated by a ",". These are the 4 objects: alphabetical strings, real numbers, integers, alphanumerics.

## Backend
the backend is writen in Python using Flask framework, so you need to install it first. Simply, just do this:
```
cd backend
pip install -r requirements.txt
```

and then run it.
```
python run.py
```
the backend will serve at port 5000 (flask default)

## Frontend
this is writen using React, to serve the front end, simply:
```
cd frontend
npm install
npm run build
```
after build for production, you can serve using `serve`, install it first:
```
npm install -g serve
```
then serve to user:
```
serve -s build -p <anyport>
```
