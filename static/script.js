// Get elements for the modal and check-in button
const checkInBtn = document.getElementById("check-in-btn");
const modal = document.getElementById("check-in-modal");
const closeBtn = document.getElementById("close-btn");
const submitCheckInBtn = document.getElementById("submit-check-in");

// Open the modal when the Check-in button is clicked
checkInBtn.addEventListener("click", function() {
    modal.style.display = "block";
});

// Close the modal when the close button is clicked
closeBtn.addEventListener("click", function() {
    modal.style.display = "none";
});

// Close the modal if clicked outside of the modal content
window.addEventListener("click", function(event) {
    if (event.target === modal) {
        modal.style.display = "none";
    }
});

// Handle check-in submission
submitCheckInBtn.addEventListener("click", function() {
    const goalFollowed = document.querySelector('input[name="goal-followed"]:checked');
    const badHabit = document.querySelector('input[name="bad-habit"]:checked');
    const journal = document.getElementById("journal").value;

    // Check if both questions are answered
    if (goalFollowed && badHabit) {
        // Increment the count if "Yes" is selected for both questions
        let points = 0;
        if (goalFollowed.value === "yes" && badHabit.value === "yes") {
            points = 1; // Example: award 1 point for successful check-in
        }

        // Store journal (or handle as needed)
        console.log("Journal Entry:", journal);

        // Hide the modal and display a message (you can handle this as needed)
        modal.style.display = "none";
        alert("Check-in complete. You gained " + points + " points!");
    } else {
        alert("Please answer all questions.");
    }
});
