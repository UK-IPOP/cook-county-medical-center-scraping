from arcgis.geocoding import geocode
from arcgis.gis import GIS
import os
import json
from rich.progress import track
from dotenv import load_dotenv


def initialize():
    load_dotenv()
    GIS(
        api_key=os.getenv("ARCGIS_API_KEY"),
    )


def load_data() -> list[dict[str, str]]:
    with open("./medicalfacilities/data/cookcounty-centers.json", "r") as f:
        centers = json.load(f)

    with open("./medicalfacilities/data/university-centers.json", "r") as f:
        university_centers = json.load(f)

    return centers + university_centers


def main():
    initialize()
    centers = load_data()
    for center in track(centers, description="Geocoding"):
        result = geocode(center["address"])
        if result:
            geo = result[0]  # best result
            center["geocoded_latitude"] = geo["location"]["x"]
            center["geocoded_longitude"] = geo["location"]["y"]
            center["geocoded_address"] = geo["address"]
            center["geocoded_score"] = geo["score"]

    with open("./medicalfacilities/data/centers.json", "w") as f:
        json.dump(centers, f, indent=4)


if __name__ == "__main__":
    main()
