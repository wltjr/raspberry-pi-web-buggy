/* Copyright 2020-2023 Florida State College at Jacksonville
* Author William L. Thomson Jr. <w@wltjr.com>
*
* Distributed under the terms of The GNU Public License v3.0 (GPLv3)
*/

function submitForm(e) {
    $("#action").val(window.event.target.innerHTML);
    $.ajax({
        url: "/action",
        type: 'post',
        dataType: 'json',
        data: $("#controls").serialize()
    });
}
$(function () {
    $("#speed_lock").click(function () {
        if ($(this).is(":checked")) {
            $("#speed_right").val($("#speed_left").val())
        }
    });
});
$(function () {
    $("#speed_left").change(function () {
        if ($("#speed_lock").is(":checked")) {
            $("#speed_right").val($("#speed_left").val())
        }
    });
});
$(function () {
    $("#speed_right").change(function () {
        if ($("#speed_lock").is(":checked")) {
            $("#speed_left").val($("#speed_right").val())
        }
    });
});