#!/usr/bin/env python3
# https://github.com/StannisGr/yaschedule

import os
import argparse
from dotenv import load_dotenv
from yaschedule.core import YaSchedule

if __name__ == "__main__":
    load_dotenv()

    parser = argparse.ArgumentParser(description='Script download stations list from Yandex Schedule API')
    parser.add_argument('--json',
        action='store_true',
        help='Save also json')
    args = parser.parse_args()
    
    TOKEN = os.getenv('YASCHEDULE_YANDEX_TOKEN')
    print("YASCHEDULE_YANDEX_TOKEN:", TOKEN)
    yaschedule = YaSchedule(TOKEN)
    stations_list = yaschedule.get_all_stations()
    print("Stations list loaded and saved in cache")

    if args.json:
        import json
        with open("stations_list.json", "w") as f:
            json.dump(stations_list, f)
            print("Stations list saved as json file")
