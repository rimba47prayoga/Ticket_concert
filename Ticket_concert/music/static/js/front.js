$(document).ready(function () {

    'use strict';

    // ------------------------------------------------------- //
    // Search Box
    // ------------------------------------------------------ //
    $('#search').on('click', function (e) {
        e.preventDefault();
        $('.search-box').fadeIn();
    });
    $('.dismiss').on('click', function () {
        $('.search-box').fadeOut();
    });

    // ------------------------------------------------------- //
    // Card Close
    // ------------------------------------------------------ //
    $('.card-close a.remove').on('click', function (e) {
        e.preventDefault();
        $(this).parents('.card').fadeOut();
    });


    // ------------------------------------------------------- //
    // Adding fade effect to dropdowns
    // ------------------------------------------------------ //
    $('.dropdown').on('show.bs.dropdown', function () {
        $(this).find('.dropdown-menu').first().stop(true, true).fadeIn();
    });
    $('.dropdown').on('hide.bs.dropdown', function () {
        $(this).find('.dropdown-menu').first().stop(true, true).fadeOut();
    });


    // ------------------------------------------------------- //
    // Sidebar Functionality
    // ------------------------------------------------------ //
    $('#toggle-btn').on('click', function (e) {
        e.preventDefault();
        $(this).toggleClass('active');

        $('.side-navbar').toggleClass('shrinked');
        $('.content-inner').toggleClass('active');
        $(document).trigger('sidebarChanged');

        if ($(window).outerWidth() > 1183) {
            if ($('#toggle-btn').hasClass('active')) {
                $('.navbar-header .brand-small').hide();
                $('.navbar-header .brand-big').show();
            } else {
                $('.navbar-header .brand-small').show();
                $('.navbar-header .brand-big').hide();
            }
        }

        if ($(window).outerWidth() < 1183) {
            $('.navbar-header .brand-small').show();
        }
    });

    // ------------------------------------------------------- //
    // Universal Form Validation
    // ------------------------------------------------------ //

    $('.form-validate').each(function() {  
        $(this).validate({
            errorElement: "div",
            errorClass: 'is-invalid',
            validClass: 'is-valid',
            ignore: ':hidden:not(.summernote, .checkbox-template, .form-control-custom),.note-editable.card-block',
            errorPlacement: function (error, element) {
                // Add the `invalid-feedback` class to the error element
                error.addClass("invalid-feedback");
                console.log(element);
                if (element.prop("type") === "checkbox") {
                    error.insertAfter(element.siblings("label"));
                } 
                else {
                    error.insertAfter(element);
                }
            }
        });

    });    

    // ------------------------------------------------------- //
    // Material Inputs
    // ------------------------------------------------------ //

    var materialInputs = $('input.input-material');

    // activate labels for prefilled values
    materialInputs.filter(function() { return $(this).val() !== ""; }).siblings('.label-material').addClass('active');

    // move label on focus
    materialInputs.on('focus', function () {
        $(this).siblings('.label-material').addClass('active');
    });

    // remove/keep label on blur
    materialInputs.on('blur', function () {
        $(this).siblings('.label-material').removeClass('active');

        if ($(this).val() !== '') {
            $(this).siblings('.label-material').addClass('active');
        } else {
            $(this).siblings('.label-material').removeClass('active');
        }
    });

    // ------------------------------------------------------- //
    // Footer 
    // ------------------------------------------------------ //   

    var contentInner = $('.content-inner');

    $(document).on('sidebarChanged', function () {
        adjustFooter();
    });

    $(window).on('resize', function () {
        adjustFooter();
    })

    function adjustFooter() {
        var footerBlockHeight = $('.main-footer').outerHeight();
        contentInner.css('padding-bottom', footerBlockHeight + 'px');
    }

    // ------------------------------------------------------- //
    // External links to new window
    // ------------------------------------------------------ //
    $('.external').on('click', function (e) {

        e.preventDefault();
        window.open($(this).attr("href"));
    });

    // ------------------------------------------------------ //
    // For demo purposes, can be deleted
    // ------------------------------------------------------ //

    var stylesheet = $('link#theme-stylesheet');
    $("<link id='new-stylesheet' rel='stylesheet'>").insertAfter(stylesheet);
    var alternateColour = $('link#new-stylesheet');

    if ($.cookie("theme_csspath")) {
        alternateColour.attr("href", $.cookie("theme_csspath"));
    }

    $("#colour").change(function () {

        if ($(this).val() !== '') {

            var theme_csspath = 'css/style.' + $(this).val() + '.css';

            alternateColour.attr("href", theme_csspath);

            $.cookie("theme_csspath", theme_csspath, {
                expires: 365,
                path: document.URL.substr(0, document.URL.lastIndexOf('/'))
            });

        }

        return false;
    });

    // ------------------------------------------------------ //
    // For click button , elm album
    // ------------------------------------------------------ //

    if (typeof GD == 'undefined') {
        window.GD = {
            get_url_albums : function(data) {
            var _url =  "/static/img/GreenDay/albums/"
            var result = _url + data;
            return result;
            },

            clear_content_elem : function() {
                $('div#GreenDay_slide, div#albums-container,section.projects').remove()
            },

            handler_album_click : function() {
                if ($("div#btn_detail_album").is(':visible')) {
                    $("div#btn_detail_album").click(function (event) {
                        var links = this.dataset.links;
                        $.ajax({
                            url: links,
                            beforeSend: function (data) {
                                GD.clear_content_elem();
                                $('body').append('<div class="dropSheet" style="height:' + $('body')[0].offsetHeight + 'px"></div>');
                                $('div.dropSheet').append('<i style="position: absolute;z-index: 1000000;color: white;top: 4em;left: 9em;" class="fa fa-circle-o-notch fa-pulse fa-4x fa-fw"></i>');
                                GD.processAjaxData(links);
                            },
                            success: function (data) {
                                $('div.dropSheet').remove();
                                $(data).appendTo($('div.content-inner'));
                                var album_name = $('p#album-name').text()
                                var home = document.createElement('a')
                                home.href = '/'
                                home.textContent = 'Home '
                                var site_map = document.querySelector('h2.no-margin-bottom');
                                site_map.textContent = '';
                                site_map.appendChild(home);
                                var text_album = document.createTextNode(' > ' + 'Album' + ' > ' +album_name)
                                site_map.appendChild(text_album);
                            }
                        })
                    })
                } else {
                    setTimeout(this.handler_album_click, 1000)
                }

            },
            processAjaxData: function(urlPath){
                window.history.pushState({"html":'GD',"pageTitle":'Green Day'},"", urlPath);
            },
            get_csrf : function() {
            return document.cookie.replace(/csrftoken\=/, '')
            },
            check_RadioChecked : function(Selector) {
                var radio = document.querySelectorAll(Selector);
                for (var i = 0; i < radio.length; i++) {
                    if (radio[i].checked) {
                        return true;
                        break;
                    }
                }
            },
            AssignObject: function () {
                var resObj = {};
                for (var i = 0; i < arguments.length; i++) {
                    var obj = arguments[i],
                        keys = Object.keys(obj);
                    for (var j = 0; j < keys.length; j++) {
                        resObj[keys[j]] = obj[keys[j]];
                    }
                }
                return resObj; //result Object
            }
        }
        
    }

    
});