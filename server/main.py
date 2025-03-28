from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os
import importlib
import traceback
from logging_config import get_logger, close_loggers
from utils import get_line_number

base_path = os.path.dirname(__file__)

for filename in ['.env', '.env.local']:
    env_file = os.path.join(base_path, filename)
    if os.path.exists(env_file):
        load_dotenv(env_file, override=(filename == '.env.local'))

PORT = int(os.getenv("PORT", 15000)) or 15000
DEBUG = os.getenv("DEBUG", "false").lower() == "true"

app = Flask(__name__)
logger = get_logger()

@app.teardown_appcontext
def shutdown_session(exception=None):
    logger.debug(f"[{get_line_number()}] - Flushing the logger before shutting down the application...")
    close_loggers(logger)

@app.route("/", defaults={"path": ""}, methods=["GET", "POST"])
@app.route("/<path:path>", methods=["GET", "POST"])
def handle_all(path):
    try:
        func_name = path.strip("/").split("/")[-1]
        match func_name:
            case "calculate_date_time":
                from date_utils import calculate_date_time
                data = request.get_json() if request.is_json else request.args.to_dict()
                result = calculate_date_time(data)
                return jsonify({"status": "success", "message": "Calculation completed.", "result": result}), 200

            case "fetch_web_page_content":
                from webpage_utils import fetch_web_page_content
                data = request.get_json() if request.is_json else request.args.to_dict()
                result = fetch_web_page_content(data)
                return jsonify({"status": "success", "message": "Page content fetched.", "result": result}), 200

            case _:
                return jsonify({"status": "error", "message": "Function not found"}), 404

        return jsonify({"status": "success", "result": result})

    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e),
            "trace": traceback.format_exc()
        }), 500


if __name__ == "__main__":
    try:
        logger.info(f"[{get_line_number()}] - Starting server on port {PORT} (debug={DEBUG})")
        app.run(port=PORT, debug=DEBUG)
    except OSError as e:
        logger.error(f"[{get_line_number()}] - Failed to start server: {e}")

