''' 
Twitter Analysis
Various functions for analyzing twitter marketplace data
June 2018
'''
import pandas as pd
import numpy as np
from numpy import random
import matplotlib.pyplot as plt
import time
from cycler import cycler

#######################################
######### Loading data ################
#######################################

#Load data and convert time to appropriate format
def prep_data():
    df = pd.read_csv("twitter_marketplace_data.csv")
    #convert datetime to a datetime type
    df['datetime'] = pd.to_datetime(df['datetime'])
    #sort by datetime
    df = df.sort_values('datetime')
    #calculate time as a float (in units of hours)
    df['hour'] = (df['datetime'] - df['datetime'].iloc[0]) / np.timedelta32(1,'h')
    
    return df

#######################################
######### Analysis of spend ###########
#######################################

#Plots spend vs time for a particular campaign
def spendvtime( df, campaign_id ):
    spend = df[df['campaign_id'] == campaign_id]['campaign_spend'].tolist()
    time = df[df['campaign_id'] == campaign_id]['datetime'].tolist()
    
    plt.scatter(time, spend,lw=0,s=2)
    
    ax = plt.gca()
    
    plt.xlim(min(time),max(time)) 
    plt.setp(ax.get_xticklabels(), rotation=30, horizontalalignment='right')

#plots spend vs time for all campaigns together
def spendvtime_all(df):
    campaign_ids = np.sort(df['campaign_id'].unique())
    
    plt.figure()
    plt.axis()
    ax = plt.gca()
    ax.set_prop_cycle( cycler('color', ['b', 'g', 'r', 'c', 'm', 'y', 'k']))
    
    for campaign_id in campaign_ids:
        spend = df[df['campaign_id'] == campaign_id]['campaign_spend'].tolist()
        time = df[df['campaign_id'] == campaign_id]['hour'].tolist()
    
        #ax.scatter(time, spend,lw=0,s=2)
        ax.plot(time,spend,label='Campaign %i' % campaign_id)
    
    plt.xlim(min(df['hour']),max(df['hour'])) 
    plt.setp(ax.get_xticklabels(), rotation=30, horizontalalignment='right')
    plt.legend(loc='best',fontsize=10)
    
    plt.title('Spend vs time')
    plt.xlabel('Time (hours)')
    plt.ylabel('Dollars spent')
    
#######################################
######### Analysis of engagement ######
#######################################

#Function based on an initial misunderstanding of engagement rate
#plots the number of charges per unit time.  Binned such that the average number of charges per bin is avg_per_bin
#avg_per_bin is hardcoded for now
def engagementvtime(df, campaign_id):
    avg_per_bin = 10
    charge_times = df[np.logical_and(df['campaign_id'] == campaign_id, df['charged'] > 0)]['datetime'].tolist()
    
    num_charges = len(charge_times)
    num_bins = int( num_charges / avg_per_bin )
    
    #currently only plots the number of charges per bin, and doesn't divide by the size of the bin.
    print(num_bins)
    plt.hist(charge_times,num_bins)
    
    ax = plt.gca()
    plt.setp(ax.get_xticklabels(), rotation=30, horizontalalignment='right')
    
#Function based on an initial misunderstanding of engagement rate
#looks at how many ads were seen by users, and assumes a constant pclick conditional on impression.
def engagementvtime2(df, campaign_id):
    avg_per_bin = 50
    num_charges = np.sum(np.logical_and(df['campaign_id'] == campaign_id, df['charged'] > 0))
    imp_times = df[np.logical_and(df['campaign_id'] == campaign_id, df['seen_by_user'])]['hour'].tolist()
    
    num_imps = len(imp_times)
    num_bins = int( num_imps / avg_per_bin )
    
    #print(num_imps, num_bins)
    engagement,time = np.histogram(imp_times,num_bins)
    time_center = (time[1:] + time[:-1] ) / 2
    #convert engagement to units of charges per hour
    engagement = engagement * num_charges / num_imps / (time[1] - time[0])
    
    plt.plot(time_center, engagement)
    
    ax = plt.gca()
    plt.xlim(min(imp_times),max(imp_times)) 
    plt.xlabel('Time (hours)')
    plt.ylabel('Estimated charges per hour')
    plt.title('Engagement rate of campaign %i' % campaign_id)
    
#I realized that I understood the term "engagement rate" wrong.
#Here I calculate the engagement rate, defined as the number of charges per number of seen impressions.
def engagement_rate(df,campaign_id):
    num_charges = np.sum(np.logical_and(df['campaign_id'] == campaign_id, df['charged'] > 0))
    num_imps = np.sum(np.logical_and(df['campaign_id'] == campaign_id, df['seen_by_user']))
    return num_charges / num_imps
    