let searchForm = document.querySelector(".search-form");
let searchbtn = document.querySelector("#search-btn");

searchbtn.onclick = () =>{
    searchForm.classList.toggle('active');
    shoppingCart.classList.remove('active');
    loginForm.classList.remove('active');
    navBar.classList.remove('active');
}

let shoppingCart = document.querySelector(".shopping-cart");
let cartBtn = document.querySelector("#cart-btn");

cartBtn.onclick = () =>{
    shoppingCart.classList.toggle('active');
    searchForm.classList.remove('active');
    loginForm.classList.remove('active');
    navBar.classList.remove('active');
}

let loginForm = document.querySelector(".login-form");
let loginBtn = document.querySelector("#login-btn");

loginBtn.onclick = () =>{
    loginForm.classList.toggle('active');
    shoppingCart.classList.remove('active');
    searchForm.classList.remove('active');
    navBar.classList.remove('active');
}

let navBar = document.querySelector(".navbar");
let menuBtn = document.querySelector("#menu-btn");

menuBtn.onclick = () =>{
    navBar.classList.toggle('active');
    loginForm.classList.remove('active');
    shoppingCart.classList.remove('active');
    searchForm.classList.remove('active');
}

Window.onscroll = () =>{
    searchForm.classList.remove('active');
    shoppingCart.classList.remove('active');
    loginForm.classList.remove('active');
    navBar.classList.remove('active');
}

var swiper = new Swiper(".product-slider", {
    loop:true,
    spaceBetween: 20,
    
    autoplay: {
        delay:20000,
        disableOnInteraction: false,
    },

    breakpoints: {
      0: {
        slidesPerView: 1,
      },
      768: {
        slidesPerView: 2,
      },
      1020: {
        slidesPerView: 3,
      },
    },
  });

  var swiper = new Swiper(".review-slider", {
    loop:true,
    spaceBetween: 20,
    
    autoplay: {
        delay:20000,
        disableOnInteraction: false,
    },

    breakpoints: {
      0: {
        slidesPerView: 1,
      },
      768: {
        slidesPerView: 2,
      },
      1020: {
        slidesPerView: 3,
      },
    },
  });


  // Get all quantity input containers
const quantityInputs = document.querySelectorAll('.quantity-input');

// Add event listeners to each container
quantityInputs.forEach(function(input) {
    const decrementButton = input.querySelector('.decrement');
    const incrementButton = input.querySelector('.increment');
    const quantityInput = input.querySelector('.quantity');

    // Decrement quantity when "-" button is clicked
    decrementButton.addEventListener('click', function() {
        let value = parseInt(quantityInput.value);
        if (value > 1) {
            value--;
            quantityInput.value = value;
        }
    });

    // Increment quantity when "+" button is clicked
    incrementButton.addEventListener('click', function() {
        let value = parseInt(quantityInput.value);
        value++;
        quantityInput.value = value;
    });
});
