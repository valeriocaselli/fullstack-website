// Define the max lenght in characters for textarea of the review description

const textarea = document.querySelector('.description-content')
textarea.setAttribute('maxLength', '100')

const lettersCounter = document.querySelector('.letters-counter')

textarea.addEventListener('keyup', () => {
    lettersCounter.textContent = ''
    lettersCounter.innerHTML = `${textarea.value.length}/100`
})

// Reset textarea content on reloading page and submitting form

window.onbeforeunload = function () {
    textarea.innerHTML = ''
}

const submitBtn = document.querySelector('.button')
submitBtn.addEventListener('click', () => {
    textarea.innerHTML = ''
    console.log('Ciao')
})
