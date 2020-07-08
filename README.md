# FastAPI demo project
[![Travis][travis-shield]][travis-url]
[![PyUp][pyup-shield]][pyup-url]
[![MIT License][license-shield]][license-url]
[![Code Style][code-style-shield]][code-style-url]
[![LinkedIn][linkedin-shield]][linkedin-url]


<br />
<p align="center">
  <a href="https://github.com/sandervandorsten/azure-iothub-demo">
    <img src="docs/assets/imgs/FastAPI-logo-teal.png" alt="Logo" height="80">
  </a>

  <h3 align="center">FastAPI Demo</h3>

  <p align="center">
    REST API built with FastAPI on top of mock-up JSON dataset
    <br />
    <br />
    <a href="https://github.com/sandervandorsten/azure-iothub-demo/issues">Report Bug</a>
    ·
    <a href="https://github.com/sandervandorsten/azure-iothub-demo/issues">Request Feature</a>
  </p>
</p>


## Features
- allows some basic requests to a mock database (JSON)
- verifies input and output using FastAPI.


## Installation

```bash
# Create a virtual Environment
virtualenv -p $(which python3.7) venv
source venv/bin/activate
```

```bash
# Install packages
$ make install
...
Finished processing dependencies for chinook-fastapi
```

```bash
# Serve the API
$ make serve-api
cd chinook_fastapi && uvicorn api:app --reload
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [...] using statreload
INFO:     Started server process [...]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

## Usage
Using a browser (or you favorite API client, I use [Insomnia](https://insomnia.rest/)), go to `localhost:8000/docs` to see the available API methods.

e.g:
```bash
curl --request GET \
  --url http://localhost:8000/users/4 \
  --header 'content-type: application/json'
```
would return
```json
{
  "first_name": "Willard",
  "last_name": "Valek",
  "email": "wvalek3@vk.com",
  "gender": "Male",
  "ip_address": "67.76.188.26"
}
```


## TODO
- deploy API somewhere
- deploy docs

## Contact
Sander van Dorsten <sandervandorsten@gmail.com>

<hr>

<small>

This package was created with [Cookiecutter](https://github.com/audreyr/cookiecutter)
 and the [audrey/cookiecutter-pypackage](https://github.com/audreyr/cookiecutter-pypackage)
 project template.

</small>


[travis-shield]: https://img.shields.io/travis/sandervandorsten/chinook_fastapi.svg
[travis-url]: https://travis-ci.com/sandervandorsten/chinook_fastapi
[pyup-shield]: https://pyup.io/repos/github/sandervandorsten/chinook_fastapi/shield.svg
[pyup-url]: https://pyup.io/repos/github/sandervandorsten/chinook_fastapi/
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/sandervandorsten
[code-style-shield]: https://img.shields.io/badge/code%20style-black-000000.svg
[code-style-url]: https://github.com/psf/black
[license-shield]: https://img.shields.io/github/license/sandervandorsten/azure-iothub-demo.svg?
[license-url]: https://github.com/sandervandorsten/azure-iothub-demo/blob/master/LICENSE