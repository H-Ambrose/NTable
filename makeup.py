# -*- coding: UTF-8 -*-
import os

nlist = os.listdir('./weibo_processed/')
cnt = 0
for n in nlist:
    os.rename('./weibo_processed/' + n, './weibo_processed/weibo' + str(cnt) + '.jpg')
    cnt = cnt + 1
