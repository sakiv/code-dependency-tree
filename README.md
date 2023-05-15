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

- Clone git repository
    ```
    git clone https://github.com/sakiv/dep-graph-generator.git
    ```

- Start docker container
    ```
    docker compose up
    ```

## VS Code Instructions

- Install the `Python` extension
- Install the `Remote - Containers` extension
- Open the `Command Palette` and type `Dev Containers`, then select the `Dev Containers: Attach to Running Container...` and select the running docker container
- VS Code will restart and reload
- On the `Explorer` sidebar, click the open a folder button and then enter `/workspace` (this will be loaded from the remote container)
- On the `Extensions` sidebar, select the `Python` extension and install it on the container
- When prompted on which interpreter to use, select `/usr/local/bin/python`
- Open the `Command Palette` and type `Python: Configure Tests`, then select the `pytest framework`



