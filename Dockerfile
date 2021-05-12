FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7
WORKDIR /app/
COPY Regressoion.pkl .
COPY requirements.txt .
COPY AgrcultureDataset.csv .
RUN pip install -r ./requirements.txt
COPY main.py /app/
CMD ["python", "main.py"]