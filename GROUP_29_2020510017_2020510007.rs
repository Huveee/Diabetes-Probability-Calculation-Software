// Function to calculate the Euclidean distance between two points
fn euclidean_distance(point1: &[f64], point2: &[f64]) -> f64 {
    // Calculate the sum of squared differences between corresponding elements of point1 and point2
    let sum: f64 = point1.iter()
                         .zip(point2.iter())  // Pair up elements from both points
                         .map(|(a, b)| (a - b).powi(2))  // Calculate the squared difference for each pair
                         .sum();  // Sum all the squared differences
    sum.sqrt()  // Return the square root of the sum, which is the Euclidean distance
}

fn main() {
    // Define the first point with eight dimensions
    let point1 = [6.0, 148.0, 72.0, 35.0, 0.0, 33.6, 0.627, 50.0];
    // Define the second point with eight dimensions
    let point2 = [1.0, 85.0, 66.0, 29.0, 0.0, 26.6, 0.351, 31.0];

    // Calculate the Euclidean distance between the two points
    let distance = euclidean_distance(&point1, &point2);
    // Print the calculated distance with two decimal precision
    println!("Euclidean Distance: {:.2}", distance);
}
