# rgr

## RUN

### With Virtualenv

	$ python3 -m venv rgr-env

Active virtualenv and run:

	$ cat websites.txt | python3 -m rgr

### With Docker

	$ docker build --tag rgr .

	$ cat websites.txt | docker run -i rgr /bin/bash -c 'cat | python3 -m rgr'


