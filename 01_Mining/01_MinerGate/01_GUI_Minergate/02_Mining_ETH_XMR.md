```{bash}
# 4Core / 5120MB Ram / 100GB HDD
cat /etc/issue
Ubuntu 16.04.3 LTS \n \l
```

```{bash}
sudo dpkg -i minergate-7.2.deb
minergate &
```

```{bash}
top -p `pgrep "minergate"`
ls -lh ~/.ethash-minergate/
tail -f ~/.local/share/minergate/log/eth.log
tail -f ~/.local/share/minergate/log/minergate.log
```
