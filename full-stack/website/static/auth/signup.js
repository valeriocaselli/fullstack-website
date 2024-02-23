// Typing effect

const animated = document.querySelector(".typing")

let i = 0

let typingEffect = function () {
    let text = 'Registrati'
    let speed = 130
    let pause = 3000

    if (i<text.length) {
        animated.innerHTML += text.charAt(i);
        i++;
        setTimeout(typingEffect, speed)
    }

    // Repeating the effect endlessly
    else if (i===text.length) {
        setTimeout(() => {
            i = 0;
            animated.textContent = ''
            typingEffect()
        }, 3000)
    }
}

typingEffect()

// Handling click events on eyye icon to show the password

const eyeIcons = document.querySelectorAll(".show-password")
const inputs = document.querySelectorAll(".password-input")

eyeIcons.forEach((icon, index) => {
    icon.addEventListener("click", () => {
        // console.log(inputs[index].getAttribute("type"))
        let type = inputs[index].getAttribute('type') === 'password' ? 'text' : 'password'
        inputs[index].setAttribute('type', type)
        icon.className = type === 'text' ? 'fa-solid fa-eye-slash' : 'fa-solid fa-eye'
    })
})