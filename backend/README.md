# PBAD - backend

## Setup

In `backend` directory run:

### Windows

```
py -3 -m venv .venv
```

```
.venv\scripts\activate
```

```
python -m pip install -r requirements.txt
```

### macOS/Linux

```
python3 -m venv .venv
```

```
source .venv/bin/activate
```

```
python3 -m pip install -r requirements.txt
```

## Installing new packages

In `backend` directory with activated virtual environment run:

### Windows

```
python -m pip install -r <package_name>
```

Before commit run:

```
python -m pip freeze > requirements.txt
```

### macOS/Linux

```
python3 -m pip install -r <package_name>
```

Before commit run:

```
python3 -m pip freeze > requirements.txt
```
