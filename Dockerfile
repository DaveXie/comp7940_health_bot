FROM python
COPY healthbot.py /healthbot.py
COPY requirements.txt /requirements.txt
RUN pip install pip update
RUN pip install -r requirements.txt

ENV ACCESS_TOKEN=1742240853:AAEv96o5sCN1bY2YLmwJ7sz7Tx0n0w93DvM
ENV HOST=redis-18976.c124.us-central1-1.gce.cloud.redislabs.com
ENV PASSWORD=rhOK7SQtW4baUgkqlOQ4VJ4Eh8j9C1pc
ENV REDISPORT=18976
ENV APIKEY=10240eda73mshec0bc03cd897568p16cae8jsnd9d2285d965e

CMD python healthbot.py