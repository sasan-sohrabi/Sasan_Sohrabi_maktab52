function menuGenerator(ntable) {
    console.log(ntable)
    for( var key in ntable)  {
        let cardGenerator = document.getElementById('cardGenerator')
        console.log(key);
        let divCol = document.createElement('div')
        divCol.classList.add("col-12")
        divCol.classList.add("col-sm-6")
        divCol.classList.add("col-md-6")
        divCol.classList.add("col-lg-4")
        divCol.classList.add("filter")
        divCol.classList.add("text-center")
        // divCol.classList.add("col-12")
        divCol.classList.add("mt-5")
        // divCol.classList.add("drink")
        divCol = cardGenerator.appendChild(divCol)

        let divCard = document.createElement('div')
        divCard.classList.add("card")
        // divCard.style.borderRadius("50px")
        // divCard.classList.add("bg-nav")
        divCard.classList.add("h-100")
        divCard.classList.add("text-center")
        divCard = divCol.appendChild(divCard)

        let img = document.createElement('img')
        img.classList.add("card-img")
        img.src = "static/images/ATbrnyMpc.png"
        img.style.width = "200px";
        img.style.height = "100px";
        img.style.marginTop="10%";
        img = divCard.appendChild(img);

        let a1 = document.createElement('a')
        let a2 = document.createElement('a')
        let a3 = document.createElement('a')
        let a4 = document.createElement('a')
        a2.innerText = "Table  :  " + ntable[key]["number"] ;
        a2.style.borderStyle="solid";
        a2.style.borderRadius="10%";
        a2.style.padding="0.5%";
        a2.style.margin="2%";
        if(ntable[key]["situation"]=="full"){

            a3.style.backgroundColor= "red";
        }
        else{
            a3.classList.add('bg-nav');
        }
        a2.classList.add('bg-nav');
        a3.style.borderStyle="solid";
        a3.style.borderRadius="10%";
        a3.style.padding="2%";
        // a3.style.marginTop="100px";
        a4.style.borderStyle="solid";
        a4.style.borderRadius="10%";
        a4.style.padding="2%";
        a4.style.margin="2%";
        a4.classList.add('bg-nav');
        a3.innerText = "situation  :  " + ntable[key]["situation"] ;
        a4.innerText = "order_number  :  " + ntable[key]["order_number"] ;
        a3.style.borderColor="black";
        a4.style.borderColor="black";
        a2.style.borderColor="black";
        a2.style.color="black";
        a3.style.color="black";
        a4.style.color="black";
        let br1 = document.createElement('br')
        let br2 = document.createElement('br')
        let br3 = document.createElement('br')
        let br4 = document.createElement('br')
        let br5 = document.createElement('br')
        let br6 = document.createElement('br')
        let br7 = document.createElement('br')
        let br8 = document.createElement('br')
        a1 = divCol.appendChild(a1);
        br1 = divCol.appendChild(br1);
        a2 = divCol.appendChild(a2);
        br2 = divCol.appendChild(br2);
        br5 = divCol.appendChild(br5);
        a3 = divCol.appendChild(a3);
        br3 = divCol.appendChild(br3);
        br6 = divCol.appendChild(br6);
        a4= divCol.appendChild(a4);
        br4 = divCol.appendChild(br4);
        br7 = divCol.appendChild(br7);
        // a1 = divCard.appendChild(a1);
        // br1 = divCard.appendChild(br1);
        // a2 = divCard.appendChild(a2);
        // br2 = divCard.appendChild(br2);
        // a3 = divCard.appendChild(a3);
        // br3 = divCard.appendChild(br3);
        // a4= divCard.appendChild(a4);
        // br4 = divCard.appendChild(br4);




    }
}



