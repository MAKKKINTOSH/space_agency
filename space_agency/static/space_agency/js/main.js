$(document).ready(function(){

	let slider = $('.slider');
	let mainSlider = $('.main-slider');
	let internalSlider = $('.internal-slider');

	slider.slick({
		slidesToShow: 3,
		slidesToScroll: 1,
		dots: false,
		arrows: true,
		centerMode: true,
		focusOnSelect: true,
		touchMove: false,
		centerMode: true,
		asNavFor: ".main-slider"
	});
	mainSlider.slick({
		slidesToShow: 1,
		slidesToScroll: 1,
		dots: false,
		arrows: false,
		touchMove: false,
		centerMode: true,
		fade: true,
		asNavFor: ".slider"
	});
	internalSlider.slick({
		slidesToShow: 1,
		slidesToScroll: 1,
		dots: false,
		arrows: false,
		touchMove: false,
		centerMode: true,
		fade: true,
	});
	slider.on('beforeChange', (event, slick, currentSlide, nextSlide) => {
		current_slide = nextSlide
	})
})

// let current_slide = $('.slider').slick('slickCurrentSlide')

