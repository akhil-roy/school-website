const scrollElements = document.querySelectorAll(".js-scroll");
const filterButtons = document.querySelectorAll(".myBtnContainer button");
const categoryHead = document.querySelectorAll(".categoryhead");

const elementInView = (el, dividend = 1) => {
  const elementTop = el.getBoundingClientRect().top;

  return (
    elementTop <=
    (window.innerHeight || document.documentElement.clientHeight) / dividend
  );
};

const elementOutofView = (el) => {
  const elementTop = el.getBoundingClientRect().top;

  return (
    elementTop > (window.innerHeight || document.documentElement.clientHeight)
  );
};

const displayScrollElement = (element) => {
  element.classList.add("scrolled");
};

const hideScrollElement = (element) => {
  element.classList.remove("scrolled");
};

const handleScrollAnimation = () => {
  scrollElements.forEach((el) => {
    if (elementInView(el, 1.15)) {
      displayScrollElement(el);
    }
    //  else if (elementOutofView(el)) {
    //   hideScrollElement(el)
    // }
  })
};

window.addEventListener("scroll", () => { 
  handleScrollAnimation();
});

const filterimages = e =>{
  e.preventDefault();
  document.querySelector(".myBtnContainer .active").classList.remove("active");
  e.target.classList.add("active");
  categoryHead.forEach(item=>{
    item.classList.add("hide");
    if(item.dataset.name === e.target.dataset.name || e.target.dataset.name === "all"){
      item.classList.remove("hide");
    }
  });
};
filterButtons.forEach(button => button.addEventListener("click",filterimages));

        
        
$(document).ready(function() {

  $('.counter').each(function () {
$(this).prop('Counter',0).animate({
  Counter: $(this).text()
}, {
  duration: 5000,
  easing: 'swing',
  step: function (now) {
      $(this).text(Math.ceil(now));
  }
});
});

});  

// Get the button
let mybutton = document.getElementById("backToTopBtn");

// When the user scrolls down 20px from the top of the document, show the button
window.onscroll = function() {scrollFunction()};

function scrollFunction() {
  if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
    mybutton.style.display = "block";
  } else {
    mybutton.style.display = "none";
  }
}

// When the user clicks on the button, scroll to the top of the document
function topFunction() {
  document.body.scrollTop = 0; // For Safari
  document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
}

