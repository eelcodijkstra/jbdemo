(function() {
  function allowDrop(ev) {
    ev.preventDefault();
  }

  function drag(ev) {
    ev.dataTransfer.setData('text', ev.target.id);
    console.log('drag source: ' + ev.target.id);
  }

  function drop(ev) {
    ev.preventDefault();
    const data = ev.dataTransfer.getData('text');
    const elt = document.getElementById(data);
    let target = ev.target;
    while (target.tagName != 'DIV') {
      target = target.parentNode;
    }
    target.appendChild(elt);
  }

  function checkDnd(ev) {
    const dnd = ev.target.parentNode;
    const items = dnd.querySelectorAll('.dndsourceitem');
    for (const item of items) {
      if (
        (item.parentNode.dataset != null) &&
        (item.dataset.value == item.parentNode.dataset.value)
      ) {
        item.style.backgroundColor = 'yellowGreen';
      } else {
        item.style.backgroundColor = 'salmon';
      }
    }
  }

  function resetDnd(ev) {
    const dnd = ev.target.parentNode;
    const items = dnd.querySelectorAll('.dndsourceitem');
    const source = dnd.querySelector('.dndsourcelist');
    for (const item of items) {
      if (item.parentNode != source) {
        source.appendChild(item);
      }
      item.style.backgroundColor = '';
    }
  }

  function findDragndrops() {
    const sources = document.getElementsByClassName('dndsourceitem');
    for (const item of sources) {
      item.ondragstart = drag;
    }
    const targets = document.getElementsByClassName('dndtargetitem');
    for (const item of targets) {
      item.ondrop = drop;
      item.ondragover = allowDrop;
    }
    const checkbuttons = document.getElementsByClassName('dndcheckbutton');
    for (const button of checkbuttons) {
      button.onclick = checkDnd;
    }
    const resetbuttons = document.getElementsByClassName('dndresetbutton');
    for (const button of resetbuttons) {
      button.onclick = resetDnd;
    }
  }

  document.addEventListener('DOMContentLoaded', function(event) {
    findDragndrops();
  });
})();
