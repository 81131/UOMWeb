function calculateTimeComplexity() {
    const listLength = parseInt(document.getElementById("listLength").value);

    const linearTime = listLength; 
    const binaryTime = Math.ceil(Math.log2(listLength)); 

    const resultsDiv = document.getElementById("results");
    resultsDiv.innerHTML = `
        <h4>Results:</h4>
        <p style= "color: lightgray;">For a list length of <strong>${listLength}</strong>:</p>
        <ul>
            <li>Linear Search Time (O(n)): <strong>${linearTime} steps</strong></li>
            <li>Binary Search Time (O(log n)): <strong>${binaryTime} steps</strong></li>
        </ul>
    `;
    return false;
}
