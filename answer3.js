function cal(n){
    let cur=0;
    for (i=2;i<=n;i++){
        cur+=1/(i*(i-1))
    }
    if(n<2){
        throw new console.error("invalid Input");
    }
    return cur;
}
