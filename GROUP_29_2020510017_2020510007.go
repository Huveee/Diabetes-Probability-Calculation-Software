package main

import (
	"fmt"    // Importing the fmt package for formatted I/O operations
	"math"   // Importing the math package for mathematical functions
)

// Function to calculate the Euclidean distance between two points
func euclideanDistance(point1, point2 []float64) float64 {
	var sum float64  // Variable to accumulate the sum of squared differences
	for i := range point1 {  // Loop over each dimension of the points
		sum += math.Pow(point1[i] - point2[i], 2)  // Add the squared difference to the sum
	}
	return math.Sqrt(sum)  // Return the square root of the sum
}

func main() {
	// Define the first point with eight dimensions
	point1 := []float64{6, 148, 72, 35, 0, 33.6, 0.627, 50}
	// Define the second point with eight dimensions
	point2 := []float64{1, 85, 66, 29, 0, 26.6, 0.351, 31}

	// Calculate the Euclidean distance between the two points
	distance := euclideanDistance(point1, point2)
	// Print the calculated distance with two decimal precision
	fmt.Printf("Euclidean Distance: %.2f\n", distance)
}
