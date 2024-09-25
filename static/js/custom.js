const scrollElements = document.querySelectorAll(".js-scroll");
const filterButtons = document.querySelectorAll(".myBtnContainer button");
const filterableImages = document.querySelectorAll(".gall-images .item");

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
  e.preventDefault()
  document.querySelector(".myBtnContainer .active").classList.remove("active");
  e.target.classList.add("active");
  filterableImages.forEach(item =>{
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


