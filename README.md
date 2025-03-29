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

Each tool is located in its own separate file. To add a new tool, it must be registered in `main.py` by adding a new case block to the `handle_all(path)` function. The functions here are examples. You can modify them or use them as they are.

* `calculate_date_time`: A function that calculates date and time given an offset.
* `fetch_web_page_content`: Attempts to fetch the content of a given URL if possible. Note that some sites may block requests suspected as non-human and may ban your IP.
* `web_search`: Allow the LLM to search beyond the page loaded in current tab. see [Web Search](#web-search)

# Using the server

To start the server, run:
```
$ python ./server/main.py
```

You should see output in the console similar to this:

```
 * Serving Flask app 'main'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:15000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 288-852-566
```

> [!NOTE]
> The warning about the development server is standard for Flask. It's safe to ignore while running on localhost, but switch to a production WSGI server for deployment.

# Web Search
There are three ways to implement web search:

1. **Scrape Search Engines**: Be aware of potential legal issues.
2. **Use an API**: Utilise free or paid APIs like the Google Custom Search API with the appropriate key.
3. **Use SearxNG**: A free, self-hosted meta-search engine. More details at [searxng](https://github.com/searxng/searxng).

The provided `web_search` function utilises [SearxNG](https://github.com/searxng/searxng). Below is how you can set it up.
The necessary variables are in the `.env` file.

## Using Podman
```
podman run -d --name searxng \
	--network=pasta:-t,7999:8080,-u,auto,-T,auto,-U,auto \
	-v ~/searxng:/etc/searxng \
	-v ~/logs:/var/log/uwsgi \
	--restart unless-stopped \
	docker.io/searxng/searxng:latest
```

This will add a container that is accessible on http://localhost:7999

- **Start it**: `pondman start searxng`
- **Stop it**: `pondman stop searxng`
- **Delete it**: `podman rm searxng`

To update it:
1. Stop it
2. Remove it
3. Run it again with `podman run` command above.

## Using Docker
```
docker run -d --name searxng \
    -p 7999:8080 \
    -v ~/searxng:/etc/searxng \
    -v ~/logs:/var/log/uwsgi \
    --restart unless-stopped \
    searxng/searxng:latest
```

- **Start it**: `docker start searxng`
- **Stop it**: `docker stop searxng`
- **Delete it**: `docker rm searxng`
