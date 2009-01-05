function delayContinue(nSeconds)
{
    nSeconds = 0;
    hideLr("loading");
    setTimeout("showContinue()", nSeconds * 1000);
}

function showContinue()
{
    var elm;

    elm = document.getElementById("pleaseWait");
    if (elm) {
        elm.style.display = "none";
    }

    elm = document.getElementById("continueButton");
    if (elm) {
        elm.style.visibility = "visible";
    }
    
    setFocus();
}

function hideLr(id)
{
    var elm;
    elm = document.getElementById(id);
    if (elm) {
        elm.style.display = "none";
    }
}

function setFocus() {
    if (document.theform != undefined) {
        document.theform.guess.focus();
    }
    else {
        elm = document.getElementById("continueButton");
        if (elm) {
            elm.focus();
        }
    }
}