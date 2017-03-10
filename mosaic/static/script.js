$(function () {
  $('#upload-file-btn').click(function () {

    var form_data = new FormData($('#upload-file')[0]);

    $.ajax({
      type: 'POST',
      url: '/index',
      data: form_data,
      contentType: false,
      cache: false,
      processData: false,
      async: false,
      success: function (data) {
        if (data.message != undefined){
          alert(data.message);
        }
        // $('#result').html(data.result);
        $('#result').attr("src", data.result);
      }
    });
  });
});

function readURL(input) {
  if (input.files && input.files[0]) {
    var reader = new FileReader();
    reader.onload = function (e) {
      // $('#uploadImg').attr('src', e.target.result);
      // $('#uploadImg').css({"background-image": "url(" + e.target.result + ")"});
      $('#uploadImg').attr("src", e.target.result);
    };
    reader.readAsDataURL(input.files[0]);
  }
}
$("#inputImage").change(function () {
  readURL(this);
});