// Typing effect

const animated = document.querySelector(".typing")

let i = 0

let typingEffect = function () {
    let text = 'Accedi'
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