import pandas as pd
import numpy as np

data = np.array([2,4,5,3,7,5,8,900,10000,4,6,7,8])

threshold = 3
data_mean = np.mean(data)
data_std_deviation = np.std(data)

z_score = (data - data_mean)/data_std_deviation

final_anamolies = pd.DataFrame(
    {
        "original_value" : data,
        "z_score" : z_score,
        "is_anamoly" : np.abs(z_score)> threshold
    }
)

# print(final_anamolies)

"""---------------------------------------------------------------------------------------------"""

from scipy import stats
import numpy as np
data = [2,4,5,3,7,5,8,900,10000,4,6,7,8] #skew

final_z_score = stats.zscore(data)
print(final_z_score)

anamoly_detection = np.abs(final_z_score) > 2
print(anamoly_detection)

"""---------------------------------------------------------------------------------------------------"""

from scipy import stats
import numpy as np
data = [2,4,5,3,7,5,8,900,1000,4,6,7,8] #skew

final_z_score = stats.zscore(data)
print(final_z_score)

anamoly_detection = np.abs(final_z_score) > 2
print(anamoly_detection)

"""scipy.stats
1. Descriptive stats
2. Distribution stats
3. Correlation 
4. hypothesis
5. random sampling
6. outlier detection (anamoly)"""