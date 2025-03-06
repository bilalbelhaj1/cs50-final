document.addEventListener('DOMContentLoaded', () => {
    // Generate random fact functionality
    const funFacts = [
        "Elephants communicate through vibrations and sounds over long distances.",
        "Giraffes have long necks to reach high leaves and branches.",
        "Cheetahs are the fastest land animals, reaching speeds of 60 mph.",
        "A group of flamingos is called a 'flamboyance' due to their colors.",
        "Kangaroos use their tails for balance while hopping across terrain.",
        "Penguins are excellent swimmers, but they cannot fly through air.",
        "Owls have silent flight, allowing them to hunt in silence.",
        "Sloths spend most of their lives hanging upside down from trees.",
        "Dolphins are known for their intelligence and social interaction skills.",
        "Polar bears are strong swimmers and live in freezing Arctic environments."
    ];

    const fact = document.querySelector('.fact');
    const newFctBtn = document.getElementById('newFactBtn');
    
    function generateFact() {
        const randomIndex = Math.floor(Math.random() * funFacts.length);
        fact.innerText = '"' + funFacts[randomIndex] + '"';
    }
    newFctBtn.addEventListener('click', generateFact);

    const questions = document.getElementsByClassName('content-container');

    for (let i = 0; i < questions.length; i++) {
        questions[i].addEventListener('click', function (e) {
            this.classList.toggle('active-question');
            e.preventDefault();
        });
    } 
});