# fast_api.py

from fastapi import FastAPI, Form, HTTPException
from main import SourceScraper

app = FastAPI()

@app.post("/scrape")
async def scrape_url(emulate_browser: bool = True, url: str = Form(...)):
    if emulate_browser:
        try:
            scraper = SourceScraper(emulate_browser=True)
            html_content = scraper.scrape_page(url)
            return {"status": "success", "message": html_content}
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
    else:
        return {"status": "success", "message": "POST request received"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)



#  command = uvicorn fast_api:app --reload