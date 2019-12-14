const baseUrl = 'http://localhost:8000/api/v1/';

function getFullPath(path) {
    path = path.replace(/^\/+|\/+$/g, '');
    path = path.replace(/\/{2,}/g, '/');
    return baseUrl + path + '/';
}

function makeRequest(path, method, auth=true, data=null) {
    let settings = {
        url: getFullPath(path),
        method: method,
        dataType: 'json'
    };
    if (data) {
        settings['data'] = JSON.stringify(data);
        settings['contentType'] = 'application/json';
    }
    if (auth) {
        settings.headers = {'X-CSRFToken': getToken()};
    }
    return $.ajax(settings);
}



function getToken(name='csrftoken') {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;

}
let createCommentForm, editCommentForm,formCreateSubmit, editTextInput, createTextInput, commentBlock;
function setUpGlobalVars(){
    createCommentForm = $('#comment_create');
    createTextInput = $('#comment_text_create');
    commentBlock = $('#comments');
    formCreateSubmit = $('#CreateFormSubmit');


}
function createComment(text, photo){
    let credentials = {text, photo};
    let request = makeRequest('comment', 'post', true, credentials);
    request.done(function(data, status, response){
        commentBlock.prepend($(`
            <div class="comment border-dark">
            <h4>Комментарий от пользователя ${data.author}</h4>
            <p>${data.text}</p>
            <p>Дата создания: ${data.created_at }</p>
            </div>
            <a href="" class="btn btn-danger" id="delete_comment_${ data.id }">Удалить комментарий</a>
                <a href="" class="btn btn-info" id="update_comment_${ data.id }">Изменить комментарий</a>
                <script>
                    $("#delete_comment_${ data.id }").on('click', function(event){
                        event.preventDefault();
                        deleteComment(${ data.id });
                    });
                </script>
        `));
        createTextInput.val("");
    }).fail(function (response, status, message) {
        console.log(response.responseText);
    })
}
function deleteComment(id){
    let request = makeRequest('comment/' + id, 'delete', true, )
    request.done(function(data,status,response){
        $(`#comment_${id}`).addClass('d-none');
        console.log("deleted");
    }).fail(function(response, status, message){
        console.log(response.responseText);
    })
}
function likePhoto(id){
    let request = makeRequest('like/' + id, 'patch', true,);
    request.done(function(data,status,response){
        console.log(response.responseText)
        console.log($("#rating").val())


    }).fail(function(response, status, message){
        console.log(response.responseText);
    })
}
function dislikePhoto(id){
    let request = makeRequest('dislike/' + id, 'patch', true,);
    request.done(function(data,status,response){
        console.log(response.responseText);
        $("#rating").val(`Рейтинг :`+response.likes);

    }).fail(function(response, status, message){
        console.log(response.responseText);
    })
}
function setUpButtons(){
    createCommentForm.on('submit', function(event){
        event.preventDefault();
        createComment(createTextInput.val(), photoId);
    });
    formCreateSubmit.off('click');
    formCreateSubmit.on('click', function (event) {
            event.preventDefault();
            createCommentForm.submit();
    })
}


function checkAuth() {
    if (getToken()){
        createCommentForm.removeClass('d-none');
       // editCommentForm.removeClass('d-none');
    }
    else{
        createCommentForm.addClass('d-none');
        //editCommentForm.addClass('d-none');
    }
}

$(document).ready(function() {
    setUpGlobalVars();
    checkAuth();
    setUpButtons();
});

