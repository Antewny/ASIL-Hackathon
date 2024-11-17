const currentDate = new Date();

function getWeekRange(date) {
    const day = date.getDay(),
          diff = date.getDate() - day + (day == 0 ? -6 : 0); // Adjust when day is sunday
    const startDate = new Date(date.setDate(diff));
    const endDate = new Date(date.setDate(diff + 6));
    return [startDate, endDate];
}

// Update the mini calendar and weekly view
function updateCalendar() {
    const monthNames = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
    const month = currentDate.getMonth();
    const year = currentDate.getFullYear();

    document.getElementById('calendar-month').textContent = monthNames[month];
    document.getElementById('calendar-year').textContent = year;

    const firstDayOfMonth = new Date(year, month, 1);
    const lastDayOfMonth = new Date(year, month + 1, 0);
    const daysInMonth = lastDayOfMonth.getDate();

    const calendarDays = document.getElementById('calendar-days');
    calendarDays.innerHTML = ''; 

    for (let i = 0; i < firstDayOfMonth.getDay(); i++) {
        const emptyDay = document.createElement('div');
        emptyDay.className = 'calendar__day';
        calendarDays.appendChild(emptyDay);
    }

    for (let i = 1; i <= daysInMonth; i++) {
        const dayElement = document.createElement('div');
        dayElement.className = 'calendar__day';
        dayElement.textContent = i;
        dayElement.addEventListener('click', () => highlightWeek(i));
        calendarDays.appendChild(dayElement);
    }
    highlightCurrentWeek();
}

function highlightCurrentWeek() {
    const [startDate, endDate] = getWeekRange(currentDate);
    const weekDays = document.querySelectorAll('.calendar__day');

    weekDays.forEach(day => {
        const dayNumber = parseInt(day.textContent, 10);
        if (dayNumber >= startDate.getDate() && dayNumber <= endDate.getDate()) {
            day.style.backgroundColor = '#007BFF';
            day.style.color = 'white';
        }
    });
    updateWeekView(startDate);
}

function updateWeekView(startDate) {
    const weekDays = document.querySelectorAll('.day');
    const weekRange = getWeekRange(startDate);

    weekDays.forEach((dayElement, index) => {
        const currentDate = new Date(weekRange[0]);
        currentDate.setDate(currentDate.getDate() + index);
        dayElement.textContent = currentDate.toLocaleString('en-us', { weekday: 'long' });
    });
}

function highlightWeek(dayNumber) {
    const selectedDate = new Date(currentDate.getFullYear(), currentDate.getMonth(), dayNumber);
    const [startDate, endDate] = getWeekRange(selectedDate);
    updateWeekView(startDate);
}

window.onload = updateCalendar;