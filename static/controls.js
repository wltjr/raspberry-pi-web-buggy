/*
    var actions = ['move_backward', 'move_forward', 'stop', 'turn_left', 'turn_right'];
    function buttonActions(acts) {
        for(var i = 0; i < acts.length; i++) {
                $('a#'+acts[i]).on('click', function(e) {
                   console.log("action "+acts[i]);
                  e.preventDefault()
                  $.getJSON('/test'+acts[i],
                      function(data) {
                      //do nothing
                  });
                  return false;
                });
            }
        }
        $(function() {
            buttonActions(actions);
        });
*/
$(function () {
    $('a#move_backward').on('click', function (e) {
        e.preventDefault()
        $.getJSON('/move_backward',
            function (data) {
                //do nothing
            });
        return false;
    });
});
$(function () {
    $('a#move_forward').on('click', function (e) {
        e.preventDefault()
        $.getJSON('/move_forward',
            function (data) {
                //do nothing
            });
        return false;
    });
});
$(function () {
    $('a#stop').on('click', function (e) {
        e.preventDefault()
        $.getJSON('/stop',
            function (data) {
                //do nothing
            });
        return false;
    });
});
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