# Import modules
import sys

# Function to try to convert to a string to an integer
# If successful, the converted integer is returned
# If unsuccessful, False is returned


# Create a clear cache (dictionary)


# global counter variables for the function calls and cache hits

# weight_on function calculates the weight on a specific person

    # Provide write access to the global counter variables

    # Increments the function counter variable because
    # we're calling this function again
    
    # Constant for how heavy each person is
    

    # If the row and column are already cached...
    
        # Increment the cache counter,
        
        # and return the cached value
        

    # If the coordinates are invalid or the row is 0,
    # return 0
    
    
    # Handle people on the left edge
    
        #Calculate the resulting weight on that person
        
    # Right edge

        #Calculate the resulting weight on that person
    
    # Middle person

        #Calculate the resulting weight on that person (remember there are two above)
    
    # Cache the result, because we know it's not cached yet
    

    # Return the result
    
# Main function
def main():
    # The argv is the height of the pyramid
    for i in range(len(sys.argv)):
        print(sys.argv[i])
# Get the number of rows if possible otherwise return and
# IndexError and ask for the height of the pyramid (try except)

# Except prompt the user for a number of rows

# Loop prompting the user until there's a valid height

# create start_time variable to time how long this takes

# Iterate through the rows (height)

    # Iterate through the people in the row
    
# variable for end time


# Print the results for timing and counters







if __name__ == '__main__':
    main()
