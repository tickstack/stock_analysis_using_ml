# stock_analysis_using_ml

## Things and their uses:
1. poetry library
2. cookiecutter library
3. Makefile


### 1. Poetry
Add poetry for library dependency resolution:

#### Command to create new poetry project
```bash
poetry new porject_name
```
#### Command to initiate poetry in existing project
```bash
poetry init
```
#### Command to add library
```bash
poetry add library_name
```
#### Command to activate virtual env
```bash
poetry shell
```

#### Command to de-activate virtual env
```bash
exit
```

#### To install dependency
```bash
poetry install
```

#### To update dependency
```bash
poetry update
```

### 2. Cookiecutter
To get formatted directory temple and use it that as start or create new as i did for data science
```bash
cookiecutter templete_name
``` 
### 3. Makefile
It's been used to make things more automated and can write full process in single command and run like below

```bash
make command
```