  function mchandler(event) {
      console.log("target: " + event.target.id);
      var myform = event.target;
      var correct = myform.dataset.correct;
      var feedbackline = myform.getElementsByClassName("feedback")[0];
      if (myform.answer.value == correct) {
          feedbackline.innerHTML = '<i class="fas fa-check"> </i>';
      } else {
          feedbackline.innerHTML = '<i class="fas fa-times"> </i>';
      }
      var feedbacklist = myform.getElementsByTagName("ul")[0];
      feedbacklist.hidden = false;
      var feedbacks = feedbacklist.getElementsByTagName("li");
      for (i = 0; i < feedbacks.length; i++) {
          if (feedbacks[i].dataset.value == myform.answer.value) {
              feedbacks[i].hidden = false;
              if (myform.answer.value == correct) {
                feedbacklist.style.backgroundColor = "yellowgreen";
              } else {
                feedbacklist.style.backgroundColor = "salmon";  
              }
         } else {
              feedbacks[i].hidden = true;            
         }
      }
      return false; // no further action  
  }

  function mcresethandler(event) {
      console.log("target: " + event.target.id);
      console.log("form: " + event.target.form.id);
      var myform = event.target.form;
      var feedbacklist = myform.getElementsByTagName("ul")[0];
      feedbacklist.hidden = true;
      var feedbacks = feedbacklist.getElementsByTagName("li");
      for (i = 0; i < feedbacks.length; i++) {
          feedbacks[i].hidden = true;
      }      
      var elements = myform.elements;
      for (i = 0; i < elements.length; i++) {
          if (elements[i].nodeName == "INPUT") {
              elements[i].checked = false;
          }
      }
      return false; // no further action
  }
  
  function find_mchoices() {
      var forms = document.getElementsByClassName("mchoice");
      for (i = 0; i < forms.length; i++) {
          console.log("mchoice nr: " + i);
          forms[i].onsubmit = mchandler;
          resetbutton = forms[i].querySelector('button[type=reset]');
          resetbutton.onclick = mcresethandler;
      }
  }

  document.addEventListener('DOMContentLoaded', function(event) {
      find_mchoices();
  })
