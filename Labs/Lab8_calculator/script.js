function calculate(form) {
    form.display.value = eval(form.display.value);
    if(form.display.value == Infinity){
        form.display.value = 'Syntax Error';
    }
}
function getSqrt(form){
    form.display.value = Math.sqrt(form.display.value);
}
function getPercentage(form){
    form.display.value = form.display.value / 100;
}
function getSin(form){
    form.display.value = Math.sin(form.display.value);
}
function getCos(form){
    form.display.value = Math.cos(form.display.value);
}
function getTan(form){
    form.display.value = Math.tan(form.display.value);
}
function getLog10(form){
    form.display.value = Math.log10(form.display.value);
}
function getLog2(form){
    form.display.value = Math.log2(form.display.value);
}
function getExp(form){
    form.display.value = Math.exp(form.display.value);
}