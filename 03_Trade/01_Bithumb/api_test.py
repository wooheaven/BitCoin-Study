#! /usr/bin/env python
# XCoin API-call sample script (for Python 3.X)
#
# @author	btckorea
# @date	2017-04-11
#
#
# First, Build and install pycurl with the following commands::
# (if necessary, become root)
#
# https://pypi.python.org/pypi/pycurl/7.43.0#downloads
#
# tar xvfz pycurl-7.43.0.tar.gz
# cd pycurl-7.43.0
# python setup.py --libcurl-dll=libcurl.so install
# python setup.py --with-openssl install
# python setup.py install

import sys
from xcoin_api_client import *
import pprint

pp = pprint.PrettyPrinter(indent=4, depth=2)

api_key = "aeb42a7d6bb79ec841dcc7023d858f85";
api_secret = "d7050adf37348992540b15525f51e3d0";

api = XCoinAPI(api_key, api_secret);

rgParams = {"currency" : "ETH"};
# rgParams = {"currency" : "XMR"};

#
# public api
#
# /public/ticker/{currency}              bithumb 거래소 마지막 거래 정보
# /public/orderbook/{currency}           bithumb 거래소 판/구매 등록 대기 또는 거래 중 내역 정보
# /public/recent_transactions/{currency} bithumb 거래소 거래 체결 완료 내역

# print("status: " + result["status"]);
result = api.xcoinApiCall("/public/ticker", rgParams);
pp.print(result)

#
# private api
#
# endpoint		=> parameters
# /info/current
# /info/account
# /info/balance
# /info/wallet_address

# result = api.xcoinApiCall("/info/account", rgParams);
# pp.pprint(result)

sys.exit(0);
