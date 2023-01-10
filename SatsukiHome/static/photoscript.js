let photo = ".jpg";
var bltx = 1;
var exx = 1;

function left(x,n,id) {
    if (x==1) {
        let photoNew = n + photo;
        document.getElementById(id).src="/static/images/"+id+"/"+photoNew;
        return n;
    } else {
        x = x-1;
        let photoNew = x + photo;
        document.getElementById(id).src="/static/images/"+id+"/"+photoNew;
        return x;
    }
}

function right(x,n,id) {
    if (x==n) {
        let photoNew = 1 + photo;
        document.getElementById(id).src="/static/images/"+id+"/"+photoNew;
        return 1;
    } else {
        x = x+1;
        let photoNew = x + photo;
        document.getElementById(id).src="/static/images/"+id+"/"+photoNew;
        return x;
    }
}

function EXRight() {
    exx=right(exx,6,'EX');
}

setInterval(EXRight,5000);