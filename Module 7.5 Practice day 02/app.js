// fetch('https://jsonplaceholder.typicode.com/comments')
//       .then(response => response.json())
//       .then(json => console.log(json))



document.addEventListener('DOMContentLoaded', function() {
    // Get the button and the div where data will be displayed
    const getDataBtn = document.getElementById('getDataBtn');
    const displayDataDiv = document.getElementById('displayData');

    // Add a click event listener to the button
    getDataBtn.addEventListener('click', function() {
        // Simulate fetching data (replace this with your actual data fetching logic)
        const data = fetchData();

        // Display the data in the div
        displayDataDiv.innerHTML = `<p>${data}</p>`;
    });

    // Function to simulate fetching data
    function fetchData() {
        // Replace this with your actual data fetching logic
        return 'This is the data!';
    }
});
