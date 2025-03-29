# LLM Tools


This is an example server that can be used with LocalAI browser extension to extend the Large Language Model (LLM) with user-defined functionality. It is safe to use locally if you dont want to create your own.

> [!Note]
> Python is required to run this server.

# Installation

1. Open a terminal in any location where you want to use it.
2. Execute the following command to clone the repository:
```
git clone https://github.com/ivostoykov/llmTools.git
```

This will create an `llmTools` directory where your terminal is opened.

3. Move into the `llmTools` directory:

```
cd ./llmTools
```

4. Create a new virtual environment and install the required libraries:

```
python3 -m venv venv
source venv/bin/activate
pip install -U pip
pip install -U -r requirements.txt
```

All libraries are standard, so there should be no issues here. If you encounter any problems, please report them on the [Issues](https://github.com/ivostoykov/llmTools/issues) page.

## Server and Tools

The server and tools are located in the `llmTools/server` directory. The main entry point is `main.py`. There are two additional helpers: `utils.py` and `logging_config.py`.

* `.env` file contains variables needed for the server to run.
* When running the server, log records are stored in the `storeapi.log` file. This file should be checked first if something goes wrong. It needs to be cleaned manually periodically.

## Tools

Each tool is located in its own separate file. To add a new tool, it must be registered in `main.py` by adding a new case block to the `handle_all(path)` function.

* `calculate_date_time`: A function that calculates date and time given an offset.
* `fetch_web_page_content`: Attempts to fetch the content of a given URL if possible. Note that some sites may block requests suspected as non-human and may ban your IP.


