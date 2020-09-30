import json
import os

app_dir = os.path.dirname(os.path.abspath(__file__))


if __name__ == "__main__":
    with open(f"{app_dir}/geojson/uk.ac.cam.kings.geojson") as f:
        status = json.load(f)

    print(status)
