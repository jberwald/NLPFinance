import numpy as np
import matplotlib.pyplot as plt
#tfidf, pca, 50svals, 100 estimators, rf

month1= [0.003590317538052235, 0.006037493966947749, 0.004700003031114715, 0.0037777364384003784, -0.004000305272332671, 0.007584151017689817, -0.0007277368809861102, 0.014287082609427916, -0.0010896481203239653, 0.010278568657583222]
month3=[0.040740395053625006, 0.021619385802353834, 0.026067266528329962, 0.030370056875414348, 0.025532866986624336, 0.012825972664737426, 0.024734866303243497, 0.03321243619716336, 0.04439988081226234, 0.004972966287326869]
month6= [0.03498917031444297, 0.02901267858546693, 0.02680588650110629, 0.03136225749858222, 0.02113442175797685, 0.01426543118113179, 0.020962565005498677, 0.033362871042928226, 0.04405916997723677, 0.00584732200731225]
month12=[0.08702374771250794, 0.08550277431179602, 0.09956999953518346, 0.10812988076451453, 0.07809389068066203, 0.09415879767498149, 0.10360888370946031, 0.10977101087827251, 0.06441271394137367, 0.0767160237666238]
x = [1,2,3,4,5,6,7,8,9,10]

plt.xlabel('2013-2015 Return Bins')
plt.ylabel('2016 Mean Returns')
plt.title('PCA & Random Forests')
plt.plot(x, month1, '-o', color='black', marker='^', ms=14, lw=2, alpha=1, mfc='black', label='1 Month')
plt.plot(x, month3, '-o', color='blue', marker='o', ms=10, lw=2, alpha=1, mfc='blue', label='3 Month')
plt.plot(x, month6, '-o', color='red', marker='s', ms=12, lw=2, alpha=1, mfc='red', label='6 Month')
plt.plot(x, month12, '-o', color='green', marker='*', ms=14, lw=2, alpha=1, mfc='green', label='12 Month')
plt.legend(loc=6)

plt.show()