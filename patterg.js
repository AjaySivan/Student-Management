let row = 5
let col = 5
for(r=1;r<=row;r++){
    let line =""
    for(c=1;c<=col;c++){
        if(r==1 ||c==1 || r == 3 && c>2 || r>2 && c==5 || r==5){
            line+="*"
        }
        else{
            line+=" "

        }
    }
    console.log(line)
}