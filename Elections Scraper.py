import sys
import os
import csv
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# URL of Český statistický úřad, Parliament of ČR elections 2017
BASE_URL = "https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ"


# standard error print
def print_error(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

# get district link, parse html code,
def get_district_link(district):
    html = requests.get(BASE_URL)

    parser = BeautifulSoup(html.text, "html.parser")

    # css selectors
    for row in parser.select("#publikace table.table tr"):
        columns = row.select("td")
        # skip header
        if len(columns) != 4:
            continue
        name = columns[1].text
        if name.lower() == district.lower():
            # abs url creation from relative
            abs_url = urljoin(BASE_URL, columns[3].a['href'])
            return abs_url

    return None


def parse_district(district_url):
    html = requests.get(district_url)
    parser = BeautifulSoup(html.text, "html.parser")
    for row in parser.select("#publikace table.table tr"):
        columns = row.select("td")
        if len(columns) != 3:
            continue
        # skip blank rows
        if not columns[0].a:
            continue

        city_code = columns[0].text
        city_name = columns[1].text
        abs_url = urljoin(BASE_URL, columns[0].a['href'])
        print(f"Found city link for {city_name} #{city_code}: {abs_url}")
        parse_city(city_name, city_code, abs_url)


def parse_city(city_name, city_code, city_url):
    html = requests.get(city_url)
    parser = BeautifulSoup(html.text, "html.parser")

    summary_row = parser.select("#publikace table#ps311_t1 tr")[-1].select("td")

    # delete all spaces, convert to number
    total_voters = int("".join(summary_row[3].text.split()))
    issued_votes = int("".join(summary_row[4].text.split()))
    valid_votes = int("".join(summary_row[7].text.split()))

    parties = []
    for parties_row in parser.select("#publikace div.t2_470 table tr"):
        columns = parties_row.select("td")
        if len(columns) != 5 or not columns[-1].a:
            continue
        parties.append(columns[1].text)

    line = [city_code, city_name, total_voters, issued_votes, valid_votes, "|".join(parties)]
    print(f"RESULT: {line}")
    csv_writer.writerow(line)


if __name__ == '__main__':
    # Arguments check
    try:
        requested_district = sys.argv[1]
        requested_file_name = sys.argv[2]
    except IndexError:
        print_error("Invalid number of arguments.")
        print_error("Usage: DISTRICT_NAME OUTPUT_FILE")
        print_error(f"Sample: {os.path.basename(sys.argv[0])} Beroun /tmp/beroun-2017.csv")
        exit(-1)

    print(f"Hello. Scrapping elections results for {requested_district}")

    district_link = get_district_link(requested_district)
    if not district_link:
        print_error(f"District not found for name: {requested_district}")
        exit(-1)

    print(f"Found district link for {requested_district}: {district_link}")
    with open(requested_file_name, mode='w') as file:
        csv_writer = csv.writer(file, delimiter=';', quotechar='"')

        # header write out
        csv_writer.writerow(["CITY_CODE", "CITY_NAME", "TOTAL_VOTERS", "ISSUED_VOTES", "VALID_VOTES", "PARTIES"])
        parse_district(district_link)
