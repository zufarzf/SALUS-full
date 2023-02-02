
$(document).ready(function () {
    // Header
    // ===========================================

    // Burger menu active
    // -------------------------------------------
    $('.burger_button').on('click', function (e) {
        e.preventDefault();

        if ($('.header-langs__list').hasClass('header-langs__list-active')) {

            $('.header-langs__list').removeClass('header-langs__list-active');
        }
        $('span.burger_button-line').toggleClass('burger_button-line-active')
        $('nav.burger_button-nav_bar').toggleClass('burger_button-nav_bar-active')
    })
    // -------------------------------------------

    // Language list active
    // -------------------------------------------
    $('.header-lang_menu').on('click', function (e) {
        e.preventDefault();

        if ($('span.burger_button-line').hasClass('burger_button-line-active')) {

            $('span.burger_button-line').removeClass('burger_button-line-active');
            $('nav.burger_button-nav_bar').removeClass('burger_button-nav_bar-active');
        }
        // Language list active
        $('.header-langs__list').toggleClass('header-langs__list-active')
    })
    // -------------------------------------------




    // Services -> section active
    // -------------------------------------------
    var more_is_checked = $("a.services-section_name");
    // -------------------------------------------
    more_is_checked.click(function (e) {
        e.preventDefault();
        $(this).children('span.services-section_name-open').toggleClass('services-section_name-open-active');
        $(this).parent().children('.services-section-list').toggleClass('services-section-list-active');
    });
    // -------------------------------------------
    // end Services -> section active





    // Функция подсчета количества символов	- START
    function limitChars(myObject, max, leftChars) {
        $(myObject).keydown(function () {
            var count = $(this).val().length; // кол-во уже введенных символов
            var num = max - count; // кол-во символов, которое еще можно ввести

            if (num > 0) {
                // если не достигнут лимит символов
                $(leftChars).text('Осталось ' + num + ' символов');
                $(this).removeClass('type');
            } else {
                // если достигнут лимит символов
                $(leftChars).text('Достигнут лимит символов');
                $(this).addClass('type');
            }
        });
    }
    // Функция подсчета количества символов - END

    $(document).ready(function () {
        var myObject = '.leave_a_review-textarea'; // объект, у которого считаем символы
        var max = 330; // максимум символов
        var leftChars = '#leave_a_review-textarea__text_lenth'; // куда выводим кол-во оставшихся символов

        limitChars(myObject, max, leftChars);
    });

    // ===============================================
});






// Slider Swiper
// Initialization Swiper
// Main page swiper
// ===========================================
new Swiper('.main_page-content__slider', {
    speed: 700,
    allowTouchMove: true,

    // Запоминает место слайда
    hashNavigation: { watchState: true },

    simulateTouch: false,

    // Положение
    direction: 'vertical',

    // Отступы
    spaceBetween: 10,

    // Dots
    pagination: {
        el: '.main_page-swiper_progressbar',
        clickable: true,
        type: 'progressbar',
        progressbarOpposite: true
    },

    // Изменение с кнопками клавиатуры
    keyboard: {
        enabled: true,
        onlyInViewport: true,
        pageUpDown: true,
    },

    // Изменение при скролле
    mousewheel: {
        sensitivity: 1,
        eventsTarget: '.main_page-content__slider',
    },

    // Media
    breakpoints: {
        1300: {
            direction: 'horizontal',
            allowTouchMove: true,
            simulateTouch: false,
            touchRatio: 0.5,
            pagination: {
                el: '.main_page-swiper_progressbar',
                type: 'progressbar',
                progressbarOpposite: false
            },
        }
    }
});
// ===========================================
// end Slider Swiper

// Deportament swiper
// ===========================================
new Swiper('.departments_cards_container', {
    nested: true,
    speed: 700,
    slidesPerView: 1,
    autoHeight: false,

    // Rows
    grid: { rows: 2 },

    // Margin
    spaceBetween: 25,

    // Dots
    pagination: {
        el: '.deportaments_cards_swiper_pagination',
        clickable: true,
    },

    // Media
    breakpoints: {
        1300: { slidesPerView: 4, },
        950: { slidesPerView: 3, },
        620: { slidesPerView: 2, },
    }
});
// ===========================================
// end Deportament swiper




// Doctors swiper
// ===========================================
new Swiper('.doctors_cards_container', {
    nested: true,
    speed: 700,
    slidesPerView: 1,
    autoHeight: false,
    // centeredSlides: true,
    // Rows
    grid: { rows: 1 },
    spaceBetween: 10,

    // Dots
    pagination: {
        el: '.doctors_cards_swiper_pagination',
        clickable: true,
    },
    // Media
    breakpoints: {
        1660: {
            slidesPerView: 4,
            spaceBetween: 55,
        },
        1210: {
            slidesPerView: 4,
            spaceBetween: 30,
        },
        820: {
            slidesPerView: 3,
            spaceBetween: 20,
        },
        680: {
            slidesPerView: 2,
            spaceBetween: 100,
        },
    }
});
// ===========================================
// end Deportament swiper






// Slider Swiper
// Initialization Swiper
// About swiper
// ===========================================
new Swiper('.gallery-swiper_slider', {
    speed: 700,
    slidesPerView: 1,
    autoHeight: false,
    // centeredSlides: true,
    // Rows

    centerInsufficientSlides: true,
    centeredSlides: true,
    centeredSlidesBounds: true,
    loop: true,

    // Изменение с кнопками клавиатуры
    keyboard: {
        enabled: true,
        onlyInViewport: true,
        pageUpDown: true,
    },

    // Изменение при скролле
    mousewheel: {
        sensitivity: 1,
        eventsTarget: '.gallery-swiper_slider',
    },

    // Margin
    spaceBetween: 20,

    // Dots
    pagination: {
        el: '.doctors_cards_swiper_pagination',
        clickable: true,
    },
    // Media
    breakpoints: {
        1660: { slidesPerView: 3.5, },
        1210: { slidesPerView: 3, },
        815: { slidesPerView: 2, },
    }
});
// ===========================================
// end Slider Swiper



// Slider Swiper
// Initialization Swiper
// Service doctors swiper
// ===========================================
new Swiper('.doctors_slider', {
    speed: 700,
    slidesPerView: 1,
    autoHeight: false,
    // centeredSlides: true,
    // Rows

    centerInsufficientSlides: true,
    centeredSlides: true,
    centeredSlidesBounds: true,
    loop: true,

    // Изменение с кнопками клавиатуры
    keyboard: {
        enabled: true,
        onlyInViewport: true,
        pageUpDown: true,
    },

    // Изменение при скролле
    mousewheel: {
        sensitivity: 1,
        eventsTarget: '.doctors_slider',
    },

    // Margin
    spaceBetween: 20,

    // Dots
    pagination: {
        el: '.doctors_cards_swiper_pagination',
        clickable: true,
    },
    // Media
    breakpoints: {
        1660: { slidesPerView: 6, },
        1250: { slidesPerView: 5, },
        920: { slidesPerView: 4, },
        660: { slidesPerView: 3, },
        470: { slidesPerView: 2, },
    }
});
// ===========================================
// end Slider Swiper


// Hidden message body
setTimeout(function () {
    $('.message-body').fadeOut();
}, 5000)