import time
import pandas as pd
import numpy as np
import calendar

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():

    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('\nHello! Let\'s explore some US bikeshare data!')
    
    
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    cities = ['chicago', 'new york city', 'washington']
    city = input('\nPlease select a city from Chicago, New York City or Washington to see its data\n').lower()
    while city not in cities:
        city = input('\n{} isn\'t from the specified cities Please enter one of the specified cities\n'.format(city.title())).lower()
                            
    print('\nYou chose to show the data regarding ({})\n'.format(city.title()))

    # TO DO: get user input for month (all, january, february, ... , june)
    months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
    month = input('Please select the month you want to filter by, type all to apply no filter\n*Note that we currently have data for the first 6 months only\n').lower()
    while month not in months and month != 'all':
        month = input('\n{} isn\'t a valid month, please enter a valid month, remember we currently have data for the first 6 months only\n'.format(month.title())).lower()

    print('\nYou chose to show the data regarding ({})\n'.format(month.title()))

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['all', 'saturday', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday']
    day = input('Please select the day you want to filter by, type all to apply no filter\n').lower()
    while day not in days and day != 'all':
        day = input('{} isn\'t a valid day, please enter a valid day of the week\n'.format(day.title())).lower()


    print('\nYou chose to show the data regarding ({})\n'.format(day.title()))
    
    print('Please wait while we calculate the data you requested\n')

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
    
    #convert start time to date time
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    #extract month, day name , and hour from start time
    df['month'] = df['Start Time'].dt.month_name()

    df['day_name'] = df['Start Time'].dt.day_name()

    df['hour'] = df['Start Time'].dt.hour
    
    # if the user didn't choose all to filter, filter by the selected month
    if month != 'all':

        df = df[df['month'] == month.title()]
    
    # if the user didn't choose all to filter, filter by the selected day
    if day != 'all':
        
        df = df[df['day_name'] == day.title()]
    

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
        
    # TO DO: display the most common month
    most_common_month = df['month'].mode()[0]
    print('The most common month is {}\n'.format(most_common_month))

    # TO DO: display the most common day of week
    most_common_day = df['day_name'].mode()[0]
    print('The most common day is {}\n'.format(most_common_day))
    
    # TO DO: display the most common start hour
    most_common_hour = df['hour'].mode()[0]
    print('The most common hour is {}\n'.format(most_common_hour))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station = df['Start Station'].mode()[0]
    print('The most common start station is: {}\n'.format(most_common_start_station))

    # TO DO: display most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]
    print('The most common end station is: {}\n'.format(most_common_end_station))


    # TO DO: display most frequent combination of start station and end station trip
    df['The most common trip'] = df['Start Station'] + ' ' + df['End Station']
    most_frequent_combination = df['The most common trip'].mode()[0]
    print('The most frequent trip is between ({})\n'.format(most_frequent_combination))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time and converting the output which is in seconds to hours, minutes and seconds
    seconds1 = df['Trip Duration'].sum()
    seconds1 = seconds1 % (24 * 3600) 
    hour1 = seconds1 // 3600
    seconds1 %= 3600
    minutes1 = seconds1 // 60
    seconds1 %= 60
    print('Total travel time is {} hours {} minutes and {} seconds\n'.format(int(hour1), int(minutes1), int(seconds1)))

    # TO DO: display mean travel time and converting the output which is in seconds to hours, minutes and seconds
    seconds2 = df['Trip Duration'].mean()
    seconds2 = seconds2 % (24 * 3600)
    hour2 = seconds1 // 3600
    seconds2 %= 3600
    minutes2 = seconds2 // 60
    seconds2 %= 60
    print('The average travel time is {} hours {} minutes and {} seconds\n'.format(int(hour2), int(minutes2), int(seconds2)))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    # display number of subscribers
    number_of_subscribers = (df['User Type'] == 'Subscriber').sum()
    print('Number of subscriber is {}\n'.format(number_of_subscribers))
    
    # display number of customers
    number_of_customers = (df['User Type'] == 'Customer').sum()
    print('Number of customers is {}\n'.format(number_of_customers))
    
    # display total number of users
    total_num = number_of_subscribers + number_of_customers
    print('Total number of users is {}\n'.format(total_num))

    # TO DO: Display counts of gender
    
    # display number of male users
    # used try and except so that if the city didn't provide data for the gender and birth year a message will
    # appear stating that the city didn't provide said data
    try:
        number_of_males = (df['Gender'] == 'Male').sum()
        print('Number of male users is {}\n'.format(number_of_males))
    
    # number of female users
        number_of_females = (df['Gender'] == 'Female').sum()
        print('Number of female users is {}\n'.format(number_of_females))

    # TO DO: Display earliest, most recent, and most common year of birth
        earliest_year = df['Birth Year'].min()
        print('The oldest users was born in {}\n'.format(int(earliest_year)))

        most_recent_year = df['Birth Year'].max()
        print('The youngest users was born in {}\n'.format(int(most_recent_year)))

        most_common_year = df['Birth Year'].mode()[0]
        print('The most common birth year is {}\n'.format(int(most_common_year)))
    
    except:
        print('We apologize, the city you chose didn\'t provide data for Gender or Birth year')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_raw_data(df):
    """Displays raw data on user request.
    Args:
        (DataFrame) df - Pandas DataFrame containing city data filtered by month and day
    """
    #asking the user if he or she wants to show the head (first 5 rows of data) of the DataFrame
    view_head = input('\nWould you like to view the first five row of raw data? Enter yes or no.\n')

    #if the user said yes displaying the data and if he wrote no, then start the next function
    if view_head.lower() != 'yes':
        return

    print(df.head())
    
    #if the user chose to display the head of the DataFrame then asking again if he or she wants to show another 5 rows
    next = 0
    
    while True:
        view_raw_data = input('\nWould you like to view next five row of raw data? Enter yes or no.\n')
        if view_raw_data.lower() != 'yes':
            return
        next += 5
        
        print(df.iloc[next:next+5])


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()