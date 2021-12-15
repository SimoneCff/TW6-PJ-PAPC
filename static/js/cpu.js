$(document).on('submit','#buyD',function(e){
    e.preventDefault();
    $.ajax({
        type:'POST',
        url:'/',
        data:{
            id: $("#val").val()},
        success:function(){
            alert('done')
        }
    })
})