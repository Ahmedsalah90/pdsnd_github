import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

#this function for recieving your input

city = (input("kindly inter the name of the city you want to analyse^_^:")).lower()
if city not in ['chicago', 'new york city', 'washington']:
    print('Sorry, city does not exist,kindly expilictly choose one of the following cities(chicago/new york city/washinton')
    city = (input("kindly inter the name of the city you want to analyse^_^")).lower()
month = (input("kindly inter the name of the month you want to analyse^_^:")).lower()
if month not in ['january', 'february', 'March', 'may', 'june', 'july']:
    print('Sorry, month does not exist,kindly try again')
    month = (input("kindly inter the name of the month you want to analyse^_^: ")).lower()
day = (input("kindly inter the name of the day you want to analyse^_^: ")).lower()
if day not in ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']:
    print('Sorry, day does not exist,kindly try again')
    day = (input("kindly inter the name of the day you want to analyse^_^: ")).lower()
print('Hello! Let\'s explore some US bikeshare data!')



def load_data(city, month, day):

    df = pd.read_csv(CITY_DATA[city])

    df['Start Time']=pd.to_datetime(df['Start Time'])


    df['month'] = df['Start Time'].dt.month
    df['week'] = df['Start Time'].dt.weekofyear
    df['day_of_week'] = df['Start Time'].dt.weekday_name


    if month != 'all':

        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1


        df = df[df['month'] == month]


    if day != 'all':

        df = df[df['day_of_week'] == day.title()]

        return df
# this function to Calculating time stats
def time_stats(df2):
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    df2 = load_data(city, month, day)
    popular_month = df2['month'].mode()[0]
    popular_week = df2['week'].mode()[0]
    popular_day = df2['day_of_week'].mode()[0]

    print('Most Popular  month:', popular_month)
    print('Most Popular  week:', popular_week)
    print('Most Popular day:', popular_day)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
time_stats(load_data(city, month, day))
print(time_stats)
def station_stats(df3):

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    df3 = load_data(city, month, day)
    popular_start_station = df3['Start Station'].mode()[0]
    popular_End_station= df3['End Station'].mode()[0]

    df3['frequency'] = df3['End Station']
    end_start_station = df3.groupby(['Start Station', 'End Station']).agg({'frequency': 'count'})
    most_popular_combo = end_start_station[ end_start_station['frequency'] == end_start_station['frequency'].max() ]


    print('Most Popular  Start Station:', popular_start_station)
    print('Most Popular  End Station:', popular_End_station)
    print('Most Popular  Start-End Stations Combonation:', most_popular_combo)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
station_stats(load_data(city, month, day))
print(station_stats)

def trip_duration_stats(df4):

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    total_travel_time= df4['Trip Duration'].sum()
    mean_travel_time= df4['Trip Duration'].mean()
    print('The total travel time is :', total_travel_time)
    print('The mean travel time is :', mean_travel_time)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
trip_duration_stats(load_data(city, month, day))
print(station_stats)

def user_stats(df5):

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    user_types = df5['User Type'].value_counts()
    if city != 'washington':
        user_gender = df5['Gender'].value_counts()
        most_common_year_birth = df5['Birth Year'].mode()[0]
        most_recent_year_birth = df5['Birth Year'].max()
        most_early_year_birth = df5['Birth Year'].min()
        print('The total count of gender:', user_gender)
        print('The most common year of birth: ', most_common_year_birth)
        print('The recent year of birth: ', most_recent_year_birth)
        print('The earliest year of birth: ', most_early_year_birth)
    else:
        print('Sorry, birth data and gender are not available!')
    print('The total count of user type is :', user_types)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
user_stats(load_data(city, month, day))
print(user_stats)


def raw_data_display(df6):
 raw_data = (input("Do you want to see five rows of raw data Yes/No:")).lower()
 if raw_data not in ['yes', 'no']:
    print('Sorry, please choose Yes/No')
    raw_data = (input("Do you want to see five rows of raw data Yes/No:")).lower()
 from_index = 0
 to_index = 5
 print(df6.iloc[from_index:to_index])
 while raw_data == 'yes' :
    raw_data = (input("Do you want to see five rows of raw data Yes/No:")).lower()
    from_index += 5
    to_index += 5
    print(df6.iloc[from_index:to_index])
    if raw_data not in ['yes', 'no']:
        print('Sorry, please choose Yes/No')
        raw_data = (input("Do you want to see five rows of raw data Yes/No:")).lower()



raw_data_display(load_data(city, month, day))
