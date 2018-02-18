FROM arm32v7/python:3.7-rc-stretch
EXPOSE 8000

# Setup sudo
RUN apt-get update && \
      apt-get -y install sudo
RUN adduser --disabled-password --gecos '' docker
RUN adduser docker sudo
RUN echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers

USER docker
RUN sudo mkdir -p /usr/src/code/test
COPY test_servo.py /usr/src/code/test 
COPY servosix /usr/src/code/servosix

WORKDIR "/usr/src/code/servosix/python"
RUN sudo python setup.py install
WORKDIR "/usr/src/code/test"
CMD ["python","./test_servo.py"]
