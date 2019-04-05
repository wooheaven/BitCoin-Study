# timeZone
```{bash}
root@057788a367e7:/mnt# dpkg-reconfigure tzdata
debconf: unable to initialize frontend: Dialog
debconf: (No usable dialog-like program is installed, so the dialog based frontend cannot be used. at /usr/share/perl5/Debconf/FrontEnd/Dialog.pm line 76.)
debconf: falling back to frontend: Readline
Configuring tzdata
------------------

Please select the geographic area in which you live. Subsequent configuration questions will narrow this down by presenting a list of cities, representing the time zones in which they are located.

  1. Africa  2. America  3. Antarctica  4. Australia  5. Arctic  6. Asia  7. Atlantic  8. Europe  9. Indian  10. Pacific  11. SystemV  12. US  13. Etc
Geographic area: 6

Please select the city or region corresponding to your time zone.

  1. Aden      9. Baghdad   17. Chita       25. Dushanbe     33. Irkutsk    41. Kashgar       49. Macau         57. Omsk        65. Riyadh         73. Tashkent       81. Ulaanbaatar    89. Yerevan
  2. Almaty    10. Bahrain  18. Choibalsan  26. Famagusta    34. Istanbul   42. Kathmandu     50. Magadan       58. Oral        66. Sakhalin       74. Tbilisi        82. Urumqi
  3. Amman     11. Baku     19. Chongqing   27. Gaza         35. Jakarta    43. Khandyga      51. Makassar      59. Phnom_Penh  67. Samarkand      75. Tehran         83. Ust-Nera
  4. Anadyr    12. Bangkok  20. Colombo     28. Harbin       36. Jayapura   44. Kolkata       52. Manila        60. Pontianak   68. Seoul          76. Tel_Aviv       84. Vientiane
  5. Aqtau     13. Barnaul  21. Damascus    29. Hebron       37. Jerusalem  45. Krasnoyarsk   53. Muscat        61. Pyongyang   69. Shanghai       77. Thimphu        85. Vladivostok
  6. Aqtobe    14. Beirut   22. Dhaka       30. Ho_Chi_Minh  38. Kabul      46. Kuala_Lumpur  54. Nicosia       62. Qatar       70. Singapore      78. Tokyo          86. Yakutsk
  7. Ashgabat  15. Bishkek  23. Dili        31. Hong_Kong    39. Kamchatka  47. Kuching       55. Novokuznetsk  63. Qyzylorda   71. Srednekolymsk  79. Tomsk          87. Yangon
  8. Atyrau    16. Brunei   24. Dubai       32. Hovd         40. Karachi    48. Kuwait        56. Novosibirsk   64. Rangoon     72. Taipei         80. Ujung_Pandang  88. Yekaterinburg
Time zone: 68


Current default time zone: 'Asia/Seoul'
Local time is now:      Thu Oct 25 16:56:14 KST 2018.
Universal Time is now:  Thu Oct 25 07:56:14 UTC 2018.

root@057788a367e7:/mnt# date
Thu Oct 25 16:56:16 KST 2018
```

# xmr-stak initialize
```{bash}
root@057788a367e7:/mnt# /usr/local/bin/xmr-stak
Please enter:
- Do you want to use the HTTP interface?
Unlike the screen display, browser interface is not affected by the GPU lag.
If you don't want to use it, please enter 0, otherwise enter port number that the miner should listen on
80
Configuration stored in file 'config.txt'
Please enter:
- Please enter the currency that you want to mine: 
	- aeon7
	- bbscoin
	- bittube
	- cryptonight
	- cryptonight_bittube2
	- cryptonight_masari
	- cryptonight_haven
	- cryptonight_heavy
	- cryptonight_lite
	- cryptonight_lite_v7
	- cryptonight_lite_v7_xor
	- cryptonight_v7
	- cryptonight_v8
	- cryptonight_v7_stellite
	- graft
	- haven
	- intense
	- masari
	- monero
	- qrl
	- ryo
	- stellite
	- turtlecoin

monero
- Pool address: e.g. pool.example.com:3333
asia.cryptonight-hub.miningpoolhub.com:20580
- Username (wallet address or pool login):
nomad2on2digital.t04c
- Password (mostly empty or x):
x
- Rig identifier for pool-side statistics (needs pool support). Can be empty:

- Does this pool port support TLS/SSL? Use no if unknown. (y/N)
N
- Do you want to use nicehash on this pool? (y/n)
n
- Do you want to use multiple pools? (y/n)
n

^C (<- Ctl + c)
root@057788a367e7:/mnt# vi config.txt
...
"output_file" : "/mnt/xmr-stak.log",
"http_login" : "t04c",
"http_pass" : "12qwaszx",

# run as backgroup with print to null
root@057788a367e7:/mnt# cat 01_run_xmr-stak.sh
/usr/local/bin/xmr-stak > /dev/null 2>&1 &

root@057788a367e7:/mnt# ./01_run_xmr-stak.sh
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

# docker run with : processors 0 1 2
```{bash}
root@057788a367e7:/mnt# vi cpu.txt
...
"cpu_threads_conf" :
[
    { "low_power_mode" : false, "no_prefetch" : true, "asm" : "auto", "affine_to_cpu" : 0 },
    { "low_power_mode" : false, "no_prefetch" : true, "asm" : "auto", "affine_to_cpu" : 1 },
    { "low_power_mode" : false, "no_prefetch" : true, "asm" : "auto", "affine_to_cpu" : 2 },
    { "low_power_mode" : false, "no_prefetch" : true, "asm" : "auto", "affine_to_cpu" : 3 },
],
```
