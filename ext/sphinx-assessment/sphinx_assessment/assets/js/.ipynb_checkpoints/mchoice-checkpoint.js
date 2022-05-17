function mcHandler(event) {
    console.log('target: ' + event.target.id);
    const myform = event.target;
    const correct = myform.dataset.correct;
    const feedbackline = myform.getElementsByClassName('feedback')[0];
    if (myform.answer.value == correct) {
        feedbackline.innerHTML = '<i class="fas fa-check"> </i>';
    } else {
        feedbackline.innerHTML = '<i class="fas fa-times"> </i>';
    }
    const feedbacklist = myform.getElementsByTagName('ul')[0];
    feedbacklist.hidden = false;
    const feedbacks = feedbacklist.getElementsByTagName('li');
    for (let i = 0; i < feedbacks.length; i++) {
        if (feedbacks[i].dataset.value == myform.answer.value) {
            feedbacks[i].hidden = false;
            if (myform.answer.value == correct) {
                feedbacklist.style.backgroundColor = 'yellowgreen';
            } else {
                feedbacklist.style.backgroundColor = 'salmon';
            }
        } else {
            feedbacks[i].hidden = true;
        }
    }
    return false; // no further action
}

function mcResetHandler(event) {
    console.log('target: ' + event.target.id);
    console.log('form: ' + event.target.form.id);
    const myform = event.target.form;
    const feedbacklist = myform.getElementsByTagName('ul')[0];
    feedbacklist.hidden = true;
    const feedbacks = feedbacklist.getElementsByTagName('li');
    for (let i = 0; i < feedbacks.length; i++) {
        feedbacks[i].hidden = true;
    }
    const elements = myform.elements;
    for (let i = 0; i < elements.length; i++) {
        if (elements[i].nodeName == 'INPUT') {
            elements[i].checked = false;
        }
    }
    return false; // no further action
}

function findMchoices() {
    const forms = document.getElementsByClassName('mchoice');
    for (let i = 0; i < forms.length; i++) {
        console.log('mchoice nr: ' + i);
        forms[i].onsubmit = mcHandler;
        resetbutton = forms[i].querySelector('button[type=reset]');
        resetbutton.onclick = mcResetHandler;
    }
}

document.addEventListener('DOMContentLoaded', function(event) {
    findMchoices();
});
