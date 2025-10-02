// Sample JavaScript file with various issues
console.log('Starting application...'); // Should use proper logging

function processData(data) {
    console.log('Processing data:', data); // Should use proper logging
    return data.map(item => item * 2);
}

function calculateSum(a, b) {
    // Missing JSDoc comment
    return a + b;
}

function dangerousFunction(userInput) {
    // This is dangerous - eval with user input
    return eval(userInput); // Security risk
}

// Using var instead of let/const
var globalVariable = "bad practice";

// Missing error handling
function fetchData(url) {
    fetch(url)
        .then(response => response.json())
        .then(data => console.log(data));
    // No error handling
}

// TODO: Add error handling
// FIXME: This function needs optimization
// HACK: Temporary solution

function main() {
    console.log('Application started'); // Should use proper logging
    
    const data = [1, 2, 3, 4, 5];
    const processed = processData(data);
    
    console.log('Processed data:', processed); // Should use proper logging
    console.log('Application completed'); // Should use proper logging
}

main();
