# app.py

from flask import Flask, render_template, request
from proxy1 import SourceScraper  # Assuming you've saved the SourceScraper class in a file named scraper.py

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def scrape_and_display():
    if request.method == 'POST':
        user_input_urls = request.form.get('urls')
        start_urls = user_input_urls.split('\n') if user_input_urls else []

        try:
            scraper = SourceScraper(start_urls)
            scraped_data = scraper.scrape()
            return render_template('display1.html', scraped_data=scraped_data)
        except Exception as e:
            return render_template('error.html', error_message=str(e))

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)


# python app1.py