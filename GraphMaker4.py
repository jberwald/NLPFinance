import numpy as np
import matplotlib.pyplot as plt
#2013-2016, 10 bins, flipped, filesize

month1 = [-0.007278702455696207, 0.025807440694029852, 0.021664741649253732, 0.004074311119402984, 0.014181087170370369, 0.010220111353383457, 0.023866421360902255, 0.025855300755555553, 0.017356618714285715, 0.015322886097744359]
month3 = [0.018893899284810126, 0.0782763903283582, 0.04211134023134328, 0.051360793589552235, 0.028424938785185185, 0.03406582679699248, 0.05230850210526315, 0.047828989911111106, 0.05615278130827068, 0.04114484357894736]
month6 = [0.06556213227215191, 0.14912534764925373, 0.10787796660447761, 0.11315629182089552, 0.07000203926666668, 0.09570905912781955, 0.07018809166165413, 0.0863324622148148, 0.06524892439849624, 0.06590523253383458]
month12 = [0.12017091920253166, 0.283532201380597, 0.1976728851567164, 0.22098792470895523, 0.1543499547185185, 0.1875753476917293, 0.15329284303759397, 0.10335747401481483, 0.1559701405037594, 0.1296698942857143]
x = [1,2,3,4,5,6,7,8,9,10]

plt.xlabel('File Size Deciles')
plt.ylabel('Mean Return')
plt.title('10-K Relative Returns vs. File Sizes')
plt.plot(x, month1, '-o', color='black', marker='^', ms=14, lw=2, alpha=1, mfc='black', label='1 Month')
plt.plot(x, month3, '-o', color='blue', marker='o', ms=10, lw=2, alpha=1, mfc='blue', label='3 Month')
plt.plot(x, month6, '-o', color='red', marker='s', ms=12, lw=2, alpha=1, mfc='red', label='6 Month')
plt.plot(x, month12, '-o', color='green', marker='*', ms=14, lw=2, alpha=1, mfc='green', label='12 Month')
plt.legend(loc=1)

plt.show()