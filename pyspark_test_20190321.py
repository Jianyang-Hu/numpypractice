# -*- coding: utf-8 -*-
# @version : Python3.6
# @Time    : 2019/3/21 14:58
# @Author  : Jianyang-Hu
# @contact : jianyang1993@163.com
# @File    : pyspark_test_20190321.py
# @Software: PyCharm

from pyspark import SparkContext
from pyspark import SparkContext as sc
from pyspark import SparkConf

conf=SparkConf().setAppName("miniProject").setMaster("local[*]")
sc2=SparkContext.getOrCreate(conf)
rdd = sc2.parallelize([1,2,3,4,5])
rdd
print(rdd)
print(rdd.getNumPartitions() )






df_dic, mzlist_dic = be.extract_all_mz(out_path, dic_msdata, mspola, dic_id,
                                       intensity_thre=1e5, min_scan_num=5)