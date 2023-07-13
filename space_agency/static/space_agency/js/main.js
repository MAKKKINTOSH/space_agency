$(document).ready(function(){
	$('.slider').slick({
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
	$(".main-slider").slick({
		slidesToShow: 1,
		slidesToScroll: 1,
		dots: false,
		arrows: false,
		touchMove: false,
		centerMode: true,
		fade: true,
		asNavFor: ".slider"
	})
	$(".main-slider__item.slick-center").on('click', function(){
		console.log('1233')
	})
})

