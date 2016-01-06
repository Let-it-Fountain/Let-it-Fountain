FROM ubuntu:15.10
MAINTAINER Andrew Kuchev (kuchevad@gmail.com)

RUN apt-get update \
 && apt-get install -y git build-essential cmake \
    libx11-dev libxi-dev \
    libsndfile1-dev \
    libpng12-dev libjpeg-dev libfftw3-dev \
    libopenexr-dev libopenjpeg-dev \
    libopenal-dev libalut-dev libvorbis-dev \
    libglu1-mesa-dev libsdl1.2-dev libfreetype6-dev \
    libtiff5-dev libavdevice-dev \
    libavformat-dev libavutil-dev libavcodec-dev libjack-dev \
    libswscale-dev libx264-dev libmp3lame-dev python3.5-dev \
    libspnav-dev libtheora-dev libglew-dev \
    libboost-all-dev libopenimageio-dev python-requests python3 python3-pip \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

RUN mkdir ~/blender-git \
 && cd ~/blender-git \
 && git clone http://git.blender.org/blender.git \
 && cd blender \
 && git submodule update --init --recursive \
 && git submodule foreach git checkout master \
 && git submodule foreach git pull --rebase origin master

RUN cd ~/blender-git/blender \
 && mkdir build \
 && cd build \
 && cmake ../ -DWITH_PYTHON_INSTALL=OFF -DWITH_PLAYER=OFF -DWITH_PYTHON_MODULE=ON \
 && make \
 && make install

RUN adduser python-test --disabled-password --quiet

RUN mkdir -p /home/python-test/blender \
 && cp ~/blender-git/blender/build/bin /home/python-test/blender -r \
 && chown -R python-test:python-test /home/python-test/blender

USER python-test

WORKDIR /home/python-test

RUN mkdir ~/src

VOLUME ~/src

ENTRYPOINT ["bash"]

