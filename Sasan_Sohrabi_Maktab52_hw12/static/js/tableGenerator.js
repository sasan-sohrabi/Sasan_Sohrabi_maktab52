function tableGenerator(data) {

    let x = document.getElementById("order-table-body");
    for (var key in data) {
        let tr = document.createElement('tr');
        let td0 = document.createElement('td');
        let td1 = document.createElement('td');
        let td2 = document.createElement('td');
        let td3 = document.createElement('td');
        let td4 = document.createElement('td');
        let td5 = document.createElement('td');
        td0.innerText = data[key]['id'];
        console.log(data[key]['id'])
        td1.innerText = data[key]['name'];
        td2.innerText = data[key]['price'];
        td3.innerText = data[key]['table'];
        td4.innerText = data[key]['status'];
        td5.innerText = data[key]['date'];
        td0 = tr.appendChild(td0);
        td1 = tr.appendChild(td1);
        td2 = tr.appendChild(td2);
        td3 = tr.appendChild(td3);
        td4 = tr.appendChild(td4);
        td5 = tr.appendChild(td5);
        tr = x.appendChild(tr);
    }
}

function productgenerator(data) {
    console.log(data)
    let y = document.getElementById("product-table-body");
    for (var key in data) {
        let tr = document.createElement('tr');
        tr.style.marginTop = "2px";
        let td0 = document.createElement('td');
        td0.style.width = "60px";
        let div1 = document.createElement('div');
        div1.classList.add("imgbx10");
        let img1 = document.createElement('img');
        img1.src = "../static/images/coffee.jpg";
        img1 = div1.appendChild(img1);
        div1 = td0.appendChild(div1);
        let td1 = document.createElement('td');
        let h4 = document.createElement('h4');
        h4.innerHTML = data[key]['name'] + "<br><span>" + data[key]['category'] +"</span>";
        h4 = td1.appendChild(h4);
        td0 =tr.appendChild(td0);
        td1=tr.appendChild(td1);
        tr = y.appendChild(tr);
    }

}