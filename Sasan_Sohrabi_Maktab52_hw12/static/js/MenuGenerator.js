function menuGenerator(data) {
    console.log("Im Here")
    for (let drink in data) {
        let cardGenerator = document.getElementById('cardGenerator')

        let divCol = document.createElement('div')
        divCol.classList.add("col-12")
        divCol.classList.add("col-sm-6")
        divCol.classList.add("col-md-6")
        divCol.classList.add("col-lg-4")
        divCol.classList.add("filter")
        divCol.classList.add("col-12")
        divCol.style.marginTop="20px";
        divCol.style.borderRadius= "30%";
        divCol.classList.add(data[drink]["category"])
        divCol = cardGenerator.appendChild(divCol)

        let divCard = document.createElement('div')
        divCard.classList.add("card")
        divCard.classList.add("bg-nav")
        divCard.classList.add("h-100")
        divCard.style.padding = "5%"
        divCard = divCol.appendChild(divCard)

        let img = document.createElement('img')
        img.classList.add("card-img")
        img.style.borderRadius="80%"
        img.src = "/static/images/" + data[drink]['img']

        img = divCard.appendChild(img)

        let divCarBody = document.createElement('div')
        divCarBody.classList.add("card-body")
        divCarBody = divCard.appendChild(divCarBody)

        let title_h4 = document.createElement('h4')
        title_h4.classList.add("card-title")
        title_h4 = divCarBody.appendChild(title_h4)

        let spanTitle = document.createElement('span')
        spanTitle.classList.add("shop-item-title")
        spanTitle.innerText = data[drink]["name"]
        spanTitle = title_h4.appendChild(spanTitle)

        let idData = document.createElement('span')
        idData.classList.add("data-id")
        idData.setAttribute("type", "hidden")
        idData.innerText = drink
        idData = divCarBody.appendChild(idData)

        let divBuy = document.createElement('div')
        divBuy.classList.add("buy")
        divBuy.classList.add("d-flex")
        divBuy.classList.add("justify-content-between")
        divBuy.classList.add("align-items-center")
        divBuy = divCarBody.appendChild(divBuy)

        let divPrice = document.createElement('div')
        divPrice.classList.add("price")
        divPrice.classList.add("text-success")
        divPrice.classList.add("text-center")
        divPrice = divBuy.appendChild(divPrice)

        let spanPrice = document.createElement('span')
        spanPrice.classList.add("shop-item-price")
        spanPrice.innerText = data[drink]["price"] + "$"
        spanPrice = divPrice.appendChild(spanPrice)

        let btnCart = document.createElement('btn')
        btnCart.classList.add("btn")
        btnCart.style.backgroundColor ="rgba(80, 61, 43, 0.68)"
        btnCart.classList.add("HoverClass1")
        btnCart.classList.add("btn-large")
        btnCart.classList.add("shop-item-button")
        btnCart.setAttribute('aria-hidden', 'true')
        btnCart.setAttribute('type', 'button')
        btnCart.innerText = "Add to cart"
        let i = document.createElement('i')
        i.classList.add("fa");
        i.classList.add("fa-shopping-cart");
        i = btnCart.appendChild(i);
        btnCart = divBuy.appendChild(btnCart);
    }


    var removeCartItemButtons = document.getElementsByClassName('btn-danger')
    for (var i = 0; i < removeCartItemButtons.length; i++) {
        var button = removeCartItemButtons[i]
        button.addEventListener('click', removeCartItem)
    }

        var quantityInputs = document.getElementsByClassName('cart-quantity-input')
        for (var i = 0; i < quantityInputs.length; i++) {
            var input = quantityInputs[i]
            input.addEventListener('change', quantityChanged)
        }

        var addToCartButtons = document.getElementsByClassName('shop-item-button')
        for (var i = 0; i < addToCartButtons.length; i++) {
            var button = addToCartButtons[i]
            button.addEventListener('click', addToCartClicked)
        }

        document.getElementById('btn-purchase').addEventListener('click', purchaseClicked)


        function purchaseClicked() {
            alert('Thank you for your purchase')
            var cartItems = document.getElementsByClassName('cart-items')[0]
            while (cartItems.hasChildNodes()) {
                cartItems.removeChild(cartItems.firstChild)
            }
            updateCartTotal()
        }

        function removeCartItem(event) {
            var buttonClicked = event.target
            buttonClicked.parentElement.parentElement.remove()
            updateCartTotal()
        }

        function quantityChanged(event) {
            var input = event.target
            if (isNaN(input.value) || input.value <= 0) {
                input.value = 1
            }
            updateCartTotal()
        }

        function addToCartClicked(event) {
            var button = event.target
            var shopItem = button.parentElement.parentElement
            var title = shopItem.getElementsByClassName('shop-item-title')[0].innerText
            var price = shopItem.getElementsByClassName('shop-item-price')[0].innerText
            var id = shopItem.getElementsByClassName('data-id')[0].innerText
            addItemToCart(title, price, id)
            updateCartTotal()
        }

        function addItemToCart(title, price, id) {
            var cartRow = document.createElement('div')
            cartRow.classList.add('cart-row')
            var cartItems = document.getElementsByClassName('cart-items')[0]
            var cartItemNames = cartItems.getElementsByClassName('cart-item-title')
            for (var i = 0; i < cartItemNames.length; i++) {
                if (cartItemNames[i].innerText == title) {
                    alert('This item is already added to the cart')
                    return
                }
            }
            var cartRowContents = `
        <div class="cart-item cart-column">
            <span class="cart-item-title title_1">${title}</span>
        </div>
        <span class="cart-price cart-column price_1">${price}</span>
        <div class="cart-quantity cart-column">
            <input class="cart-quantity-input" type="number" value="1" dataid-quantity=${id}>
            <button class="btn btn-danger" type="button">REMOVE</button>
        </div>`
            cartRow.innerHTML = cartRowContents
            cartItems.append(cartRow)
            cartRow.getElementsByClassName('btn-danger')[0].addEventListener('click', removeCartItem)
            cartRow.getElementsByClassName('cart-quantity-input')[0].addEventListener('change', quantityChanged)
        }

        function updateCartTotal() {
            var cartItemContainer = document.getElementsByClassName('cart-items')[0]
            var cartRows = cartItemContainer.getElementsByClassName('cart-row')
            var total = 0
            for (var i = 0; i < cartRows.length; i++) {
                var cartRow = cartRows[i]
                var priceElement = cartRow.getElementsByClassName('cart-price')[0]
                var quantityElement = cartRow.getElementsByClassName('cart-quantity-input')[0]
                var price = parseFloat(priceElement.innerText.replace('$', ''))
                var quantity = quantityElement.value
                total = total + (price * quantity)
            }
            total = Math.round(total * 100) / 100
            document.getElementsByClassName('cart-total-price')[0].innerText = '$' + total
        }

}


