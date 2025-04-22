from flask import Flask, render_template
import json
import urllib.parse

app = Flask(__name__)

def load_brands():
    with open("brand_list.json", "r") as f:
        return json.load(f)

@app.route("/")
def home():
    brands = load_brands()
    for brand in brands:
        brand["screenshot_url"] = (
            "https://api.apiflash.com/v1/urltoimage?"
            + urllib.parse.urlencode({
                "access_key": "2502b57d86e94ccf8f8879946f030ba2",  # <- replace with your API key
                "url": brand["url"],
                "full_page": "false",
                "fresh": "true"
            })
        )
    return render_template("index.html", brands=brands)

if __name__ == "__main__":
    app.run(debug=True)
