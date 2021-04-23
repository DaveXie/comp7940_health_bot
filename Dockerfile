FROM python
COPY healthbot.py /healthbot.py
COPY requirements.txt /requirements.txt
RUN pip install pip update
RUN pip install -r requirements.txt
CMD python healthbot.py



