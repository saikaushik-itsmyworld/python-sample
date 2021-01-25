FROM python:3
ADD python-sample.py /
RUN pip install flask
RUN pip install flask_restful
EXPOSE 3333
CMD [ "python", "./python-sample.py"]