# xmr-stak-cpu
```{text}
docker + alpine:3.6
```

# cpu : processor, core-id
```{bash}
$ egrep 'processor|core id' /proc/cpuinfo > cpu.txt
$ cat cpu.txt
processor	: 0
core id		: 0
processor	: 1
core id		: 1
processor	: 2
core id		: 2
processor	: 3
core id		: 3
processor	: 4
core id		: 0
processor	: 5
core id		: 1
processor	: 6
core id		: 2
processor	: 7
core id		: 3

$ awk '{if(NF ==3) {printf "%s%s", $1,$3} else{printf ",%s%s\n", $1,$4}} ' cpu.txt > tmp.txt
$ mv tmp.txt cpu.txt
$ sed -i 's/processor/p/g' cpu.txt
$ sed -i 's/core/c/g' cpu.txt
$ awk 'BEGIN{FS=OFS=","} {if(arr[$2]) {arr[$2]=arr[$2]"|"$1} else{arr[$2]=$1}} END{for(i in arr) {print i,arr[i]}}' cpu.txt > tmp.txt
$ mv tmp.txt cpu.txt
$ sort -t, -k1.2n,1 cpu.txt > tmp.txt
$ mv tmp.txt cpu.txt
$ cat -n cpu.txt
1 c0,p0|p4
2 c1,p1|p5
3 c2,p2|p6
4 c3,p3|p7
```

# find THREAD_CONFIG
```{text}
0 2 4 6 = 91 H/s
0 1 2 3 = 99 H/s <- by core id
```

# docker pull and tag
```{bash}
# ref Dockerfile = https://github.com/neffets/docker-xmr-stak-cpu
# ref xmr-stak   = https://github.com/fireice-uk/xmr-stak

$ docker pull neffects/xmr-stak-cpu
$ docker tag neffects/xmr-stak-cpu:latest test/test:latest
$ docker rmi neffects/xmr-stak-cpu:latest
$ docker images
```

# docker build 
```{bash}
$ git clone git@github.com:neffets/docker-xmr-stak-cpu.git
$ vi Dockerfile
...
RUN git clone https://github.com/fireice-uk/xmr-stak.git \
    && cd xmr-stak \
    && git checkout tags/${XMR_STAK_VERSION} -b build  \
    && sed -i 's/constexpr double fDevDonationLevel.*/constexpr double fDevDonationLevel = 0.0;/' xmrstak/donate-level.hpp \
    && cat -n xmrstak/donate-level.hpp \
    \
    && cmake . -DCUDA_ENABLE=OFF -DOpenCL_ENABLE=OFF -DHWLOC_ENABLE=ON -DXMR-STAK_COMPILE=generic \
    && make -j$(nproc) \
    \
    && cp -t /app bin/xmr-stak \
    && chmod 777 -R /app
...

$ docker build --tag test/test:latest --force-rm --file Dockerfile .
$ docker images
```

# docker run with : processors 0 1 2 3 in cpu.txt
```{bash}
$ docker run -itd --restart unless-stopped \
-e WALLET_ADDRESS='ID' \
-e POOL_PASSWORD='PASSWORD' \
-e POOL_ADDRESS='asia.cryptonight-hub.miningpoolhub.com:20580' \
-e THREAD_CONFIG='{"low_power_mode" : false, "no_prefetch" : true, "affine_to_cpu" : 0 },{"low_power_mode" : false, "no_prefetch" : true, "affine_to_cpu" : 1 },{"low_power_mode" : false, "no_prefetch" : true, "affine_to_cpu" : 2 },{"low_power_mode" : false, "no_prefetch" : true, "affine_to_cpu" : 3 },' \
-e HTTPD_PORT=80 \
-p 180:80 \
--name test test/test:latest

$ docker stop xmr-stak-cpu
$ docker rm xmr-stak-cpu
```

# docker logs
```{bash}
docker logs --tail -f 1000 test
```

# monitoring
```{text}
IP:Port
192.11.22.33:180
```
