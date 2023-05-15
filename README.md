# Dependency Graph Generator
An utility to generate dependency graph for your code.

## Usage
---

- Interactive mode
    ```
    > python3 app.py
    ```

- Pass agruments
    ```
    > python3 app.py <directory-path> <format> <enable-debugging>
    ```

    - **directory path**: Path to source files. Default is current directory.
    - **format**: Possible values - ksh, js
    - **enable-debugging**: Print debug information on console.
## Want to contribute? Steps to setup development environment
---
### Prerequisites
- An IDE Tool,  
    - [Visual Studio Code](https://code.visualstudio.com/download) - preferred by @sakiv
    - [PyCharm](https://www.jetbrains.com/pycharm/download)
- A Git client ([Git Bash for Windows](https://git-scm.com/downloads))
- [Docker Engine](https://docs.docker.com/engine/install/)
    - Docker Desktop (free for personal use) 
    - Standalone Docker Engine (works well with Colima)

** *Note: If you are using VS Code then I highly recommended [VS Code Docker extension](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-docker) to manage docker images and containers*

### Usage:

- If you are starting fresh, clone git repository
    ```
    git clone https://github.com/sakiv/devcontainer-python.git
    ```

- If you already have a python code, then go to your python project directory and pull this repository
    ```
    git pull https://github.com/sakiv/devcontainer-python.git
    ```

- Add necessary environment variables in local.env
    ```
    POSTGRESS_UID=********
    POSTGRESS_PWD=********
    ```

- Add or remove any additional python libraries in requirements.txt, defaults are
    ```
    pytest
    pytest-mock
    postgres
    typer
    asyncio
    aiohttp
    requests
    ```

- Build docker image
    ```
    docker compose build
    ```

- Build docker image and spin off a new container
    ```
    docker compose up
    ```

- Create new container from existing image and workspace from host machine directory
    ```
    docker run -dit --env-file local.env --mount type=bind,source="$(pwd)",target=/workspace --name="$(basename $PWD)" devcontainer-python:latest
    ```

** *Note: I recommend using VS Code Docker extension to manage docker images and containers. But if you are using another IDE and need to use Docker CLI then refer to (Docker CLI documentation)[https://docs.docker.com/engine/reference/commandline/cli/]*

## VS Code Instructions

- Install the `Python` extension
- Install the `Remote - Containers` extension
- Open the `Command Palette` and type `Dev Containers`, then select the `Dev Containers: Attach to Running Container...` and select the running docker container
- VS Code will restart and reload
- On the `Explorer` sidebar, click the open a folder button and then enter `/workspace` (this will be loaded from the remote container)
- On the `Extensions` sidebar, select the `Python` extension and install it on the container
- When prompted on which interpreter to use, select `/usr/local/bin/python`
- Open the `Command Palette` and type `Python: Configure Tests`, then select the `pytest framework`



