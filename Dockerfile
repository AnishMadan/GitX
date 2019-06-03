FROM python:3

COPY ["libgitX.py", "gitX"]

ARG COMMAND

RUN pip install argparse
RUN pip install configparser

CMD [ "python3", "./gitX" ]
