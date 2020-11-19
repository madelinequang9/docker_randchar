FROM python:3.7
WORKDIR /serverdata
ENV FLASK_APP=text_gen.py
ENV FLASK_RUN_HOST=0.0.0.0
COPY requirements.txt .
RUN pip install -r requirements.txt
EXPOSE 5000
COPY . /serverdata 
CMD ["python","./app/text_gen.py"]
 


