from bs4 import BeautifulSoup
import requests

def main(URL):
    with open("out.csv", "a") as File:
        HEADERS = ({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'})

        webpage = requests.get(URL, headers=HEADERS)
        soup = BeautifulSoup(webpage.content, "html.parser")

        try:
            title = soup.find("span", attrs={"id": 'productTitle'})
            title_value = title.get_text(strip=True)
        except AttributeError:
            title_value = "NA"
        print("product Title = ", title_value)
        File.write(f"{title_value},")

        try:
            price = soup.find("span", attrs={'id': 'priceblock_ourprice'}).get_text(strip=True)
        except AttributeError:
            price = "NA"
        print("Products price = ", price)
        File.write(f"{price},")

        try:
            rating = soup.find("i", attrs={'class': 'a-icon a-icon-star a-star-4-5'}).get_text(strip=True)
        except AttributeError:
            try:
                rating = soup.find("span", attrs={'class': 'a-icon-alt'}).get_text(strip=True)
            except:
                rating = "NA"
        print("Overall rating = ", rating)
        File.write(f"{rating},")

        try:
            review_count = soup.find("span", attrs={'id': 'acrCustomerReviewText'}).get_text(strip=True)
        except AttributeError:
            review_count = "NA"
        print("Total reviews = ", review_count)
        File.write(f"{review_count},")

        try:
            available = soup.find("div", attrs={'id': 'availability'}).find("span").get_text(strip=True)
        except AttributeError:
            available = "NA"
        print("Availability = ", available)
        File.write(f"{available}\n")

if __name__ == '__main__':
    with open("url.txt", "r") as file:
        for links in file.readlines():
            main(links.strip())