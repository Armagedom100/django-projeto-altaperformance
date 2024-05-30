'use strict';


/*
*Loading
*/

const loading = document.querySelector("[pageloading]");

window.addEventListener("load", function() {
    loading.classList.add("loaded");
    document.body.classList.add("loaded");
});

const addEvents = function (elements, event, callback) {
    for (let i = 0, len = elements.length;i<len;i++) {
        elements[i].addEventListener(event, callback);
    }
}

const barra = document.querySelector("[navbar");
const togglers = document.querySelectorAll("[navtoggler");
const overlay = document.querySelector("[pageoverlay")
const toggleBarra = function() {
    barra.classList.toggle("active");
    overlay.classList.toggle("active");
    document.body.classList.toggle("nav-active");
}

addEvents(togglers, "click", toggleBarra);

const header = document.querySelector("[pageheader");
let lastScrollPos = 0;
const esconder = function() {
    const isScrollBottom = lastScrollPos < window.scrollY;
    if(isScrollBottom){
        header.classList.add("hide");
    } else{
        header.classList.remove("hide");
    }
    lastScrollPos = window.scrollY;
}

window.addEventListener("scroll", function(){
    if(window.scrollY >= 50){
        header.classList.add("active");
        esconder();
    } else {
        header.classList.remove("active");
    }
});


const rollSlide = document.querySelector("[page-slide]");
const rollSlideItem = document.querySelectorAll("[page-slide-item]");
const rollSlidePrevBtn = document.querySelector("[prev-btn]");
const rollSlideNextBtn = document.querySelector("[next-btn]");

let currentSlide = 0;
let lastActiveSlideItem = rollSlideItem[0];

const updateSlide = function() {
    lastActiveSlideItem.classList.remove("active");
    rollSlideItem[currentSlide].classList.add("active");
    lastActiveSlideItem = rollSlideItem[currentSlide];
}

const nextSlide = function() {
    if (currentSlide >= rollSlideItem.length - 1){
        currentSlide = 0;
    } else {
        currentSlide++;
    }

    updateSlide();
}

rollSlideNextBtn.addEventListener("click", nextSlide);

const prevSlide = function() {
    if (currentSlide <= 0) {
        currentSlide = rollSlideItem.length-1;
    } else {
        currentSlide--;
    }

    updateSlide();
}

rollSlidePrevBtn.addEventListener("click", prevSlide);

let automaticSlideInt;

const automaticSlide = function () {
    automaticSlideInt = setInterval(function(){
        nextSlide();
    }, 7000)
}

addEvents([rollSlideNextBtn, rollSlidePrevBtn], "mouseover", function () {
    clearInterval(automaticSlideInt);
});

addEvents([rollSlideNextBtn, rollSlidePrevBtn], "mouseout", automaticSlide);

window.addEventListener("load", automaticSlide);