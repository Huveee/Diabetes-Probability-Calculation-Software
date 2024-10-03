# Function to calculate the Euclidean distance between two points
def euclidean_distance(point1, point2)
    sum = 0  # Variable to accumulate the sum of squared differences
    point1.each_with_index do |p, i|  # Iterate over each element of point1 with its index
      sum += (p - point2[i])**2  # Add the squared difference to the sum
    end
    Math.sqrt(sum)  # Return the square root of the sum
  end
  
  # Define the first point with eight dimensions
  point1 = [6, 148, 72, 35, 0, 33.6, 0.627, 50]
  # Define the second point with eight dimensions
  point2 = [1, 85, 66, 29, 0, 26.6, 0.351, 31]
  
  # Calculate the Euclidean distance between the two points
  distance = euclidean_distance(point1, point2)
  # Print the calculated distance with two decimal precision
  puts "Euclidean Distance: %.2f" % distance