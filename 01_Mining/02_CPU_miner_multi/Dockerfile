FROM       ubuntu:14.04

RUN        echo "deb http://ftp.daumkakao.com/ubuntu/ xenial main restricted" > /etc/apt/source.list
RUN        echo "deb http://ftp.daumkakao.com/ubuntu/ xenial-updates main restricted" >> /etc/apt/source.list
RUN        echo "deb http://ftp.daumkakao.com/ubuntu/ xenial universe" >> /etc/apt/source.list
RUN        echo "deb http://ftp.daumkakao.com/ubuntu/ xenial-updates universe" >> /etc/apt/source.list
RUN        echo "deb http://ftp.daumkakao.com/ubuntu/ xenial multiverse" >> /etc/apt/source.list
RUN        echo "deb http://ftp.daumkakao.com/ubuntu/ xenial-updates multiverse" >> /etc/apt/source.list
RUN        echo "deb http://ftp.daumkakao.com/ubuntu/ xenial-backports main restricted universe multiverse" >> /etc/apt/source.list
RUN        echo "deb http://ftp.daumkakao.com/ubuntu xenial-security main restricted" >> /etc/apt/source.list
RUN        echo "deb http://ftp.daumkakao.com/ubuntu xenial-security universe" >> /etc/apt/source.list
RUN        echo "deb http://ftp.daumkakao.com/ubuntu xenial-security multiverse" >> /etc/apt/source.list
RUN        echo "deb [arch=amd64] https://download.docker.com/linux/ubuntu xenial stable" >> /etc/apt/source.list

RUN        apt-get update -qq
RUN        apt-get install -qy automake autoconf pkg-config libcurl4-openssl-dev libssl-dev libjansson-dev libgmp-dev make g++ git vim

RUN        git clone https://github.com/tpruvot/cpuminer-multi -b linux
RUN        cd cpuminer-multi && ./build.sh

WORKDIR    /cpuminer-multi
ENTRYPOINT ["/bin/bash"]
