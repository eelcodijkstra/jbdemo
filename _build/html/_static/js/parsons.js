
function parsonsAllowDrop(ev) {
    ev.preventDefault();
}

function parsonsDrag(ev) {
    ev.dataTransfer.setData("text", ev.target.id);
    console.log("drag: " + ev.target.id);
}

function parsonsPositionItems(target) {
  var itemList = target.getElementsByClassName("parsons-item");
  var pos = 1;
  for (let item of itemList) {
    item.style.gridRowStart = pos;
    pos += 1;
  }
}

function parsonsDrop(ev) {
    ev.preventDefault();
    console.log("initial target: " + ev.target.id);
    var rect = ev.target.getBoundingClientRect();
    var x = ev.clientX - Math.round(rect.left); //x position within the element.
    var y = ev.clientY - Math.round(rect.top);  //y position within the element.
    console.log("drop-X: " + x + " ; Y: " + y + ".");
    var data = ev.dataTransfer.getData("text");

    var target = ev.target,
    item = document.getElementById(data);
    if (target.classList.contains("parsons-source")) {
        var parent = item.parentElement;
        target.appendChild(item);     // move back to source container
        parsonsPositionItems(parent); // rearrange target container
        return;
    }
    if (target.classList.contains("parsons-column1")) {
        item.style.gridColumnStart = 1;
        item.style.gridColumnEnd = 6;
        if (item.parentElement.classList.contains("parsons-target")) {
            console.log("move left");
            return;
        }
    }
    if (target.classList.contains("parsons-column2")) {
        item.style.gridColumnStart = 2;
        item.style.gridColumnEnd = 6;
        if (item.parentElement.classList.contains("parsons-target")) {
            console.log("move left");
            return;
        }        
    }
    if (target.classList.contains("parsons-column3")) {
        item.style.gridColumnStart = 3;
        item.style.gridColumnEnd = 6;
        if (item.parentElement.classList.contains("parsons-target")) {
            console.log("move left");
            return;
        }        
    }    
    var insertItem = null;
    if (target.classList.contains("parsons-item") && target.parentElement.classList.contains("parsons-target")) {
        insertItem = target;
        if (insertItem === item) {
            item.style.gridColumnStart = parseInt(item.style.gridColumnStart) + 1;
            console.log("move right");
        } else {
            item.style.gridColumnStart = insertItem.style.gridColumnStart;
            item.style.gridColumnEnd = 6;
        }
    }
    while (!target.classList.contains("parsons-target") && !target.classList.contains("parsons-source")) {
        target = target.parentElement;
    }
    // console.log("drop target: " + target.id);
    var dndItemCount = target.dndItemCount || 0;
    dndItemCount += 1;
    target.dndItemCount = dndItemCount;
    item.style.gridRowStart = dndItemCount;
    if (insertItem !== null) {
        target.insertBefore(item, insertItem);
    } else {
        target.appendChild(item);
    }
    item.style.zIndex = 10;
    parsonsPositionItems(target);
  
}

function parsonsCheckHandler(evt) {
    console.log("Parsons: check");
    // find surrounding parsons admonition
    var parsons = evt.target.closest(".parsons");
    var targets = parsons.getElementsByClassName("parsons-target");
    console.log("target found? - " + targets.length);
    var target = targets[0];
    for (let item of target.children) {
        console.log("next item");
        if (item.classList.contains("parsons-item")) {
            if ((item.style.gridRowStart == item.dataset.value) &&
                (item.style.gridColumnStart - 1 == item.dataset.indent)) {
                item.style.backgroundColor = "yellowgreen";
            } else {
                item.style.backgroundColor = "salmon";
            }
        }
    }
    // find parsons-target in this admonition
    // check all elements in this target:
    // if parsons-item: check "value" == item.style.gridRowStart and
    // "indent" == item.style.gridColumnStart - 1
    
}

function find_parsons() {
    var sources = document.getElementsByClassName("parsons-item");
    for (const item of sources) {
        item.ondragstart = parsonsDrag;
    }    
    var targets = document.getElementsByClassName("parsons-target");
    for (const item of targets) {    
        item.ondrop = parsonsDrop;
        item.ondragover = parsonsAllowDrop;        
    }
    var targets = document.getElementsByClassName("parsons-source");
    for (const item of targets) {    
        item.ondrop = parsonsDrop;
        item.ondragover = parsonsAllowDrop;        
    } 
    var buttons = document.getElementsByClassName("parsons-checkbutton");
    for (const button of buttons) {
        button.onclick = parsonsCheckHandler;
    }
}

  document.addEventListener('DOMContentLoaded', function(event) {
      find_parsons();
  })