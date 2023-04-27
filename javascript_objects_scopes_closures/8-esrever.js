#!/usr/bin/node
function esrever(list){
    let a = [];
    let k = list.length -1;
    for (let i = 0;i < list.length; i++){
        a[i]= list[k];
        k-=1;
    }
    return a
}
exports.esrever = esrever;