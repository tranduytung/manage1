//$(document).ready(function (e){
//    $('#upload-file-btn').click(function() {
//        var fdata = new FormData()
//        fdata.append('student_id',$('#student_id').val());
//        if($("#my_file")[0].files.length>0){
//            fdata.append("file",$("#my_file")[0].files[0])
//        }
//        $.ajax({
//            type: 'POST',
//            url: '/student/save_avatar',
//            data: fdata,
//            contentType: false,
//            processData: false,
//            success: function(data) {
//                $('#avatar').html( '<img width="100px" height="100px" src="'+data+'"/>' );
//                $('#div_action').hide();
//                document.getElementById('upload-file').style.backgroundImage = 'url('+data+')';
//            },
//        });
//        return false;
//    });
//});