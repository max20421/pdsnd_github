import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """​get_filters()
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!\n')
    while True:
        # get user input for city (chicago, new york city, washington)
        city = input("Please Enter City Name:\nChicago\nNew York City \nor Washington\n").lower()
        if city not in CITY_DATA.keys():
            print('{} is not a valid city name. Please enter Chicago, New York City or Washington'.format(city))
            continue
        else:
            break
    while True:        
        # get user input for month either all of Jan thru June which is all the data availability
        month = input("Enter The Month Name To Filter by month or All for no Filter: January, February, ... , June\n").lower()
        if month not in ('all','january', 'february', 'march', 'april', 'may', 'june'):
            print("Invlaid Month Choice Please Enter Valid Month")
            continue
        else:
            break
    while True:
        # get user input for day of week (all, monday, tuesday, ... sunday)
        day = input("Enter The Day of Week to Filter by Day or All for no Filter: Monday, Tuesday, ... Sunday\n").title()
        if day not in ('All', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'):
            print("Invlaid Day Choice Please Enter Valid Day of Week")
            continue
        else:
            break
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

    # load data file into a dataframe based on user choice in get_filters()
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract hour, month and day of week from Start Time to create new columns
    df['hour'] = df['Start Time'].dt.hour
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int only have data thru June
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable use cap A in All here to match the title format of the day column
    if day != 'All':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


    """Displays statistics on the most frequent times of travel."""
   
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # find the most popular month
    popular_month = df['month'].mode()[0]
    print('Most Popular Month of Year:', popular_month)

    # find the most popular day of week
    popular_day = df['day_of_week'].mode()[0]
    print('Most Popular Day of Week:', popular_day)

    # find the most popular hour
    popular_hour = df['hour'].mode()[0]
    print('Most Popular Start Hour:', popular_hour)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
   
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # find the most popular month
    popular_month = df['month'].mode()[0]
    #popular_month = df.mode['month'][0]
    print('Most Popular Month of Year:', popular_month)


    # find the most popular day of week
    popular_day = df['day_of_week'].mode()[0]
    print('Most Popular Day of Week:', popular_day)

    # find the most popular hour
    popular_hour = df['hour'].mode()[0]
    print('Most Popular Start Hour:', popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    
    # display most commonly used start station
    most_common_start = df['Start Station'].value_counts().idxmax() 
    print('Most Common Start Station:\n',most_common_start)

    # display most commonly used end station
    most_common_end = df['End Station'].value_counts().idxmax() 
    print('Most Common End Station:\n',most_common_end)

    # display most frequent combination of start station and end station trip
    df['station_combo'] = df['Start Station'].str.cat(df['End Station'],sep=" ")
    most_common_combo = df['station_combo'].value_counts().idxmax()
    print('Most Common Trip Combination:\n',most_common_combo)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def trip_duration_stats(df):
   """Displays statistics on the total and average trip duration."""
   print('\nCalculating Trip Duration...\n')
   start_time = time.time()
  # display total travel time
   total_travel_time = int(df['Trip Duration'].sum())
   print('Total Travel Time:',  total_travel_time)
   # display mean travel time
   mean_travel_time = int(df['Trip Duration'].mean())
   print('Travel Time Average:', mean_travel_time)
   print("\nThis took %s seconds." % (time.time() - start_time))
   print('-'*40)   
    
def user_stats(df):
    """Displays statistics on bikeshare users."""
    if "Gender" in df.columns:
        print('\nCalculating User Stats...\n')
        start_time = time.time()

        # display counts of user types
        user_types = df['User Type'].value_counts()
        print('Count of User Types:\n',user_types)

        # display counts of gender
        gender_count = df['Gender'].value_counts()
        print('Count of Gender:\n',gender_count)


        # display earliest year of birth
        birth_year_min = int(df['Birth Year'].min())
        print('Oldeset Birth year:', birth_year_min)

       # display most recent year of birth
        birth_year_max = int(df['Birth Year'].max())
        print('Latest Birth year:', birth_year_max)
        
       # most common year of birth  
        most_common_bdate = int(df['Birth Year'].mode())
        print('Most Common Birth Year:', most_common_bdate)

        print('\nThis took %s seconds.' % (time.time() - start_time))
        print('-'*40)
    else:
        print("Gender information is not available for Washington")

def display_raw_data(df):
    """Asks the user if the would like to see five rows of the bikeshare data."""
    # get user input to show data
    line_count = 0
    show_data = input("Would you like to see five rows of raw data\n Enter Yes or No \n").lower()
    while True:
        if show_data == 'no':
            break
        if show_data == 'yes':
            # print the first five rows
            print(df.iloc[line_count:line_count+5])
            # add five the line_count variable to display the next five rows if the user wants 
            line_count += 5
         # ask the user if they would like to see five more rows   
        show_data = input("Would you like to see five more rows of raw data\n Enter Yes or No \n").lower()        
    
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