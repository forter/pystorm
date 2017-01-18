FROM 174522763890.dkr.ecr.us-east-1.amazonaws.com/alpine-python2-onbuild
USER root
RUN pip install -r test-requirements.txt
USER app