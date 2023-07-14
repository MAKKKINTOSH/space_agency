$(document).ready(function(){

	let slider = $('.slider');
	let mainSlider = $('.main-slider');

	slider.slick({
		slidesToShow: 5,
		slidesToScroll: 1,
		arrows: true,
		focusOnSelect: true,
		centerMode: true,
		centerPadding: true,
		touchMove: false,
		asNavFor: ".main-slider",
		responsive:[
			{
				breakpoint: 576,
				settings: {
					arrows: false
				}
			}
		]
	});
	mainSlider.slick({
		slidesToShow: 1,
		slidesToScroll: 1,
		dots: false,
		arrows: false,
		touchMove: false,
		fade: true,
		asNavFor: ".slider"
	});
})
