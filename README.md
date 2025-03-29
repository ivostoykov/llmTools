# llmTools
This is an example server that can be used with localAI browser extension to extend the LLM with user defined functioinality. It is safe to use it locally if you don't want to bother creating your own.

> [!NOTE]
> Python is required

# Installation

1. Open a terminal wherever you want to use it, and execute the following command:
```
git clone https://github.com/ivostoykov/llmTools.git
```
This will create `llmTools` dir where your terminal is onpen into. As there are no dependencies the location generally doesn't matter, but better off to be a private place.

2. Move into the `llmTools` dir:
```
cd ./llmTools
```

3. Recreate the needed environment and install the needed libraries:
```
python3 -m venv venv
source venv/bin/activate
pip install -U pip
pip install -U -r requirements.txt
```
All libraries are standard so there are no expected problems here. If any please report on [Issues](https://github.com/ivostoykov/llmTools/issues).

The server and the tools are in the `llmTools/server` dir. `main.py` is the entry point. There are two additional helpers facilitating the track of any problems that occur. Those are `utils.py` and `logging_config.py`.

`.env` is where the variables needed are located.
While running the server various log records are stored into `storeapi.log` file. This is the first place to look at when something goes wrong.  It need manually clean periodically.

There it comes the tools - each one is in own separate file. Whenever a new one is added it must be registered into `main.py` in `def handle_all(path):` as a separate `case` block.

# What is in there
* `calculate_date_time` - A function calculating date and time by given an offset.
* `fetch_web_page_content` - Try to fetch a given url if possible. Please note that there are sites that block requests suspected as non human ones and may ban your IP.
