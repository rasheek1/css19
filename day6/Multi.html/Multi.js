function Multiples(Mult,m,n)
{
    let absX = Math.abs(n);
    let index = 1;
    while (index <= absX){
        Mult.push(index *m);
        index = index + 1
    }
}