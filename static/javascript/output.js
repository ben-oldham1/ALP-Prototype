function runCode() {
    const outputDiv = document.getElementById('output');
    let step = 0;
    let name = '';
    let age = 0;

    function addToOutput(text) {
        outputDiv.innerHTML += text + '<br>';
        outputDiv.scrollTop = outputDiv.scrollHeight; // Auto-scroll to the bottom
    }

    addToOutput(">>> run main.py");
    addToOutput("Welcome to the 100th Birthday Calculator!")
    addToOutput("What is your name?");

    document.getElementById('input').addEventListener('keydown', function (event) {
        if (event.key === 'Enter') {
            const input = event.target.value;
            event.target.value = ''; // Clear the input field

            if (step === 0) {
                name = input;
                addToOutput("How old are you?");
                step++;
            } else if (step === 1) {
                age = parseInt(input, 10);
                if (isNaN(age)) {
                    addToOutput("Please enter a valid number for age.");
                } else {
                    const currentYear = new Date().getFullYear();
                    const yearTurn100 = currentYear + (100 - age);
                    addToOutput(`Hello, ${name}! You will turn 100 years old in the year ${yearTurn100}.`);
                }
            }
        }
    });
};

const clearTerminal = () => {
    document.getElementById('terminal').innerHTML = '';
}