# ------------------------------------------------------------------------
# ENERGY PROFILER
#
# This script will do the following:
# - I dont know
# ------------------------------------------------------------------------
# Student Name:     Niall Trinder
# Student Number:   R00088254
# ------------------------------------------------------------------------

import pandas as pd
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage


def get_consumer_data(path):
    chunksize = 10000
    for chunk in pd.read_csv(path, chunksize=chunksize, nrows=10000):
        yield chunk


def process_data(path):
    # mostly junk code here to see what comes out
    con_5110 = pd.DataFrame()
    con_11617 = pd.DataFrame()
    for chunk in get_consumer_data(path):
        data = chunk
        data['ADVANCEDATETIME'] = pd.to_datetime(data['ADVANCEDATETIME'],
                                                 format='%d%b%y:%H:%M:%S')
        con_5110 = con_5110.append(data[data['ANON_ID'] == 5110])
        con_11617 = con_11617.append(data[data['ANON_ID'] == 11617])
    plt.plot(con_5110['ELECKWH'])
    plt.plot(con_11617['ELECKWH'])
    plt.show()

    # should have data from here to start clustering

    # next would be to bring in the survey data and assign the clustering res,
    # for all intents and purposes this would be an energy profiler

    # Some EDA should be here as well. Need some graphical output as well

    # now build the classification model to predict future customers energy
    # profile


# ------------------------------------------------------------------------
# MAIN FUNCTION
# ------------------------------------------------------------------------

def main():
    elec_data_path = 'data/7591elec/csv/edrp_elec.csv'
    process_data(elec_data_path)


# ------------------------------------------------------------------------
# PYTHON EXECUTION
# ------------------------------------------------------------------------

if __name__ == '__main__':
    main()
