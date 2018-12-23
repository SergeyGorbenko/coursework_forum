$(function () {
    let url = location.href.split("/");
    if (url[3] === "posts") {
        $("#posts").addClass("active_tab");
        $("#users").removeClass("active_tab");
        $("#tags").removeClass("active_tab");
        $("#profile").removeClass("active_tab");
    } else if (url[3] === "users") {
        $("#users").addClass("active_tab");
        $("#posts").removeClass("active_tab");
        $("#tags").removeClass("active_tab");
        $("#profile").removeClass("active_tab");
    } else if (url[3] === "tags") {
        $("#tags").addClass("active_tab");
        $("#users").removeClass("active_tab");
        $("#posts").removeClass("active_tab");
        $("#profile").removeClass("active_tab");
    } else if (url[3] === "profile") {
        $("#profile").addClass("active_tab");
        $("#tags").removeClass("active_tab");
        $("#users").removeClass("active_tab");
        $("#posts").removeClass("active_tab");

        $("#comment_form").on("submit", function (event) {
            event.preventDefault();
            create_comment_post();
            location.reload();
        });

        $.ajaxSetup({
            headers: {"X-CSRFToken": getCookie("csrftoken")}
        });

        function create_comment_post() {
            $.ajax({
                url: "comment/",
                type: "POST",
                data: {
                    context: $(".comment_text_area").val(),
                    creator: "{{ post.creator }}",
                    post: "{{ post.id }}"
                },
                success() {
                    $(".comment_text_area").val("");
                },
                error(xhr, errmsg) {
                    $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered " +
                        "an error: " + errmsg + " <a href='#' class='close'>&times;</a></div>");
                }
            });
        }

        function getCookie(c_name) {
            let c_start;
            let c_end;
            if (document.cookie.length > 0) {
                c_start = document.cookie.indexOf(c_name + "=");
                if (c_start !== -1) {
                    c_start = c_start + c_name.length + 1;
                    c_end = document.cookie.indexOf(";", c_start);
                    if (c_end === -1) c_end = document.cookie.length;
                    return unescape(document.cookie.substring(c_start, c_end));
                }
            }
            return "";
        }
    }
);