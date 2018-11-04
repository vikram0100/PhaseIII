FROM ubuntu
MAINTAINER s310280@oslomet.no

WORKDIR /tmp
COPY . /tmp

RUN apt-get update  && apt-get -y install python-pip python-dev build-essential

#RUN pip install --upgrade --no-cache-dir https://get.graphlab.com/GraphLab-Create/2.1/s310280@oslomet.no/2528-42A8-1569-C669-D453-0B53-78E4-8625/GraphLab-Create-License.tar.gz
RUN pip install "ipython[notebook]" jupyter
###USER ROOT

EXPOSE 8888

CMD ["jupyter","notebook","--allow-root" ,"--port=8888", "--no-browser","--ip=0.0.0.0"]
