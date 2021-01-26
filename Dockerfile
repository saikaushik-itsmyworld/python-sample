FROM python:3
ADD python-sample.py /
RUN pip install -r requirements.txt --user
EXPOSE 3333
CMD [ "python", "./python-sample.py"]