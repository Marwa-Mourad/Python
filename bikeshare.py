import time
import pandas as pd
import numpy as np

CITY_DATA = { 'CH': 'chicago.csv',
              'NYC': 'new_york_city.csv',
              'W': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    city=input('Enter city name as follows:\n CH fo Chicago\n NYC for New York City\n W for Washington\n').upper()
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while city!='CH' and city!='NYC' and city!='W':
         print ('Invalid input')
         city=input('Enter city name as follows:\n CH fo Chicago\n NYC for New York City\n W for Washington\n').upper()
    month=input('Enter month of required statistics from the following options:\n 0 for All\n 1 for January\n 2 for February\n 3 for March\n 4 for April\n 5 for May\n 6 for June\n')
    while month!='0' and month!='1' and month!='2' and month!='3' and month!='4' and month!='5' and month!='6':
         print ('Invalid input')
         month=input('Enter month of required statistics from the following options:\n 0 for All\n 1 for January\n 2 for February\n 3 for March\n 4 for April\n 5 for May\n 6 for June\n')
    # TO DO: get user input for month (all, january, february, ... , june)

    day=input('Enter weekday of required statistics from the following options:\n 0 for All\n 1 for Sunday\n 2 for Monday\n 3 for Tuesday\n 4 for Wednesday\n 5 for Thursday\n 6 for Friday\n 7 for Saturday\n')
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while day!='0' and day!='1' and day!='2' and day!='3' and day!='4' and day!='5' and day!='6' and day!='7':
         print ('Invalid input')
         day=input('Enter weekday of required statistics from the following options:\n 0 for All\n 1 for Sunday\n 2 for Monday\n 3 for Tuesday\n 4 for Wednesday\n 5 for Thursday\n 6 for Friday\n 7 for Saturday\n')

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    start_loc = 0
    display=input('Do you like to view 5 rows of data?\n Yes\n No\n').lower()
    while display != 'yes' and display!='no':
        print ('Invalid input')
        display=input('Do you like to view 5 rows of data?\n Yes\n No\n').lower()
    while (display == 'yes'):
        print(df.iloc[start_loc:(start_loc+5)])
        start_loc += 5
        display=input('Do you like to view next 5 rows of data?\n Yes\n No\n').lower()


    df.fillna(method='ffill',axis=0)
    df.fillna(method='backfill',axis=0)
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month from the Start Time column to create a month column
    df['month'] = df['Start Time'].dt.month

    # find the most common month
    pop_month =  df['month'].mode()[0]
    month_names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
    popular_month = month_names[pop_month - 1]
    print('Most Frequent Start month:', popular_month)


    # TO DO: display the most common day of week
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract day from the Start Time column to create a day column
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # find the most common day
    popular_day =  df['day_of_week'].mode()[0]
    print('Most Frequent Start day:', popular_day)


    # TO DO: display the most common start hour
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month from the Start Time column to create a month column
    df['month'] = df['Start Time'].dt.month

    # find the most common month
    pop_month =  df['month'].mode()[0]
    month_names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
    popular_month = month_names[pop_month - 1]

    print('Most Frequent Start month:', popular_month)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('Most Used Start Station:', popular_start_station)
    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('Most Used End Station:', popular_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['comb_start_end_stations'] = df['Start Station']+df['End Station']
    popular_comb_start_end_stations=df['comb_start_end_stations'].mode()[0]
    print('Most Used Combination of Start and End Station:', popular_comb_start_end_stations)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    df['Trip Duration'] = pd.to_numeric(df['Trip Duration'])
    total_travel_time = df['Trip Duration'].sum()
    print('Total Travel Time:', total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean Travel Time:', mean_travel_time)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats1(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculatin User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df.groupby(['User Type'])['User Type'].count()
    print(user_types)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats2(df):
    """Continue Displaying statistics on bikeshare users."""

    print('\nContinue Calculatin User Stats ...\n')
    start_time = time.time()

    # TO DO: Display counts of gender
    gender = df.groupby(['Gender'])['Gender'].count()
    print (gender)
    # TO DO: Display earliest, most recent, and most common year of birth
    earliest_birth_year = df['Birth Year'].min()
    recent_birth_year = df['Birth Year'].max()
    common_birth_year = df['Birth Year'].mode()[0]
    print ('Earliest Birth Year:', earliest_birth_year)
    print ('Recent Birth Year:', recent_birth_year)
    print ('Common Birth Year:', common_birth_year)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats1(df)
        if city =='W':
            print ('No gender or birth year data is available for Washington')
        else:
            user_stats2(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
