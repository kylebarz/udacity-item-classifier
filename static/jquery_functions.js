$(document).ready(function(){
    $(".upload-button").click(function(){
        $("#fileId").click();
    })
    $('#predict').prop('disabled',true);
    $("#fileId").change(function(){
        $("#fileId").click();
		var x = 3;
        var value = $("#fileId").val();
        var text1=$("#labelId").text();
        if (value != ""){
            $("#labelId").html(value.split('\\').pop());
        } else {
            $("#labelId").html("Choose a file");
        }
        $('#predict').prop('disabled',false);
    })

    $('#predict').click(function() {
        event.preventDefault();
        $("#uploads").show();
        $("#result").show();
        $('#result p').text('Please wait...')
        var reader = new FileReader();

        reader.onload = function (e) {
            $('#uploaded_image')
                .attr('src', e.target.result)
                .width(150)
                .height(200);
        };

        reader.readAsDataURL(fileId.files[0]);

        var response_count = 0;

        var form_data = new FormData($('#formId')[0]);
        $.ajax({
            type: 'POST',
            url: '/uploadajax',
            data: form_data,
            contentType: false,
            cache: false,
            processData: false,
            success: function(data) {
                console.log(data);
                console.log(JSON.stringify(data));
                $("#labelId").html("Choose a file");

                $('#result').empty()
                $(jQuery.parseJSON(JSON.stringify(data))).each(function() {
                     var INDEX = this.index;
                     var CLASS = this.class;
                     var SCORE = this.score;
                     console.log(INDEX)
                     console.log(CLASS)
                     console.log(SCORE)
                     console.log('/product_images/' + CLASS + '.jpg')
                     //$('#result p').append(item);
                     content = '<p>Predicted Item: ' + CLASS + ' Prediction Score: ' + SCORE + '</p>';
                     $('#result').append(content);
                     if ( response_count == 0 ) {
                        $('#predicted_image').attr('src','/static/product_photos/' + CLASS + '/1.jpg');
                     }

                     response_count += 1
                     //$('#result p').innerHTML += "Predicted Item: " + CLASS + " Prediction Score: " + SCORE + "<br/>";
                });
                //$('#result p').text(data);
                $('#predict').prop('disabled',true);
            }
        })
    });

});