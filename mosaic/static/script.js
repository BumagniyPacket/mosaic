$(window).on("load", function () {
  var $preloader = $("#page-preloader"),
    $spinner = $preloader.find(".spinner");
  $spinner.fadeOut();
  $preloader.delay(350).fadeOut("slow");
});

$(".image-wrapper").hide();
$(".progress").hide();


$(function () {
  $("#upload-file-btn").click(function () {

    var form_data = new FormData($("#upload-file")[0]);

    $('.progress').show();

    $.ajax({
      type: 'POST',
      url: '/index',
      data: form_data,
      contentType: false,
      cache: false,
      processData: false,
      async: false,
      success: function (data) {
        if (data.message != undefined) {
          alert(data.message);
        }
        $("#uploadImg").attr("src", data.result);
        $(".progress").hide();
      },
      error: function (data) {
        Materialize.toast("Возникла ошибка! Попробуйте еще раз.", 4000);
      }
    });
  });
});

function readURL(input) {
  if (input.files && input.files[0]) {
    var reader = new FileReader();
    reader.onload = function (e) {
      $("#uploadImg").attr("src", e.target.result);
    };
    reader.readAsDataURL(input.files[0]);
    $(".image-wrapper").show();
    $(".helper").hide();
    $(".form").css("margin-top", "10px");
  }
}
$("#inputImage").change(function () {
  readURL(this);
});