# PRODIGY_SD_05
# Product Information Scraper

This Python script extracts product information, such as names, prices, and ratings, from an online e-commerce website and stores the data in a structured format like a CSV file.

## Requirements

- Python 3.x
- `requests` library
- `beautifulsoup4` library

## Installation

1. Clone this repository or download the script files.

2. Install the required Python libraries using pip:
    ```bash
    pip install requests beautifulsoup4
    ```

## Usage

1. Create a `url.txt` file in the same directory as the script. Add the URLs of the product pages you want to scrape, each on a new line.

2. Run the script:
    ```bash
    python web_scrapper.py
    ```

3. The script will create (or append to) an `out.csv` file in the same directory, containing the extracted product information.

## Output

The `out.csv` file will contain the following columns:
- Product Title
- Product Price
- Product Rating
- Total Reviews
- Availability
