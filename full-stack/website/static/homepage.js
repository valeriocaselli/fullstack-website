// Typing effect in the contacts section (footer)

let i = 0


let typingEffect = function () {

    let text = 'Lavora con noi'
    let speed = 130 // Velocity in entering characters

    if (i < text.length) {
        document.getElementById("typing-effect").innerHTML += text.charAt(i)
        i++;
        setTimeout(typingEffect, speed)
    }
}



// Animation for scrolling

// Animation in reviews container (first section in homepage)

const reviewsBoxes = document.querySelectorAll('.review')

reviewsBoxes.forEach((box, index) => {
    // alternate the animations: from left to right and the opposite
    if (index == 0 || index == 2) {
        box.classList.add('to-left')
    } else {
        box.classList.add('to-right')
    }
})

let reviewScrolling = function (block, delay) {
    setTimeout(() => {
        block.classList.add('scrolled')
    }, delay)
}

const elementsToAnimate = document.querySelectorAll(".animated")

const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
        if (entry.isIntersecting) {
            entry.target.classList.add("scrolling")

            if (entry.target.classList.contains("typing")) {
                // Restart the typing effect
                i = 0;
                document.getElementById("typing-effect").textContent = ""
                typingEffect()
            }

            if (entry.target.classList.contains("scrolling-rev")) {
                // Review box animations
                reviewScrolling(reviewsBoxes[0], 300)
                reviewScrolling(reviewsBoxes[1], 600)
                reviewScrolling(reviewsBoxes[2], 900)
                reviewScrolling(reviewsBoxes[3], 1200)
            }

            if (entry.target.classList.contains('staff-rev')) {
                let animatedOneBoxes = document.querySelectorAll('.animation-one')

                animatedOneBoxes.forEach(box => {
                    box.classList.add('scrolled')
                })

                let animatedTwoBoxes = document.querySelectorAll('.animation-two')

                setTimeout(() => {
                    animatedTwoBoxes.forEach(box => {
                    box.classList.add('scrolled')
                })
                }, 500)

                let animatedThreeBoxesUp = document.querySelectorAll('.animation-three-up')
                let animatedThreeBoxesDown = document.querySelectorAll('.animation-three-down')

                let animatedThreeBoxes = [...animatedThreeBoxesUp, ...animatedThreeBoxesDown]

                setTimeout(() => {
                    animatedThreeBoxes.forEach(box => {
                        box.classList.add('scrolled')
                    })
                }, 1000)

                let animatedFourBoxesUp = document.querySelectorAll('.animation-four-up')
                let animatedFourBoxesDown = document.querySelectorAll('.animation-four-down')

                let animatedFourBoxes = [...animatedFourBoxesUp, ...animatedFourBoxesDown]

                setTimeout(() => {
                    animatedFourBoxes.forEach(box => {
                        box.classList.add('scrolled')
                    })
                }, 1500)
            }
        }
        else {
            entry.target.classList.remove("scrolling")

            if (entry.target.classList.contains("scrolling-rev")) {
                reviewsBoxes.forEach(box => {
                    box.classList.remove('scrolled')
                })
            }

            if (entry.target.classList.contains("staff-rev")) {
                let allStaffCards = document.querySelectorAll('.staff-card')

                allStaffCards.forEach(card => [
                    card.classList.remove('scrolled')
                ])
            }

        }

    })
}, {threshold: 0.5})

elementsToAnimate.forEach(element => {
    observer.observe(element)
})

// ScrollSpy Animation

const sections = document.querySelectorAll("section")
const navLinks = document.querySelectorAll(".navbar-items .item")


navLinks.forEach((link, index) => {
    link.addEventListener("click", () => {
        let sectionHeight = sections[0].offsetHeight
        let navbarHeight = document.querySelector(".navbar").offsetHeight
        window.scroll(0, index*(sectionHeight+navbarHeight))
    })
})

// Button to form for candidates

const toWorkFormBtn = document.getElementById("to-work-form")
toWorkFormBtn.addEventListener("click", () => {
    let sectionHeight = sections[0].offsetHeight
    window.scroll(0, 3*(sectionHeight))
})


