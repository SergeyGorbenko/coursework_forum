$(function () {
    let url = location.href.split("/");
    if (url[3] === "posts") {
        $("#posts").addClass("active_tab");
        $("#users").removeClass("active_tab");
        $("#tags").removeClass("active_tab");
    } else if (url[3] === "users") {
        $("#users").addClass("active_tab");
        $("#posts").removeClass("active_tab");
        $("#tags").removeClass("active_tab");
    } else if (url[3] === "tags") {
        $("#tags").addClass("active_tab");
        $("#users").removeClass("active_tab");
        $("#posts").removeClass("active_tab");
    }
});