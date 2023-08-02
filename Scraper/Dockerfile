FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD ["python3", "Scraper.py"]


# Run
# docker run --network tap --rm -it --name scraper scraper:1.0