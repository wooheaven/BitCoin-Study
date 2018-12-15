FROM nvidia/cuda:9.0-base
 
ENV GIT_REPOSITORY https://github.com/fireice-uk/xmr-stak.git
ENV XMR_STAK_VERSION 2.7.0
ENV XMRSTAK_CMAKE_FLAGS -DXMR-STAK_COMPILE=generic -DCUDA_ENABLE=ON -DOpenCL_ENABLE=OFF

# Install packages and Compile XMR_STAK
RUN apt-get update \
    && set -x \
    && apt-get install -qq --no-install-recommends -y build-essential ca-certificates cmake cuda-core-9-0 git cuda-cudart-dev-9-0 libhwloc-dev libmicrohttpd-dev libssl-dev \
    && git clone $GIT_REPOSITORY \
    && cd /xmr-stak \
    && git checkout tags/${XMR_STAK_VERSION} -b build \
    && sed -i 's/constexpr double fDevDonationLevel = 2.0 /constexpr double fDevDonationLevel = 0.0 /' xmrstak/donate-level.hpp \
    && cat -n xmrstak/donate-level.hpp \
    && cmake ${XMRSTAK_CMAKE_FLAGS} . \
    && make \
    && cd - \
    && mv /xmr-stak/bin/* /usr/local/bin/ \
    && rm -rf /xmr-stak \
    && apt-get purge -y -qq build-essential cmake cuda-core-9-0 git cuda-cudart-dev-9-0 libhwloc-dev libmicrohttpd-dev libssl-dev \
    && apt-get clean -qq

# TimeZone
RUN apt-get install -y tzdata
 
VOLUME /mnt

WORKDIR /mnt

ENTRYPOINT ["/bin/bash"]
#ENTRYPOINT ["/usr/local/bin/xmr-stak"]
