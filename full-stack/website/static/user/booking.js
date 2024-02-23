// Typing effect in the contacts section (footer)

let i = 0


let typingEffect = function () {

    let text = 'Prenota un tavolo'
    let speed = 130 // Velocity in entering characters

    if (i < text.length) {
        document.querySelector(".typing").innerHTML += text.charAt(i)
        i++;
        setTimeout(typingEffect, speed)
    }
}

typingEffect()

// Handling the reservations

const months = {
    1: 'Gennaio',
    2: 'Febbraio',
    3: 'Marzo',
    4: 'Aprile',
    5: 'Maggio',
    6: 'Giugno',
    7: 'Luglio',
    8: 'Agosto',
    9: 'Settembre',
    10: 'Ottobre',
    11: 'Novembre',
    12: 'Dicembre'
}

let weekDays = new Array(
    'DOM',
    'LUN',
    'MAR',
    'MER',
    'GIO',
    'VEN',
    'SAB',
)

// Read the 21 days available to book a reservation

let availableMonths = []

const calendarContainer = document.querySelector('.calendar')

let readAvailableDays = function () {
    let monthKeys = []

    fetch('/user/available_days')
    .then(res => res.json())
    .then(obj => {
        for (const [key, value] of Object.entries(obj.data)) {

            monthKeys.push(key)
            
            // Create Month section for each month
            let monthBox = document.createElement('div')
            monthBox.className = 'month'
            calendarContainer.appendChild(monthBox)

            // Create month name div for each month
            let monthNameDiv = document.createElement('div')
            monthNameDiv.className = 'month-name'
            monthNameDiv.textContent = months[key]
            monthBox.append(monthNameDiv)

            // Create calendar container for each month
            let monthCalendar = document.createElement('div')
            monthCalendar.className = 'month-calendar'
            monthBox.appendChild(monthCalendar)

            // Adding the week days names for each month (Lun, mar, mer ecc...)
            let weekDaysBox = document.createElement('div')
            weekDaysBox.className = 'week-days'
            monthCalendar.appendChild(weekDaysBox)

            weekDays.forEach(day => {
                let weekDayBox = document.createElement('div')
                weekDayBox.className = 'week-day'
                weekDayBox.textContent = day
                weekDaysBox.appendChild(weekDayBox)
            })

            // Create month days box for dates boxes (1, 2, 3, 4 ecc...
            let monthDaysBox = document.createElement('div')
            monthDaysBox.className = 'month-days'
            monthCalendar.appendChild(monthDaysBox)

            value.forEach((day, index) => {
                if (index === 0) {
                    if (key === monthKeys[0]) {
                        let toDayFormat = new Date(`${day.split('-')[2]}-${day.split('-')[1]}-${day.split('-')[0]}`)
                        let dayNumber = toDayFormat.getDay()
                        console.log(dayNumber)

                        for (let i=dayNumber; i>0; i--) {
                            let monthDayBox = document.createElement('div')
                            monthDayBox.className = 'month-day disabled'
                            monthDayBox.textContent = parseInt(day.split('-')[0]) - i
                            monthDaysBox.appendChild(monthDayBox)
                        }
                    }
                }
    
                let date = day.split('-')[0]
                let monthDayBox = document.createElement('div')
                monthDayBox.className = 'month-day'
                monthDayBox.textContent = date
                monthDayBox.setAttribute('data-date', `${day}`)
                monthDaysBox.appendChild(monthDayBox)
            })
        }
    })
    .then(res => {
        let allDays = document.querySelectorAll('.month-day')
        allDays.forEach(day => {
            day.addEventListener("click", () => {
                let flipInner = document.querySelector('.flip')
                flipInner.style.transform = 'rotateY(180deg)' 
            })
        })
    })
}
readAvailableDays()

