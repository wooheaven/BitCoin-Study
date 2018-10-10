| WorkerName | Processor | Currency | Program      | user@IP:Port                      | Mode | VM or Container      |
|------------|-----------|----------|--------------|-----------------------------------|------|----------------------|
| test01     | gpu       | ETH      | ethminer     | ubuntu@192.168.7.178     ubuntu   | CLI  | test1                |
| t01c       | cpu       | XMR      | xmr-stak-cpu | ubuntu@192.168.7.178:180          | CLI  | test3                |
| test02     | gpu       | ETH      | ethminer     | ubuntu@192.168.7.179              | CLI  | test1                |
| t02c       | cpu       | XMR      | xmr-stak-cpu | ubuntu@192.168.7.179:182          | CLI  | test3                |
| test03     | gpu       | ETH      | ethminer     | ubuntu@192.168.7.180              | CLI  | test1                |
| t03c       | cpu       | XMR      | xmr-stak-cpu | ubuntu@192.168.7.180:183          | CLI  | test3                |
| test04     |           |          |              | root@ 23wesdxc                    |      |                      |
|            | gpu       | XMR      | xmr-stak     | ubuntu@192.168.3.47:180  12qwaszx | CLI  | Notebook             |
|            | cpu       | XMR      | xmr-stak-cpu | ubuntu@192.168.3.47:184           | CLI  |                      |
| test05     | cpu       | XMR      | xmr-stak-cpu | bistel@192.168.3.37:180           | CLI  | eDL_HAWQ_5           |
| test06     | cpu       | XMR      | xmr-stak-cpu | bistel@192.168.3.38:180           | CLI  | spark.dso.test1      |
| test07     | cpu       | XMR      | xmr-stak-cpu | bistel@192.168.3.39:180           | CLI  | eDL_Algo_Ubuntu14.04 |

| Coin | Resource | Mode | Software                 |
|------|----------|------|--------------------------|
| ETH  | CPU      | GUI  | minergate                |
| ETH  | CPU      | CLI  |                          |
| ETH  | GPU      | CLI  | ethereum-mining/ethminer |
| XMR  | CPU      | CLI  | timonmat/xmr-stak-cpu    |
| XMR  | CPU/GPU  | CLI  | fireice-uk/xmr-stak      |
