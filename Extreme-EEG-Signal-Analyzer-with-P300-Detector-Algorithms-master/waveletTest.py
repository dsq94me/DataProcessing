import numpy as np
import matplotlib.pyplot as plt

import pywt
import pywt.data

#eegData = np.genfromtxt('testData\\alpha_tp9.csv', delimiter=',')
#eegData = np.genfromtxt(r'C:\Users\dsq94\OneDrive\文档\WeChat Files\orthonormal\FileStorage\File\2020-11\museMonitor_132_re.csv', delimiter=',', dtype=None, encoding=None, skiprows = 1)
eegData = np.genfromtxt(r'C:\Users\dsq94\OneDrive\文档\WeChat Files\orthonormal\FileStorage\File\2020-11\museMonitor_697.csv', delimiter=',')
index_Alpha_TP9 = 9 #np.where(eegData[0] == 'Alpha_TP9')[0][0]
index_Beta_TP9 = 13 #np.where(eegData[0] == 'Beta_TP9')[0][0]
Alpha_TP9Data = eegData[1:, index_Alpha_TP9] #.astype(np.float)
Beta_TP9Data = eegData[1:, index_Beta_TP9] #.astype(np.float)

plt.plot(Alpha_TP9Data)
plt.ylabel("Muse Alpha_TP9Data")
plt.figure()

plt.plot(Beta_TP9Data)
plt.ylabel("Muse Beta_TP9Data")
plt.figure()


cA, cD = pywt.dwt(Beta_TP9Data, 'Rbio3.5')

approx = pywt.idwt(cA, None, 'Rbio3.5')
plt.plot(approx)
plt.ylabel("Approx TP9")
plt.figure()

# detail = pywt.idwt(cD, None, 'Rbio3.5')
# plt.plot(detail)
# plt.ylabel("Detailed TP9")

plt.figure()
plt.plot(cA)
plt.ylabel("Approx Points")

plt.figure()
plt.plot(cD)
plt.ylabel("Detailed Points")


plt.show()


# # Load image
# original = pywt.data.camera()
#
# # Wavelet transform of image, and plot approximation and details
# titles = ['Approximation', ' Horizontal detail',
#           'Vertical detail', 'Diagonal detail']
# coeffs2 = pywt.dwt2(original, 'bior1.3')
# LL, (LH, HL, HH) = coeffs2
# fig = plt.figure(figsize=(12, 3))
# for i, a in enumerate([LL, LH, HL, HH]):
#     ax = fig.add_subplot(1, 4, i + 1)
#     ax.imshow(a, interpolation="nearest", cmap=plt.cm.gray)
#     ax.set_title(titles[i], fontsize=10)
#     ax.set_xticks([])
#     ax.set_yticks([])
#
# fig.tight_layout()
# plt.show()