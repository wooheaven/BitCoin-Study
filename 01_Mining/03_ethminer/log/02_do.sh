#!/bin/bash
for ((num=1; num<=${1}; num++)) do
echo "num = "${num}

date > test00gpu-${num}.log
echo "" >> test00gpu-${num}.log

nvidia-smi >> test00gpu-${num}.log
echo "" >> test00gpu-${num}.log

echo "run"
nohup ./01_run.sh >> test00gpu-${num}.log 2>&1 &
sleep 2400

echo "kill -9 ethminer"
pgrep ethminer > pid-${num}.txt
kill -9 $(cat pid-${num}.txt)
sleep 1200;

echo "" >> test00gpu-${num}.log;
echo "ethminer pid" >> test00gpu-${num}.log
cat pid-${num}.txt >> test00gpu-${num}.log

done
