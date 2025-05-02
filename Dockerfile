FROM python 3.12

WORKDIR /flaskapi3an

COPY requirement.txt .

RUN pip install --no-cache-dir -r requirement.txt

COPY . . 

EXPOSE 5000

CMD ["python", "api/app.py"]