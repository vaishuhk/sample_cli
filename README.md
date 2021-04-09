# sample_cli
##### Install Virtual ENV for Python Project
```
cd ../cli_sample
sudo -H pip3 install --upgrade pip
sudo -H pip3 install virtualenv
```
##### Install packages in Virtual ENV
```
virtualenv -p python3 sample_cli_env

To activate: source sample_cli_env/bin/activate
To deactivate: deactivate

```

##### Or Use venv 
```
Follow this
https://docs.python.org/3/library/venv.html
```

#### After activating venv (or sample_cli_env) environment install required dependencies by following command:  
`pip install -r requirements.txt`

#### Create .env and add request KEY in .env file 
```
$ touch .env
$ cp .env.sample .env
```

#### Get Commands
```
$ cd ../sample_cli/app
$ python apis_cli.py --help
Usage: apis [OPTIONS] COMMAND [ARGS]...

  A CLI wrapper for the API of Public APIs.

Options:
  --help  Show this message and exit.

Commands:
  create-entity  Create new entities
  filter-user    Filter users (entities)
  search         List all search entities

```

#### Create UserEntity by filling data
```
$ cd app 
$ python apis_cli.py create-entity

```


#### Filter Users
```
$ python apis_cli.py filter-user
```

#### Search Users
```
$ python apis_cli.py search
```
