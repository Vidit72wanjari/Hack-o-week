import pandas as pd
import numpy as np

def generate_data(n=500):

    occupancy = np.random.randint(5, 50, n)
    indoor_temp = np.random.uniform(20, 30, n)
    outdoor_temp = np.random.uniform(25, 40, n)

    cooling_load = (
        occupancy * 3 +
        indoor_temp * 2 +
        outdoor_temp * 1.5 +
        np.random.normal(0, 5, n)
    )

    df = pd.DataFrame({
        "Occupancy": occupancy,
        "Indoor_Temp": indoor_temp,
        "Outdoor_Temp": outdoor_temp,
        "Cooling_Load": cooling_load
    })

    return df