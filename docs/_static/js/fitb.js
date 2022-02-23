function fitbcheck (evt, item) {
    console.log("check fitb");
    var answers = item.getElementsByClassName("fitbanswer");
    for (const answer of answers) {
        var type = answer.dataset.type;
        var answer1 = answer.dataset.answer;
        var answer2 = answer.dataset.answer2;
        var input = answer.value;
        console.log("Check: " + type + " - " + answer1 + " - " + answer2 + " > " + input);
        var ok = false;
        if (type == 'text') {
            ok = answer.value == answer.dataset.answer;
        } else if (type == 'range') {
            var num = Number(answer.value);
            var min = Number(answer.dataset.answer);
            var max = Number(answer.dataset.answer2);
            ok = (min <= num) && (num <= max);
        } else if (type == 'regexp') {
            var regexp = new RegExp(answer.dataset.answer);
            ok = regexp.test(answer.value);
        }
        if (ok) {
            answer.style.backgroundColor = 'lightGreen';
        } else {
            answer.style.backgroundColor = 'salmon';
        }
    }
}


function find_fillintheblanks() {
    var fitbs = document.getElementsByClassName("fitb");
    console.log("fitb's found: " + fitbs.length.toString());
    
    console.log("fitbs is array? " + Array.isArray(fitbs));
    
    for (const item of fitbs) {
        console.log("in forEach");
        var checkbutton = item.querySelector(".fitbcheckbutton");
        checkbutton.onclick = function (evt) {fitbcheck(evt, item);};
    }
}

document.addEventListener('DOMContentLoaded', function(event) {
    find_fillintheblanks();
    console.log("init fillintheblank")
})