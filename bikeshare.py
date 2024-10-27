import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

cities = ['chicago', 'new york', 'washington']
months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("Please enter one of the following cities you want to see data for:\n[Chicago, New York,or Washington]\n").lower();
        if city in cities:
            break
        else:
            print('Please enter valid city.')

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("Please enter the month you want to explore.\nChoices: All, january, february, march, april, may, june \n").lower();
        if month in months:
            break
        else:
            print('Please enter a valid month.')

# TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Please enter the day of the week you want to explore.\nChoices: All, sunday, monday, tuesday, wednesday,thursday, friday, saturday \n").lower();
        if day in days:
            break
        else:
            print('Please enter a valid day')

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
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
    
        df = df[df['month'] == month]
    
    if day != 'all': 
        df = df[df['day_of_week'] == day.title()]
        return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    popular_month = df['month'].mode()[0]
    
    if popular_month == 1:
        popular_month = "January"
    elif popular_month == 2:
        popular_month = "February"
    elif popular_month == 3:
        popular_month = "March"
    elif popular_month == 4:
        popular_month = "April"
    elif popular_month == 5:
        popular_month = "May"
    elif popular_month == 6:
        popular_month = "June"
    print('Most common month: \n', popular_month)

    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0] 
    print('Most common day of the week: \n', popular_day) 

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour #PB
    popular_hour = df['hour'].mode()[0] #PB
    if popular_hour < 12:
        print('Most common start hour: \n', popular_hour, ' AM')
    elif popular_hour >= 12:
        if popular_hour > 12:
            popular_hour -= 12
        print('Most common start hour: \n', popular_hour, ' PM')

print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print("Most common start station: \n", popular_start_station)

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print("Most common end station: \n", popular_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    combo_station = df['Start Station'] + " to " +  df['End Station']
    common_combo_station = combo_station.mode()[0]
    print("Most common trip from start to end:\n {}".format(common_combo_station))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_duration = df['Trip Duration'].sum()
    minute, second = divmod(total_duration, 60)
    hour, minute = divmod(minute, 60)
    print("The Total Travel Time is {} Hours, {} Minutes, and {} Seconds.".format(hour, minute, second))

    # TO DO: display mean travel time
    average_duration = round(df['Trip Duration'].mean())
    minute, second = divmod(average_duration, 60)
    if minute> 60:
        hour, minute = divmod(minute, 60)
        print('The average travel time is {} hours, {} minutes, and {} seconds.'.format(hour, minute, second))
    else:
        print('The average trip duration is {} minutes and {} seconds.'.format(minute, second))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print("Counts of each user type:\n", user_types)

    # TO DO: Display counts of gender
    try:
        gender = df['Gender'].value_counts()
        print(' ' * 40)
        print('Counts of Each User Gender:')
        print(gender)
    except:
        print('Counts of Each User Gender:\nSorry, no gender data available for {} City'.format(city.title()))

# TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest = df['Birth Year'].min() #Oldest birth year
        recent = df['Birth Year'].max() #Youngest birth Year
        common = df['Birth Year'].mode() #This gives the Common Birth Year 
        print(' ' * 40)
        print('Counts of User Birth Year:')
        print('Oldest User(s) Birth Year: ', int(earliest))
        print('Youngest User(s) Birth Year: ', int(recent))
        print('Most Common Birth Year: ', int(common))
    except:
        print('Counts of User Birth Year:\nSorry, no birth year data available for {} City'.format(city.title()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
# Use descriptive statistics to answer questions about the data.
def individual_data(df):       
    start_data = 0
    end_data = 5
    df_length = len(df.index)
    
    while start_data < df_length:
        raw_data = input("Would you like to see individual trip data?\nEnter 'yes' or 'no'")
        if raw_data.lower() == 'yes':
            
            print("Displaying only 5 rows of data.")
            if end_data > df_length:
                end_data = df_length
            print(df.iloc[start_data:end_data])
            start_data += 5
            end_data += 5
        else:
            break;

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
