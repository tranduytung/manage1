//var imageLoader = document.getElementById('my_file');
//    imageLoader.addEventListener('change', handleImage, false);
//    var MAX_SIZE = 5*1024*1024 // 5Mb = 5 * 1024 * 1024 (Byte)
//
//    function handleImage(e) {
//        var FileUploadPath = imageLoader.value;
//        var Extension = FileUploadPath.substring(FileUploadPath.lastIndexOf('.') + 1).toLowerCase();
//        //The file uploaded is an image
//        if (Extension == "gif" || Extension == "png" || Extension == "bmp"
//            || Extension == "jpeg" || Extension == "jpg") {
//            if(imageLoader.files[0].size > MAX_SIZE){
//                alert("Photo max size is 5Mb. ");
//            }
//            else{
//                e.stopPropagation();
//                e.preventDefault();
//                var reader = new FileReader();
//                reader.onload = function (event) {
//                    $('#img_src').html( '<img id="blah" height="350px" src="'+event.target.result+'"/>' );
//                    $('#div_action').show();
//                    setTimeout(initCropper, 1000);
//                }
//                reader.readAsDataURL(e.target.files[0]);
//            }
//        }
//        else{
//            alert("Photo only allows file types of GIF, PNG, JPG, JPEG and BMP. ");
//        }
//    }
//
//    $('#cancle-upload-btn').click(function() {
//        $('#div_action').hide();
//    });
//
//
//    function initCropper(){
//        console.log("Came here")
//        var image = document.getElementById('blah');
//        var cropper = new Cropper(image, {
//          aspectRatio: 1 / 1,
//          crop: function(e) {
//            console.log(e.detail.x);
//            console.log(e.detail.y);
//          }
//        });
//
//        // On crop button clicked
//        $('#upload-file-btn').click(function(){
//            cropper.getCroppedCanvas().toBlob(function (blob) {
//                var fdata = new FormData();
//                fdata.append('student_id',$('#student_id').val());
//                fdata.append('file', blob);
//                $.ajax({
//                    type: 'POST',
//                    url: '/student/save_avatar',
//                    data: fdata,
//                    contentType: false,
//                    processData: false,
//                    success: function(data) {
//                        $('#div_action').hide();
//                        document.getElementById('upload-file').style.backgroundImage = 'url('+data+')';
//                    },
//                });
//                return false;
//            });
//            return false;
//        });
//    }