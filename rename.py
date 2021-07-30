# -*- coding: UTF-8 -*-
import os

nlist = os.listdir('./tmp_processed/')
cnt = 429
for n in nlist:
    os.rename('./tmp_processed/' + n, './tmp_processed/weibo' + str(cnt) + '.jpg')
    cnt = cnt + 1
